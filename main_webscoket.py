import requests
import websocket
import json
import pandas as pd

endpoint = 'wss://ftx.com/ws/'
our_msg = json.dumps({'op': 'subscribe',
                      'channel': 'ticker',
                      'market': 'ETH/USD'
                      })


def on_open(ws):
    ws.send(our_msg)


def on_message(ws, message):
    out = json.loads(message)
    df_ = pd.DataFrame(out['data'], index=[0])
    df_.index = pd.to_datetime(df_.time, unit='s')
    print(df_['last'])


ws = websocket.WebSocketApp(endpoint, on_message=on_message, on_open=on_open)
ws.run_forever()

##

# base = "https://ftx.com/api"
# r = requests.get(f'{base}/markets/ETH/USD/candles?resolution=86400')
# print (r.json())

