# TODO Реализовать следующую логику: получать при помощи requests данные сервиса https://jsonplaceholder.typicode.com/
# TODO (сущность можно выбрать любую, например https://jsonplaceholder.typicode.com/comments),
# TODO выводить в консоль все пары заголовки, сохранять полученный json в файл на диск

import requests
import json

url = 'https://jsonplaceholder.typicode.com/'
instance = 'posts'
f_url = url + instance

r = requests.get(f_url)
# print(r.headers)
# print(r.text)
for key, value in r.headers.items():
    print(f"{key:<35} : {value}")




# obj = json.load(r.json())


# print(r.json())


# with open('test.txt', mode='w') as f:
#     json.dump(r.json(), f)

