from flask import *
from common import DataBase
import subprocess

admin_api = Blueprint('admin_api', __name__)

@admin_api.route('/api/v1/admin/reset', methods=['POST'])
def reset_route():
    # Reset the database
    db_fptr = open('setupDB.sql', 'r')
    success = subprocess.call(['sqlite3'], stdin=db_fptr)
    db_fptr.close()

    if success != 0:
        return HTTPComm.error('Reseting database failed')

    return jsonify(), 200
