import requests

# Si quisieramos poner timepo variable lo hariamos asi:
# from_time = input("please insert from date YYYY-MM-DD: ")
# to_time = input("please insert to date  YYYY-MM-DD: ")
# url = f'https://newsapi.org/v2/everything?qInTitle=stock%20market&from={from_time}&to={to_time}&sortBy=popularity&language=en&apiKey=890603a55bfa47048e4490069ebee18c'

# r = requests.get(url)
# print(r) No nos funciona porque sale en formato JSON, en este caso

r= requests.get('https://newsapi.org/v2/everything?qInTitle=stock%20market&from=2022-09-&to=2022-10-26&sortBy=popularity&language=en&apiKey=890603a55bfa47048e4490069ebee18c')
# print(r) No nos funciona porque sale en formato JSON, en este caso error 426

content = r.json()
# print(content)
print(type(content))
print(content['articles'][0]['description'])


