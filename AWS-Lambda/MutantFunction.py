import json


def lambda_handler(event, context):
    try:
        print('====================')
        print('event: ' + str(event['body']))
        # Get json parameter
        dna = json.loads(event['body'])
        return {
            'statusCode': 200,
            'body': json.dumps('OK')
        }
    except BaseException as ex:
        err_msg: str = f"[MutantFunction] {ex.__class__.__name__}: {ex}"
        print("Returning error: " + err_msg)
        return {
            'statusCode': 500,
            'body': json.dumps(err_msg)
        }
