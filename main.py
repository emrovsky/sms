import os
from twilio.rest import Client
import random
dogrulama = random.randint(10000,99999)

sor = input("Telefon numaranızı giriniz : ")




account_sid = ('gir guzel kardesim')
auth_token = ('gir guzel kardesim')
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="Dogrulama kodunuz : " + str(dogrulama),
                     from_='+13189333284',
                     to=sor
                 )

print(message.sid)
kod_sor = input("Gönderdiğimiz kodu yazınız : ")
if str(dogrulama) == str(kod_sor):
    print("Doğrulama tamamlandı")

