#Simple test of if-else

cars=["bmw","honda","audi","suzuki"]

for car in cars:
    if car=="bmw":
        print(car.upper())
    else:
        print(car.title())

#numerical conditions

answer=17
if answer!=42:
    print("Incorrect answer")


"""lets check for grade of the student where:
    90-100 is A+ and is distinction
    80-90 is A and is distinction
    70-80 is B+
    60-70 is B
    50-60 is C+
    40-50 is C
    below 40 is Fail
     
    for this one we can create a list where the result of a student is stored and then 
    we will check that student's each and every subject mark 
"""
marks=[80,95,60,59,88,5,77,79]


for mark in marks:
    if mark >=90:
        print(f"A+ and scored Distinction has obtained { mark }")
    elif mark>=80 and mark <90:
         print(f"A and scored Distinction has obtained { mark }")
    elif mark>=70 and mark <80:
         print(f"B+ and  has obtained { mark }")
    elif mark>=60 and mark<70:
          print(f"B and has obtained { mark }")
    elif mark>=50 and mark <60:
          print(f"C+ and  has obtained { mark }")
    elif mark>=40 and mark<50:
          print(f"C and s has obtained { mark }")      
    else:
          print(f"Failed and has obtained { mark }")
         
if 5 in marks:  # this is for checking any item in list
    print("failed")
if 10 not in marks:
    print(f"no any number that is 10")


# if-else statement for voting criteria

age=20
if age>=18:
    print(f"Your age is valid to cast your vote")
else:
    print(f"Sorry your age is {age} and the valid age for voting is 18 or 18+")

# Multiple if-elif-else statement
age=12
if age<4:
    cost=0
elif age<18:
    cost=25
elif age<65:
    cost=30
else:
    cost= 20
print(f"your age is {age} and it cost you {cost}")


# Testing multpile conditions
requested_topping=["Mushroom","extra cheese"]

if "Mushroom" in requested_topping:
    print("Adding mushroom")
if "Chicken" in requested_topping:
    print("Adding chicken")
print("Pizza is in making process")

# If else practice: Alien color

alien_color="Green"
if alien_color=="Green":
    print (f"Player gained 5 points")

# prints the if part
alien_color="Green"
if alien_color=="Green":
    print (f"Player gained 5 points")
else:
    print(f"Player earned 10 points")

# prints the else part
alien_color="Red" 
if alien_color=="Green":
    print (f"Player gained 5 points")
else:
    print(f"Player earned 10 points")

#trying if-elif-else chain

alien_color="Green"
if alien_color=="Green":
    print(f"Player gained 5 points")
elif alien_color=="Yellow":
    print(f"Player gained 10 points")
elif alien_color=="Red":
    print(f"Player gained 15 points")

alien_color="Yellow"
if alien_color=="Green":
    print(f"Player gained 5 points")
elif alien_color=="Yellow":
    print(f"Player gained 10 points")
elif alien_color=="Red":
    print(f"Player gained 15 points")

alien_color="Red"
if alien_color=="Green":
    print(f"Player gained 5 points")
elif alien_color=="Yellow":
    print(f"Player gained 10 points")
elif alien_color=="Red":
    print(f"Player gained 15 points")

#Stage of life

age=3
if age<2:
    print(f"The person is baby")
elif age>=2 and age<4:
    print (f"The person is toodler")
elif age>=4 and age<13:
    print (f"The person is kid")
elif age>=13 and age<20:
    print (f"The person is a teenager")
elif age>=20 and age<65:
    print (f"The person is an adult")
else:
    print(f"Person is elder")

# Favourite fruits
favourite_foods=["Banana", "Apple","Jackfruit"]

if "Banana" in favourite_foods:
    print("I really like Banana")
if "Apple"in favourite_foods:
    print("I really like apple")
if "Litchi" in favourite_foods:
    print(f"I really love Litchi")


requested_toppings=["Mushroom","Green Peppers","Peporani"]

for requested_topping in requested_toppings:
    if requested_topping=="Green Peppers":
        print(f"Sorry we are out of {requested_topping}")
    else:
        print(f"Adding {requested_topping}")
print("\n Finished making Pizza")


#Checking list is not empty:

requested_toppings=[]

if requested_toppings:
    for requested_topping in requested_toppings:
        print(f"Adding {requested_topping}")
else:
    print(f"Are you sure ?")


# Trying multiple lists

Items_we_have= ["Pen","Copy","Pencil"] 
Items_customer_wants=["Pen","Books","Copy"]
#First check customer item in their list  
for Item_customer_want in Items_customer_wants:
    #Now look at our stock what we have that is in cutomer list
    if Item_customer_want in Items_we_have:
        print(f"Here is your {Item_customer_want}")
    else:
        print(f"Sorry we are out of {Item_customer_want}") 


#Assignment: Hello Admin

usernames=["Mukesh","Shreya","Ishan","Umanga","Sauharda","Aarav","Siddanta","Admin"]

for username in usernames:
    if username=="Admin":
        print(f"Hello {username} would you like to see report status")
    else:
        print(f"Hello {username} nice to see you again")


#No users
newusers=[]
if newusers:
    for newuser in newusers:
        print(f"Hello {newuser}")
else:
    print("We need to find some users")

#Checking Usernames:

Current_users=["Mukesh","Shreya","Sarita","Umanga","Sauharda","Aarav","Siddanta","Admin"]
new_Users=["Sarita","Rishi","Deepa"]
Current_users_lower=[cuser.lower() for cuser in Current_users]
for new_user in new_Users:
    if new_user.lower() in Current_users_lower:
        print("Username not available")
    else:
        print("Available")

# odinal number
numbers=list(range(1,10))
for number in numbers:
    if number==1:
        print(f"\n {number}st")
    elif number ==2:
        print(f"\n {number}nd")
    elif number==3:
        print(f"\n {number}rd")
    else:
        print(f"\n {number}th")
