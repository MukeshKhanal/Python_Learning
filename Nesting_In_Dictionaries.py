# list of dictionaries
alien_0={
    'color':'green',
    'points':10
}
alien_1={
    'color':'green',
    'points':10
}
alien_2={
    'color':'green',
    'points':10
}

aliens=[alien_0,alien_1,alien_2] #storing all dictionaries inside a list
print(aliens)
for alien in aliens:
    print(alien)

# creating more aliens using  range

# creating empty list

aliens=[]

for alien_number in range(30):
    new_alien= {'color':'green', 'points':5}
    aliens.append(new_alien)

# showing first 5 aliens

# for alien in aliens[:5]: #shows from 0 to 4th item of list (0,1,2,3,4):total 5
#     print(alien)

# # counting how many are there using len()

# print(f"There are {len(aliens)} aliens")


# lets try to modify first three aliens using if statement

for alien in aliens[:3]:
    if alien['color']=='green':
        alien ['color']='red'
        alien ['points']=10
    
# showing 5 aliens

for alien in aliens[:5]:
    print(alien)



# List in a dictionary

# Store the informationa bout pizza

pizza={
    'crust':'thick',
    'toppings':['mushroom','extra-cheese']
}

# summarizing order
print(f"You have ordered {pizza['crust']}-- crust pizza with following toppings:")

for topping in pizza['toppings']:
    print(topping)

List and dictionaries looping

favourite_languages={
    'Mukesh':['Python','C#'],
    'Ishan':['Python','C'],
    'Shreya':['Java'],
    'Anjan':['Javascript']
}

# looping in dictionary
for name, languages in favourite_languages.items():
    if len(languages)==1: #this looks if the person has the single fav language or has more languages
        print(f" {name.title()}'s favorite language is ") 
    else:
        print(f"The name of the person is {name.title() } and their favourite languages are ;")
    # looping in list
    for language in languages: #targeted the langauges from the dict loop where languages indicates the value which is storing list
        print(language.title())


# dictionary inside dictionary

users= {
    'Mukesh':{ #key user
        'first':'Mukesh', #values
        'last':'Khanal',
        'email':'mkhanal.com'
    },

    'Shreya':{
        'first':'Shreya',
        'last':'Pandey',
        'email':'Spandey.com'
    }

}
for user, user_info in users.items():
    print(user.title())
    First= user_info['email']
    print(First)

