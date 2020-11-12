people = ['rosa', 'beto      ', 'fátima', 'martha']

"""
print("Hola, {} te gustaría cenar en mi casa?".format(people[0].title()))
print("Hola, {} te gustaría cenar en mi casa?".format(people[1].title().
rstrip()))
print("Hola, {} te gustaría cenar en mi casa?".format(people[2].title().
lstrip()))

"""
print(people)
print("{}, no puede hacer esto. :(".format(people[2].title().lstrip()))

my_index = people.index('martha')
print(my_index)
people[my_index] = 'ana'
print(people)

print("Hola, {} te gustaría cenar en mi casa?".format(people[0].title()))
print("Hola, {} te gustaría cenar en mi casa?".format(
    people[1].title().rstrip()))
print("Hola, {} te gustaría cenar en mi casa?".format(
    people[2].title().lstrip()))
print("Hola, {} te gustaría cenar en mi casa?".format(
    people[3].title().strip()))

print('#################################################')

people.insert(0, 'Jose')
print(people)
people.insert(len(people)//2, 'Diego')
print(people)
people.append('Ocas')
print(people)

print("Hola, {} te gustaría cenar en mi casa?".format(people[0].title()))
print("Hola, {} te gustaría cenar en mi casa?".format(
    people[1].title().rstrip()))
print("Hola, {} te gustaría cenar en mi casa?".format(
    people[2].title().lstrip()))
print("Hola, {} te gustaría cenar en mi casa?".format(
    people[3].title().strip()))
print("Hola, {} te gustaría cenar en mi casa?".format(
    people[4].title().strip()))

print('#################################################')

print("Hello, {}. Sorry, I can invite only two people.".format(
    people[0].title()))
print("Hola, {}. Sorry, I can invite only two people.".format(
    people[1].title().rstrip()))
print("Hola, {}. Sorry, I can invite only two people.".format(
    people[2].title().lstrip()))
print("Hola, {}. Sorry, I can invite only two people.".format(
    people[3].title().strip()))
print("Hola, {}. Sorry, I can invite only two people.".format(
    people[4].title().strip()))
print('\n')
print(people)
rmv = people.pop()
print(people)
print('Sorry, {} :('.format(rmv))
rmv = people.pop()
print(people)
print('Sorry, {} :('.format(rmv))
rmv = people.pop()
print(people)
print('Sorry, {} :('.format(rmv))
rmv = people.pop()
print(people)
print('Sorry, {} :('.format(rmv))
rmv = people.pop()
print(people)
print('Sorry, {} :('.format(rmv))
for p in people:
    print('{} you are invited'.format(p))
