import requests,json
class usersInfo:

    def __init__(self):
       self.listUsers:

    def getUsers(self):
        responseUsers = requests.get("https://datos.gov.co/resource/jtnk-dmga.json")
        dataJson = responseUsers.json()
        for ind in range(len(dataJson)):
            print(dataJson[ind]['email_address'])
    def validateUsers(self):
        for email inf self.listUsers:
prueba = usersInfo()
prueba.getUsers()




