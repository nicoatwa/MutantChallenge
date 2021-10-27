create table db_dna.dna_register (mutant string, not_mutant string)
ROW FORMAT DELIMITED FIELDS TERMINATED BY '\|' 
STORED AS INPUTFORMAT 'org.apache.hadoop.mapred.TextInputFormat' 
OUTPUTFORMAT 'org.apache.hadoop.hive.ql.io.HiveIgnoreKeyTextOutputFormat' 
LOCATION 's3://athenaquerychallenge/dna_register' 
TBLPROPERTIES ( 'has_encrypted_data'='false','serialization.null.format'='');