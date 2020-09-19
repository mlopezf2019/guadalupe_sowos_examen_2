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

salary = [
  {
    "name": "Edgar",
    "salary": 50000.00
  },
  {
    "name": "Alan",
    "salary": 30000.00
  }
]

for i in range(len(people)):
  people[i]["salary"] = salary[i]["salary"]

print(people)