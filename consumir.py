import requests
try:
  resp = requests.get('https://swapi.dev/api/people/')
  if resp.status_code == 200:
    resp = resp.json()
    character = resp['results'][0]
    print("Nombre completo: " + character['name'])
    print("Genero: " + character['gender'])
    print("Naves piloteadas: ")
    for vehicle in character['vehicles']:
      vehicleData = requests.get(vehicle)
      if vehicleData.status_code == 200:
        vehicleData = vehicleData.json()
        print(vehicleData['name'])
except:
  print("No pudimos obtener los datos")

