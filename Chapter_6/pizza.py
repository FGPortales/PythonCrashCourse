# Store information about a pizza being ordered.
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese']
}
# Sumarize the order.
print(f"You ordered a {pizza['crust']}-crust pizza \
with the following toppings:")

for toppings in pizza['toppings']:
    print("\t" + toppings)
