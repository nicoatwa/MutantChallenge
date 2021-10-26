import json


def lambda_handler(event, context):
    try:
        print('====================')
        print('event: ' + str(event['body']))
        # Get json parameter
        dna = json.loads(event['body'])
        result = isMutant(dna['dna'])
        if result:
            print('is Mutant')
            return {
                'body': json.dumps('200-OK')
            }
        else:
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

    return isMutant    