from pymongo import MongoClient


def get_db_handle():

    client = MongoClient(host="localhost",
                         port=int(27017),
                         #  username='admin',
                         #  password='letsgo!'
                         )
    db_handle = client['restoman']
    return db_handle, client
