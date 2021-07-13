""" 1. Посмотреть документацию к API GitHub, разобраться как вывести список репозиториев для конкретного пользователя,
 сохранить JSON-вывод в файле *.json"""

# https://docs.github.com/en/rest/guides
# https://docs.github.com/en/rest/guides/getting-started-with-the-rest-api
# https://docs.github.com/en/rest/reference/repos


import requests

username = input("Введите имя пользователя github - ")
request = requests.get('https://api.github.com/users/'+username+'/repos')
json = request.json()
print(json)

for i in range(0, len(json)):
    print("Project Number:", i+1)
    print("Project Name:", json[i]['name'])
    print("Project Owner:", json[i]['owner'])
    print("Project URL:", json[i]['svn_url'], "\n")


# Источник https://qastack.ru/programming/8713596/how-to-retrieve-the-list-of-all-github-repositories-of-a-person
