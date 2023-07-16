import requests

url = 'http://localhost:5000/predict_api'
r = requests.post(url,json={'Sepal_Length':2.1, 'Sepal_Width':1.2, 'Petal_Length':4.8, 'Petal_Width':5.2})

print(r.json())