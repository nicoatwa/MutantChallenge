import json
import time
import boto3

def lambda_handler(event, context):
    try:
        request = event['info']
        if request == 'stats':
            query = "SELECT count(*) FROM db_dna.dna_register;"
            total_dna = execute_athena_query(query)
            query = "SELECT count(*) FROM db_dna.dna_register where mutant is not null;"
            mutant_dna = execute_athena_query(query)
            #Computing stats
            stats = mutant_dna/total_dna
            stats_res = {
                "count_mutant_dna":str(mutant_dna),
                "total_verified_dna":str(total_dna),
                "ratio":str(stats)
            }
            return {
               'ADN': json.dumps(stats_res)
            }
        else:
            return "Wrong value for info key in json event"

    except BaseException as ex:
        err_msg: str = f"[MutantStats] {ex.__class__.__name__}: {ex}"
        print("Returning error: " + err_msg)
        return {
            'body': json.dumps(err_msg)
        }
        
        return "ADN: {" + stats_res + "}" 
    
def execute_athena_query(query: str):
    client = boto3.client('athena')
    # Execution
    print (query)
    response = client.start_query_execution(
        QueryString=query,
        QueryExecutionContext={
            'Database': 'db_dna'
        },
        ResultConfiguration={
            'OutputLocation': 's3://athenaquerychallenge'
        },
            WorkGroup='primary'
    )
    
    query_execution_id = response['QueryExecutionId']
    print(query_execution_id)
    
    retry_count = 100
    for i in range(1, 1 + retry_count):
        query_status = client.get_query_execution(QueryExecutionId=query_execution_id)
        query_execution_status = query_status['QueryExecution']['Status']['State']
        
        if query_execution_status == 'FAILED':
            print(query_status['QueryExecution']['Status']['StateChangeReason'])
            raise Exception("STATUS:" + query_execution_status + " - " + query_status['QueryExecution']['Status']['StateChangeReason'])
        else:
            print(str(i) + " - STATUS:" + query_execution_status)
            if query_execution_status == 'SUCCEEDED':
                break
            else:
                time.sleep(i)
    # get query result
    result = client.get_query_results(QueryExecutionId=query_execution_id)
    value_res = result['ResultSet']['Rows'][1]['Data'][0]['VarCharValue']
    return int(value_res) 
