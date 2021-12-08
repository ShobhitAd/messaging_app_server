from flask import *
from common import validateRequestParams, DataBase

message_api = Blueprint('message_api', __name__)


@message_api.route('/api/v1/messages', methods=['GET'])
def get_messages_route():

    # get JSON request data
    data = request.get_json()
    # db = DataBase()

    msg, status = validateRequestParams(data, ['roomId'])
    if status != 200:
        return jsonify(msg), status

    roomId = str(data['roomId'])

    # Database operations
    connection = DataBase.getDB()

    ## Check if vehicle is available
    cur = connection.cursor()
    cur.execute('SELECT Message.id, sender, contents FROM Room INNER JOIN Message ON Message.id = Room.msgId AND Room.id = ?', (roomId,))
    result = cur.fetchall()
    cur.close()

    print(result)

    messages = []
    for msg in result:
        messages.append({
            "msgId": msg[0],
            "sender": msg[1],
            "contents": msg[2]
        })


    return jsonify(messages), 200


@message_api.route('/api/v1/sendmessage', methods=['POST'])
def send_message_route():

    # get JSON request data
    data = request.get_json()

    msg, status = validateRequestParams(data, ['roomId', 'sender', 'contents'])
    if status != 200:
        return jsonify(msg), status

    # Database operations
    connection = DataBase.getDB()

    roomId = str(data['roomId'])
    sender = str(data['sender'])
    contents = str(data['contents'])

    ## Check if vehicle is available
    cur = connection.cursor()
    cur.execute('INSERT INTO Message(sender, contents) VALUES (?, ?)', (sender, contents))
    cur.execute('SELECT last_insert_rowid()')
    msgId = str(cur.fetchall()[0][0])
    cur.close()


    print(msgId)
    cur = connection.cursor()
    cur.execute('INSERT INTO Room(id, msgId) VALUES (?, ?)', (roomId, msgId))
    cur.close()

    connection.commit()

    message = {
            "msgId": msgId,
            "sender": sender,
            "contents": contents
        }
    return jsonify(message), 200