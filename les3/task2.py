"""
Задание 2.

Ваша программа должна запрашивать пароль
Для этого пароля вам нужно вычислить хеш, используя алгоритм sha256
Для генерации хеша обязательно нужно использовать криптографическую соль
Обязательно выведите созданный хеш

Далее программа должна запросить пароль повторно и вновь вычислить хеш
Вам нужно проверить, совпадает ли пароль с исходным
Для проверки необходимо сравнить хеши паролей

ПРИМЕР:
Введите пароль: 123
В базе данных хранится строка: 555a3581d37993843efd4eba1921
f1dcaeeafeb855965535d77c55782349444b
Введите пароль еще раз для проверки: 123
Вы ввели правильный пароль

Важно: для хранения хеша и соли воспользуйтесь или файлом (CSV, JSON)
или, если вы уже знаете, как Python взаимодействует с базами данных,
воспользуйтесь базой данный sqlite, postgres и т.д.
п.с. статья на Хабре - python db-api
"""

from hashlib import pbkdf2_hmac
from binascii import hexlify

with open('salt_and_pass.txt','r') as f:
    salt_and_hash = f.readlines()

passw = input("Введите пароль: ")
salt_usr = bytes(salt_and_hash[0],'utf-8')
bpassw = bytes(passw,'utf-8')


obj = pbkdf2_hmac(hash_name='sha256',
                password = bpassw,
                salt = salt_usr,
                iterations= 10)
hash = hexlify(obj).decode()
bd = print(f'В базе данных хранится строка: {hash}')

with open('salt_and_pass.txt','w') as f:
    salt_and_hash = f.write(f'aue;{hash}')

checkpassw = input("Введите пароль для проверки: ")
bpassw = bytes(checkpassw,'utf-8')


obj = pbkdf2_hmac(hash_name='sha256',
                password = bpassw,
                salt = salt_usr,
                iterations= 10)
hash_check = hexlify(obj).decode()

if hash_check == hash:print("Пароль верный")
else:print("Пароль невереный")