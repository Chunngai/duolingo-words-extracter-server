import requests

url = "http://192.168.31.79:5000/run/"
data = {
    "language": "ru",
    "unit": 1,
    "skill": "Skill",
    "level": 1,
}
res = requests.post(url=url, data=data)  # data支持字典或字符串
print(res.text)
