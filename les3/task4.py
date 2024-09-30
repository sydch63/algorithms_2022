"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница или нет
есть ли в кэше соответствующая страница или нет

Пример кэша: {'url-адрес': 'хеш url-а'; 'url-адрес': 'хеш url-а'; ...}

Если страница в кэше есть, просто вернуть значение хеша, например, 'хеш url-а'
Если страницы в кэше нет, то вычислить хеш и записать в кэш

Подсказка: задачу решите обязательно с применением 'соленого' хеширования
и одного из алгоритмов, например, sha512
Можете усложнить задачу, реализовав ее через ООП
"""

import hashlib
from uuid import uuid4

dct_hash  = {}

def hash_url(url):
    if dct_hash.get(url) == None:
        dct_hash.update({url:hashlib.sha256(uuid4().hex.encode() + url.encode()).hexdigest()})
    else:
        print(dct_hash.get(url))

hash_url('https://vk.com')
hash_url('https://ru.dotabuff.com/heroes/meta')
hash_url('https://apps.db.ripe.net/db-web-ui/query?bflag=false&dflag=false&rflag=true&searchtext=AS15159&source=RIPE')
hash_url('https://qna.habr.com/q/1372344')
hash_url('https://bgp.tools/prefix/94.25.30.0/24#asinfo')
hash_url('https://vk.com')
