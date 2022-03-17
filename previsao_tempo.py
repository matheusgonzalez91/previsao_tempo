import requests

city_name = str(input('Digite o nome da sua cidade: '))

api_key = 'fa9627882538b4ef55efe3ee6af6e668'
link_api = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&lang=pt_br'

r = requests.get(link_api)
r_dic = r.json()
desc = r_dic['weather'][0]['description']
temp = r_dic['main']['temp'] - 273.15

print(f'Description: {desc}')
print(f'Temperatura: {temp} C')