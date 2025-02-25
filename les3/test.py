import hashlib

dict_url = {}
salt = '1452yfdh789'


def cache_url(url):
    if url in dict_url.keys():
        print(f'хеш {url} - {dict_url[url]}')
    else:
        dict_url[url] = hashlib.sha512(salt.encode() + url.encode()).hexdigest()
        print(dict_url)


cache_url('https://netflix.com')
cache_url('https://netflix.com')
cache_url('https://www.kinopoisk.ru')
cache_url('https://www.kinopoisk.ru')