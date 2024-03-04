import json

data = '{"firstName" : "Engin", "lastName" : "demiroğ"  }'

y = json.loads(data)

print(type(y))


customer = {
    "name" : "ali",
    "mail" : "rajmet42tr@gmail.com"
 }


customerjson = json.dumps(customer)


print(customer["name"])