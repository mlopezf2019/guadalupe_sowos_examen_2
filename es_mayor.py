people = [
  {
    "name": "Edgar",
    "age": 31
  },
  {
    "name": "Alan",
    "age": 18
  }
]

def es_mayor(persona): 
  return persona and persona['age'] >= 18

print(list(filter(es_mayor, people)))

    