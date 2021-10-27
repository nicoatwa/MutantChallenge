# MutantChallenge
* How to run "/mutant/" service: 
1. Send a POST Request from Postman to URL: https://4td88od4c2.execute-api.us-east-1.amazonaws.com/test/mutant
2. Select "body" tab, check "raw" radio button, select "JSON" and type a json like below:

{"dna":["ATGCGA","CGAGTG","TTATGT","AAAAGG","CCACGT","TCACTG"]}

3. Then press "Send" button and wait for the reponse

* How to run "/stats/" service:
1. Send a GET Request from Postman to URL: https://4td88od4c2.execute-api.us-east-1.amazonaws.com/test/stats
2. Select "body" tab, check "raw" radio button, select "JSON" and type a json like below:

{"info": "stats"}

3. Then press "Send" button and wait for the reponse



