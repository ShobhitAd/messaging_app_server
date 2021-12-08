import sqlite3
from flask import g

def validateRequestParams(_data, _required_params):
    if len(_required_params) > 0 and not _data:
        json_error = {
            "error": {
                "message": "Invalid/Missing JSON parameters for request"
            }
        }
        return json_error, 400
    
    missingParams = [required_param for required_param in _required_params if required_param not in _data]
    if missingParams != []:
        json_error = {
            "error": {
                "message": "You did not provide the necessary fields. Missing %s" % (', '.join(missingParams))
            }
        }
        return json_error, 422
    
    return ({}, 200)


class DataBase():
    DATABASE_FILE = 'MessagingApp.db'

    @staticmethod
    def getDB():
        db = getattr(g, '_database', None)
        if db is None:
            db = g._database = sqlite3.connect(DataBase.DATABASE_FILE)
        return db
             
    @staticmethod
    def closeDB():
        db = getattr(g, '_database', None)
        if db is not None:
            db.close()

DEBUG = True
def log(_msg):
    if not DEBUG:
        return
    print(log)