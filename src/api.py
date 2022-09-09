import requests, json
url = "https://zipcloud.ibsnet.co.jp/api/search"
while True:
    a = input("郵便番号を入力してください:")
    break
url = url + "?zipcode={0}".format(a)
res = requests.get(url)
data = json.loads(res.content)
area = data["results"][0]
print(area["address1"] + area["address2"] + area["address3"])