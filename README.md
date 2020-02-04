# helpers-for-steemit
small python scripts to interact with steemit blockchain


## getSteemEngineTransactionHistoryAndWriteIntoCSV 
Can be used to get a complete history of transactions of a certain account for a specific token on the SteemEngine sidechain of the 
Steemit blockchain. Because every API-Call only seems to deliever 500 Entries, you can specifiy the number of times the call has to be 
repeated each time with a offset+=500 (see line 18). After writing the csv, the programm is also leveraging pandas to create an xlsx as
well.
