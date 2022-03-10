from pymongo import MongoClient

# En este script se utiliza el
# usuario root para la administracion de mongo
try:
    user = 'root'
    password = 'root'

    # connect to mongodb
    client = MongoClient(f'mongodb://{user}:{password}@localhost:27017')

    db = client['newBtc']
    node_collection = db['data']

    node_collection.insert_one({
        'clave': '1020',
        'name': 'TEMP SENSOR 23',
        'value': 9
    })

    results = node_collection.find()

    print('Inserted')

except Exception as e:
    print('Error {}'.format(e))
