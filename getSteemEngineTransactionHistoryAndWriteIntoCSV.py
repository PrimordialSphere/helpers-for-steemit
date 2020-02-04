import csv
import pandas as pd
from privex.steemengine import SteemEngineToken
from datetime import date

conv = lambda i : i or ''
s = SteemEngineToken()
today = date.today()
csv_columns = ['Timestamp', 'Symbol', 'Quantity', 'Memo', 'Sender', 'To', 'Raw Data', 'Block']
user_name = 'someguy'
token = 'TOKEN'
path_to_file_csv = '%s_%s_overview.csv' % (today, user_name)
path_to_file_xlsx = '%s_%s_overview.xlsx' % (today, user_name)

with open(path_to_file_csv, 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
    writer.writeheader()
    for x in range(0,1):
        for tx in s.list_transactions(user_name, token, 500, x*500):
            writer.writerow({
                'Timestamp' : conv(str(tx['timestamp'])), 
                'Symbol' : conv(tx['symbol']), 
                'Quantity' : str(tx['quantity']), 
                'Memo' : conv(tx['memo']), 
                'Sender' : conv(tx['sender']), 
                'To' : conv(tx['to']),
                'Raw Data' : str(tx['raw_data']),
                'Block' : str(tx['block'])
                        })
            print(
                ##tx
                ##tx['timestamp'], 
                ##tx['symbol'], 
                ##str(tx['quantity']), 
                ##type(tx['quantity'])
                ##tx['memo'],
                ##tx['sender'], 
                ##tx['to'],
                ##str(tx['raw_data']),
                ##str(tx['block'])
        )
            
data = pd.read_csv(path_to_file_csv)
data.to_excel(path_to_file_xlsx)
