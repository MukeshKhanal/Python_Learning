# Simple Dictionary
alien_0={'color':'green', 'points':5}
print(alien_0['color'])

new_color= alien_0['color']

print(f"You love {new_color} nah!!")

# Adding new key-value pairs

alien_0['X-Coordinate']=0
alien_0['Y-Coordinate']=25
print(alien_0)

# Starting with empty dictionaries
alien_1={}
alien_1["color"]="red"
# better to use same style of quote dont mix it
print(alien_1)

# modifying the dictionaries

print(f"The color was {alien_1['color']}")
alien_1['color']='yellow'
print(f"The color now {alien_1['color']}")



alien_1={'color':'red','speed':'slow'}
print(alien_1)
if alien_1['speed']=='slow':
    alien_1['color']='blue'
elif alien_1['speed']=='fast':
     alien_1['color']='Brown'

print(alien_1)
alien_1['speed']='slow'
print(alien_1)


alien_0={'x-position':0, 'y-position':25, 'speed':'medium'}
print(f"Original position: {alien_0['x-position']}")
alien_0['speed']='fast'

# Move the alien to the right
# Determine how far to move the alien based on its current speed.
if alien_0['speed']=='slow':
    x_increment=1
elif alien_0['speed']=='medium':
    x_increment=2
else:
    x_increment=3

# the new position is the old position plus the increment
alien_0['x-position']=alien_0['x-position']+x_increment


print(f"New position: {alien_0['x-position']}")

# Removing key-value pairs
alien_0={'color':'green', 'points':5}
print(alien_0)


del alien_0['points']
print(alien_0)

# Creating large dictionary

favourite_language={
    'Mukesh':'Python',
    'Ishan': 'Python',
    'Anjan': 'Javascript',
    'Shreya':'C#'
}
language= favourite_language['Mukesh']

print(f"The faviourite language of Mukesh is {language}")

print(favourite_language['Anjan'])


# using get() to access
# print(favourite_language['Shreya'])

language_value= favourite_language.get('Shreya','No language specified')
print(language_value)

# Assignment:Data of person
person={
    'First_name':'Mukesh',
    'Last_name':'Khanal',
    'Age':24,
    'City':'Thunder Bay'
}
print(person['First_name'])
print(person['Last_name'])
print(person['Age'])
print(person['City'])

# Assignment 2: Favourite numbers
favourite_numbers={
    'Mukesh':10,
    'Shreya':19,
    'Messi':30,
    'Ronaldo':7,
    'Neymar':11

}
print(f"Favourite number of Messi is {favourite_numbers['Messi']}")

# Assignment 3: Glossary:
words_meaning={
    'variables':'things that can be changed',
    'Lists':'it stores data',
    'Tuples':'immutable list'
}

print(f"Variable: {words_meaning['variables']}")