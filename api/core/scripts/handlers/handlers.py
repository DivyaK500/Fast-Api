import json

from core.scripts.utils.db import get_db_connection


def get_reception_content():
    db = get_db_connection()
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT data FROM reception_content LIMIT 1")
    result = cursor.fetchone()
    cursor.close()
    db.close()
    return json.loads(result["data"])


def get_clinic_content():
    db=get_db_connection()
    cursor = db.cursor(dictionary=True)
    cursor.execute("""SELECT * from clinic_content""")
    result=cursor.fetchone()
    cursor.close()
    db.close()
    return result

def get_patient_file():
    db=get_db_connection()
    cursor = db.cursor(dictionary=True)
    cursor.execute("""SELECT * from patient_file""")
    result=cursor.fetchone()
    cursor.close()
    db.close()
    return result
def get_side_bar():
    db = get_db_connection()
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT data FROM side_bar LIMIT 1")
    result = cursor.fetchone()
    cursor.close()
    db.close()
    return json.loads(result["data"])
