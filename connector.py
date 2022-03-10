from pymongo import MongoClient
import json
# En este script se utiliza el
# usuario connector para la administracion de mongo
try:
    user = 'connector'
    password = 'password'

    # connect to mongodb
    client = MongoClient(f'mongodb://{user}:{password}@localhost:27017')

    db = client['newBtc']
    node_collection = db['data']

    info = []

    for doc in node_collection.find():
        info.append({
            'clave': doc['clave'],
            'name': doc['name'],
            'value': doc['value']
        })


    print('All info: ')
    print(str(info))

except Exception as e:
    print('Error {}'.format(e))
