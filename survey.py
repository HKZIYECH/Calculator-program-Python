import time

name = input("What's your name?: ")
print("Hello " + name)
time.sleep(2.5)
print("Glad you're here today")
time.sleep(2.5)
print("We will be going through this python code in a while")
time.sleep(3)
print("While you wait please feel free to take our survey")
time.sleep(2)

choice = input("Do you want to take our survey?")

if choice == 'yes':
    print("Wonderful, fill the required fields below");
    time.sleep(1.5)
    namee = input("What is your name?")
    time.sleep(1.5)
    print("Hello " + namee)
    time.sleep(1.5)
    fname = input("what is your last name?")
    time.sleep(1.5)
    print("Welcome " + namee + " " + fname)
    time.sleep(1.5)
    age = input("How old are you?")
    time.sleep(1.5)
    print("Great!")
    email = input("What is your email address?")
    time.sleep(1.5)
    print("Wonderful")
    time.sleep(3)
    print("Thank you for the information, please review your information below")
    time.sleep(3.5)

    print("First Name: " + namee)
    print("Last Name: " + fname)
    print("Age: " + age)
    print("Email Address: " + email)

    time.sleep(2)
    print("Thank you for your time, have a great day")


elif choice == 'no':
    print("Okay, bye")
  

