def __init__(self):
    self.dataJson = []
    self.client = pymongo.MongoClient("mongodb://localhost:27017/")
    self.db = self.client["mydatabase"]
    self.collection = self.db["mycollection"]


def limpieza(self):
    for ind in range(len(self.dataJson)):
        jsonClean = {
            "Year": "",
            "Quarter": "",
            "Provider": "",
            "Income": ""
        }
        # ...
        jsonClean['Year'] = self.dataJson[ind]['anno']
        jsonClean['Quarter'] = self.dataJson[ind]['trimestre']
        jsonClean['Income'] = self.dataJson[ind]['ingresos_por_mensajes']
        print(jsonClean)
        self.collection.insert_one(jsonClean)