# alien_0 = {'color': 'green', 'points': 5}
# alien_0 = {}  # Dictionary empty

# **Printing values from keys**
# print(alien_0['color'])
# print(alien_0['points'])

# **Adding new key-value pairs**
# print(alien_0)
# alien_0['x-position'] = 0
# alien_0['y-position'] = 25
# print(alien_0)

alien_0 = {'x-position': 0, 'y-position': 25, 'speed': 'medium'}
print(f"Original position: {alien_0['x-position']}")

# Move the alien to the right.
# Determine how far to move the alien based on its current speed
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    # This must be a fast alien
    x_increment = 3
# The new position is the old position plus the increment.
alien_0['x-position'] = alien_0['x-position'] + x_increment

print(f"New position: {alien_0['x-position']}")


# Removing key-value pairs

alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

del alien_0['points']
print(alien_0)
