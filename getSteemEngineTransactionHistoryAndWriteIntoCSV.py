import csv
from privex.steemengine import SteemEngineToken
from datetime import date

conv = lambda i : i or ''
s = SteemEngineToken()
today = date.today()
csv_columns = ['Timestamp', 'Symbol']

with open('%s_beerlover_overview.csv' % today, 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
    writer.writeheader()
    for tx in s.list_transactions('beerlover', 'BEER', 9000):
        writer.writerow({
            'Timestamp' : conv(str(tx['timestamp'])), 
            'Symbol' : conv(tx['symbol']), 
            'Quantity' : conv(tx['quantity']), 
            'Memo' : conv(tx['memo']), 
            'Sender' : conv(tx['sender']), 
            'To' : conv(tx['to']),
            ##str(tx['raw_data']),
            ##str(tx['block'])
                        })
        print(
            tx
            ##tx['timestamp'], 
            ##tx['symbol'], 
            ##tx['quantity'], 
            ##tx['memo'],
            ##tx['sender'], 
            ##tx['to'],
            ##str(tx['raw_data']),
            ##str(tx['block'])
        )
