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
