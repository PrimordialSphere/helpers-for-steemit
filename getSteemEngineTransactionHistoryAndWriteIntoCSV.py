import csv
import pandas as pd
from privex.steemengine import SteemEngineToken
from datetime import date

conv = lambda i : i or ''
s = SteemEngineToken()
today = date.today()
csv_columns = ['Timestamp', 'Symbol', 'Quantity', 'Memo', 'Sender', 'To', 'Raw Data', 'Block']

with open('%s_beerlover_overview.csv' % today, 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
    writer.writeheader()
    for x in range(0,5):
        for tx in s.list_transactions('someguy', 'TOKEN', 500, x*500):
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
            
data = pd.read_csv('%s_beerlover_overview.csv' % today)
data.to_excel('%s_beerlover_overview.xlsx' % today)
