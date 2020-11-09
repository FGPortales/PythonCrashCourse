# motorcycles = ['honda', 'yanaha', 'suzuki', 'ducati', 'suzuki']
# print(motorcycles)

"""using the del statement"""
# del motorcycles[0]
# print(motorcycles)

"""_using pop statement_"""
# popped_motorcycle = motorcycles.pop()
# print(motorcycles)
# print(popped_motorcycle)

# too_expensive = 'ducati'
# motorcycles.remove(too_expensive)
# print(motorcycles)

"""using sort() and sorted() method"""

cars = ['bmw', 'toyota', 'subaru', 'audi']
# sort() -> permanently
# cars.sort()
# print(cars)
# cars.sort(reverse=True)
# print(cars)
# sorted() -> temporarily
print('#\n')
print(cars)
a = sorted(cars)
a.reverse()

print(a)

# l = [3,4,5,6,1,2]
# l.reverse()
# print(l)
