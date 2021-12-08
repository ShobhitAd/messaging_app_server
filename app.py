# import netifaces
from flask import Flask
import api

from common import DataBase

app = Flask(__name__)
hostname = '127.0.0.1'
port = 8080

app.register_blueprint(api.message_api)
app.secret_key = '\xb9\xafq=\xc8\xb5\xd2\x019<\xde\xd2\x90/\xe2z\xb7\xcc\xc1y\x02S\xe4'

@app.teardown_appcontext
def close_connection(exception):
    DataBase.closeDB()
    if exception is not None:
        print(exception)

# def getIPAddress():
#     ip = '127.0.0.1'
#     for interface_name in netifaces.interfaces():
#         if interface_name == 'lo': # localhost
#             continue
#         addrs = netifaces.ifaddresses(interface_name)
#         if netifaces.AF_INET in addrs:
#             ipObj = addrs[netifaces.AF_INET][0]
#             if 'addr' in ipObj:
#                 ip = ipObj['addr']
#     return ip

if __name__ == '__main__':
    # if hostname == '':
    #     hostname = getIPAddress()
    app.run(host=hostname, port=port, debug=True)