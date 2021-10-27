import json
import boto3
import time

def lambda_handler(event, context):
    try:
        print('====================')
        print('event: ' + str(event['body']))
        # Get json parameter
        dna = json.loads(event['body'])
        result = isMutant(dna['dna'])
        if result:
            print('is Mutant')
            execute_athena_query(dna['dna'][0], '')
            return {
                'body': json.dumps('HTTP 200-OK')
            }
        else:
            execute_athena_query('', dna['dna'][0])
            return {
                'body': json.dumps('403-Forbidden')
            }
    except BaseException as ex:
        err_msg: str = f"[MutantFunction] {ex.__class__.__name__}: {ex}"
        print("Returning error: " + err_msg)
        return {
            'body': json.dumps(err_msg)
        }

def isMutant(dna: list):
    isMutant=False
    if len(dna) >= 4:
        for dna_str in dna:
    	    count=0
    	    if len(dna_str)==len(dna):
    	        for i in range(1,len(dna_str)):
    	            if dna_str[i-1]=='A' or dna_str[i-1]=='T' or dna_str[i-1]=='C' or dna_str[i-1]=='G':
    	                if dna_str[i-1] == dna_str[i] :
    	                    count+=1
    	                    if count == 3:
    	                        isMutant=True
    	            else:
    	                print("DNA String contains a char different to A,T,C,G")
    	                isMutant=False
    	                break
    	    else:
    		    print("String should contain " + str(len(dna)) + " chars but " + dna_str + " contains: " + str(len(dna_str)))
    		    isMutant=False
    		    break
    else:
        print("Array length must be equal or greater than 4")
    return isMutant    
    
def execute_athena_query(mutant_dna: str, not_mutant_dna: str):
    client = boto3.client('athena')
    # Execution
    query = "INSERT INTO db_dna.dna_register values ('"+mutant_dna+"'"+",'"+not_mutant_dna+"');"
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
                print("SUCCESS")
                break
            else:
                time.sleep(i)