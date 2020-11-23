def greet_user():
    """Display a simple greeting."""
    print("Hello")


greet_user()


def describe_pet(pet_name, animal_type='dog'):
    """Display information about pet"""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name}.")


describe_pet('harry')
# describe_pet(pet_name='harry', animal_type='hamster')
