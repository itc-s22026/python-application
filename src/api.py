from curses.ascii import TAB
import requests, json
while True:
        name = input('ポケモンの名前を入力してください。:')
        uri = f'https://pokeapi.co/api/v2/pokemon/{name}/'
        res = requests.get(uri)
        an = json.loads(res.content)
        print(an['abilities'][0]['ability']['name'])
        #print(an['abilities'][0]['ability']['url'])
        print(an['abilities'][1]['ability']['name'])
        #print(an['abilities'][1]['ability']['url'])
        if (res := input('他のポケモンも調べますか？ y/n') != 'y'):
                break
