def make_pizza(size, *toppings):
    print("Size: {}".format(size))
    for topping in toppings:
        print(topping)


make_pizza(3, 'a', 'c', 'd')
