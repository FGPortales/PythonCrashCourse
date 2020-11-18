rivers = {
    'nile': 'egypt',
    'amazonas': 'peru',
    'misisipi': 'eeuu'
}

for river, country in rivers.items():
    print("The {} runs through {}".format(river.capitalize(), country.upper()))

for river in rivers.keys():
    print(river.title())

for country in rivers.values():
    print(country.title())
