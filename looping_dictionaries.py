favourite_languages={
    'mukesh':'Js',
    'ishan':'python',
    'anjan':'Java',
    'pronab':'Java'
}

for name,language in favourite_languages.items():
    print(f" Name: {name}  \n Langague: {language}")


for name in favourite_languages.keys():
    print(name)

friends=["Mukesh","Shreya"]
for name in favourite_languages.keys():
    print(f"Hi {name}")
    
    if name in friends:
        language= favourite_languages[name].title()
        print(f" I see {name} you like {language}")
    
if 'ishan' not in favourite_languages.keys():
    print(f" vai please be in pool")
else:
    print("hi")


for name in sorted(favourite_languages.keys()):
    print(f" {name.title()}")

for value in favourite_languages.values():
    print(value)
for value in set(favourite_languages.values()):
    print(value)

#Sets are like didctionaries  but without key and value pair when we print them they remove the duplicate values
names={'mukesh','mukesh','hari'}
print(sorted(names)) 


# # glossary part 2 using loop to iterate the words and meaning 
words_meaning={
    'variables':'things that can be changed',
    'Lists':'it stores data',
    'Tuples':'immutable list'
}

for k,v in words_meaning.items(): #use items() to show all the key value pairs
    print(f"word: \n{k}\nMeaning:\n{v} ")


# River and its country

rivers={
    'Koshi':'Nepal',
    'Nile':'Egypt',
    'Amazon':'Brazil'
}
# To print river and its value
for river,country in rivers.items():
    print(f"The {river} runs through {country}")
    
# To print the rivers only
for river in rivers.keys():
    print(river)
# To print name of countries only
for country in rivers.values():
    print(country)
    
    
# Polling of favourite language
favourite_language={
    'Mukesh':'C#',
    'Shreya':'Python',
    'Aarav':'Js',
    'Siddhanta':'Java',
    'Sauharda':'Ruby'
}

people=['Ishan','Mukesh','Shreya','Sajjan']

for name in favourite_language.keys():
    print(f"Hi! {name}")
    if name in people:
        print(f"Thank you {name} for taking part in poll.")
for person in people:
    if person not in favourite_language.keys():
        print(f"Please {person} take part in poll")
