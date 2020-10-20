import requests
import json
import os
import time

token = str(input("please enter authorization code for your account:"))
#print(f"successfully imputted {token} into variable token")
try:
    url = ' https://account-public-service-prod.ol.epicgames.com/account/api/oauth/token'
    myobj = {'grant_type': 'authorization_code', 'code': token}
    x = requests.post(url, data = myobj, auth=('ec684b8c687f479fadea3cb2ad83f5c6', 'e1f31c211f28413186262d37a13fc84d'))
    #auth="Basic ZWM2ODRiOGM2ODdmNDc5ZmFkZWEzY2IyYWQ4M2Y1YzY6ZTFmMzFjMjExZjI4NDEzMTg2MjYyZDM3YTEzZmM4NGQ="
    #print the response text (the content of the requested file):
    resp = x.text
    dicty = json.loads(resp)
    bond = dicty['access_token']
    accid = dicty['account_id']
    revi = 1
    #print(bond)
    def get_party_id():
        securl = f"https://party-service-prod.ol.epicgames.com/party/api/v1/Fortnite/user/{accid}"
        obj = {}
        auth = {"Authorization": f"Bearer {bond}"}
        print("getting party id....")
        y = requests.get(securl, data=obj, headers=auth).json()
        ppl = dict(y).get("current")
        strin = str(ppl)
        lis = list(strin)
        combolist = lis[9] + lis[10] + lis[11] + lis[12] + lis[13] + lis[14] + lis[15] + lis[16] + lis[17] + lis[18] + lis[19] + lis[20] + lis[21] + lis[22] + lis[23] + lis[24] + lis[25] + lis[26] + lis[27] + lis[28] + lis[29] + lis[30] + lis[31] + lis[32] + lis[33] + lis[34] + lis[35] + lis[36] + lis[37] + lis[38] + lis[39] + lis[40]
        return combolist
        '''yu = y.text
        yup = json.loads(yu)
        yuppi = str(yup).replace("'", '"')
        koko = json.loads(yuppi)
        yuppl = koko["current"]
        ditto = dict(yuppi)
        #newstr = str(yuppl).replace("'", '"')
        #par = json.loads(list(newstr))
        #print(newstr)
        pid = ditto["id"]
        return pid
        #print(f"url is {securl}")'''
    def change_skin():
        third_url = f"https://party-service-prod.ol.epicgames.com/party/api/v1/Fortnite/parties/{get_party_id()}/members/{accid}/meta"
        with open("skin.json", "r+") as f:
            objct = json.load(f) 
        authy = {"Authorization": f"Bearer {bond}"}
        z = requests.patch(third_url, json=objct, headers=authy).json()
        #print(z)
        estr = str(z)
        lista = list(estr)
        if lista[8] == "o":
            rev = z.get("messageVars")
            objct["revision"] = rev[1]
            with open("skin.json", "w+") as fp:
                json.dump(objct, fp, sort_keys=False, indent=4)
            #change_skin()
            #add this to json to also false ready: "Default:GameReadiness_s": "Ready",
            requests.patch(third_url, json=objct, headers=authy)
            print("successfully changed skin")

    def craft():
        guid = str(input("enter GUID of schematic to craft:"))
        third_url = f"https://fortnite-public-service-prod11.ol.epicgames.com/fortnite/api/game/v2/profile/{accid}/client/CraftWorldItem?profileId=theater0&rvn=-1"
        objct = {
            "targetSchematicItemId": guid,
            "numTimesToCraft": 1,
            "targetSchematicTier": "x"
        }
        authy = {"Authorization": f"Bearer {bond}"}
        z = requests.post(third_url, json=objct, headers=authy).json()
        print("request executed")

    def accinfo():
        third_url = f"https://fortnite-public-service-prod11.ol.epicgames.com/fortnite/api/game/v2/profile/{accid}/client/QueryProfile?profileId=metadata&rvn=-1"
        authy = {"Authorization": f"Bearer {bond}"}
        z = requests.post(third_url, json={}, headers=authy).json()
        print("getting account info...")
        time.sleep(2)
        print("step 1: place the following junk into a notepad or visual studio and search for: Schematic:")
        time.sleep(3)
        print("step 2: look for GUIDs. they should look similar (644a2330-d2ff-42d6-a47a-23127fa0e2d3) and be right next to the SIDs")
        time.sleep(3)
        print("step 3: do !craft to craft max level items. when it asks you for a GUID, enter the one you found.")
        print('junk:')
        time.sleep(4)
        print(z)
        #print(z)
        '''estr = str(z)
        lista = list(estr)
        if lista[8] == "o":
            rev = z.get("messageVars")
            objct["revision"] = rev[1]
            with open("skin.json", "w+") as fp:
                json.dump(objct, fp, sort_keys=False, indent=4)
            #change_skin()
            #add this to json to also false ready: "Default:GameReadiness_s": "Ready",
            requests.patch(third_url, json=objct, headers=authy)
            print("successfully changed skin")'''
    
    def emote(eid):
        with open("skin.json", "r+") as c:
            orbeez = json.load(c)
        orbeez["update"] = {
           "Default:FrontendEmote_j": "{\"FrontendEmote\":{\"emoteItemDef\":\"/Game/Athena/Items/Cosmetics/Dances/" + f"{eid}" + "." + f"{eid}" + "\",\"emoteEKey\":\"\",\"emoteSection\":-1}}"
        }
        print("recieved message" + eid)
        with open("skin.json", "w+") as fbi:
            json.dump(orbeez, fbi, sort_keys=False, indent=4)


            
    def goback():
        rawd = str(input("enter a command:"))
        comm = rawd.split()
        if comm[0] == "craft":
            craft()
            goback()
        elif comm[0] == "accountinfo":
            accinfo()
            goback()
        else:
            goback()
    goback()

#except IndexError:
#            await message.reply("authorization code not supplied. be sure to log into epic games website, visit https://www.epicgames.com/id/api/redirect?clientId=ec684b8c687f479fadea3cb2ad83f5c6&responseType=code, and put in the code you see inside the redirect url")
except KeyError:
    print(f"{dicty['errorMessage']}")