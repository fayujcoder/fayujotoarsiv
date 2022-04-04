#pip install git+https://git@github.com/ping/instagram_private_api.git@1.6.0

from instagram_private_api import Client, ClientCompatPatch
from art import *
import time,json,getpass

print(text2art("Fayujx Instagram Arsiv Bot"))
time.sleep(0.8)
print(text2art("by   Fayujx"))
time.sleep(0.8)
print("----------------------------------------------------------------------------------")
time.sleep(0.8)
user_name = "tolgasokuluu"#input("Kullanıcı Adı : ")
password = "noexbaba1"#getpass.getpass('Şifre : ')
print(user_name + " İle giriş yapılıyor...")
api = Client(user_name, password)

toplamsilinen = 0
user_id = api.authenticated_user_id
updates = []
while True:
    results = api.user_feed(user_id)
    if len(results["items"]) == 0:
        break
    for itemm in results["items"]:
        api.media_only_me(itemm["id"], itemm["media_type"])
        toplamsilinen += 1
        print(str(toplamsilinen) + ". Post Arşivlendi Upgraded Fayujx")

"""updates.extend(results.get('items', []))
next_max_id = results.get('next_max_id')
while next_max_id:
    results = api.user_feed(user_id, max_id=next_max_id)
    updates.extend(results.get('items', []))
    next_max_id = results.get('next_max_id')
    updates.sort(key=lambda x: x['pk'])
    jdump = updates
    for dddump in jdump:
        print(api.media_only_me(dddump["id"], dddump["media_type"]))
        toplamsilinen += 1
        print(str(toplamsilinen) + ". Post Arşivlendi")
    print("----------")"""

print("İşlem Tamamlandı")