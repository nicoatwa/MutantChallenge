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

* Test Cases for service "/mutant/":

1. pm.test("When Array length is equal or greater than 4 and is equal to Strings length and there is at least one sequence in which the same letter is repeated 4 times, then Status code is 200", function () {
   pm.response.to.have.status(200);
   });
   
   Above test case must be executed using below json:
	
   {"dna":["ATGCGA","CGAGTG","TTATGT","AAAAGG","CCACGT","TCACTG"]}
	
2. pm.test("When Array length is equal or greater than 4 and is equal to Strings length and there is not sequence in which the same letter is repeated 4 times, Status code is 403", function () {
   pm.response.to.have.status(403);
   });

   Above test case must be executed using below json:
	
   {"dna":["ATGCGA","CGAGTG","TTATGT","AATAGG","CCACGT","TCACTG"]}

3. pm.test("When Array length is less than 4, Status code is 403", function () {
   pm.response.to.have.status(403);
   });

   Above test case must be executed using below json:
	
   {"dna":["ATGCGA","CGAGTG","TTATGT"]}

4. pm.test("When Array length is equal or greater than 4 and is greater than at least one String length, Status code is 403", function () {
   pm.response.to.have.status(403);
   });
   
   Above test case must be executed using below json:
	
   {"dna":["ATGCGA","CGAGTG","TTATGT","CCACGT","TCACT","AAAAGG"]}
   
5. pm.test("When Array length is equal or greater than 4 and is lower than at least one String length, Status code is 403", function () {
   pm.response.to.have.status(403);
   });
   
   Above test case must be executed using below json:
	
   {"dna":["ATGCGAT","CGAGTG","TTATGT","CCACGT","TCACGT","AAAAGG"]}

6. pm.test("When Array length is equal or greater than 4 and is equal to Strings length and at least one String contain a character different to A, C, T or G, Status code is 403", function () {
   pm.response.to.have.status(403);
   });

   Above test case must be executed using below json:
	
   {"dna":["ATGRAT","CGAGTG","TTATGT","CCACGT","TCACGT","AAAAGG"]}
   