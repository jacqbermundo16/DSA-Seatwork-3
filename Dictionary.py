#Write a python program for contact tracing:

#- Display a menu of options
#	Menu:
#		 1 -> Add an item
#		 2 -> Search
#		 3 -> Exit (y/n)
#- Allow user to select item in the menu (check if valid)
#- Perform the selected option
#		- Option 1: Ask personal data for contact tracing (Listed are sample only, add more)
#				   Use dictionary to store the info
#				   Use the full name as key
#				   The value is another dictionary of personal information
#		- Option 2: Search, ask full name then display the record
#		- Option 3: Ask the user if want to exit or retry.

#Note: 
#- Your program should be uploaded to github before 4pm
#- Record a demo presenting your program
#- Send the demo or link of demo directly to my messenger

#Example Output:

#Menu:
# 1 -> Add an item
# 2 -> Search
# 3 -> Exit (y/n)

#What do you want to do? (1-3): 1
#Full name: Danilo Madrigalejos
#Age: 30
#Address: Eastwood
#Phone number: 1234567890
#Saved!
#What do you want to do? (1-3): 2
#Full name: Danilo Madrigalejos
#Age: 30
#Address: Eastwood
#Phone number: 1234567890 What do you want to do? (1-3): 3
#Exit? n

#  STEPS
# 1. display an instruction or give a brief explanation about the program (state the purpose)  
#    give an example
# 2. display the menu list
# 3. Ask the user to choose between the provided menu
# 4. create the code for each menu option
#   4.1 OPTION 1 - ASK FOR PERSONAL INFO
#       4.1.1 create a null dictionary with a key "full name"
        #    3.1. create another null dictionary (sample only to check if the code will work, delete this after if the code works so that
        #         the program will not result to syntax error)
        #         the null dictionary be named "personal info" then the program will ask the user to input their personal info
        #    3.2  after getting the info, save it to the "personal info" dictionary
        #    3.3  append the dictionary to be the value of the "full name" key in the first program
        # 4. create another null dictionary that will store the user's input

#   4.2 OPTION 2 - SEARCH

# 5. make the options a loop until the user inputs 'n'



# Start
# 1. display an instruction or give a brief explanation about the program (state the purpose)  
print("\nGood day, we'll be asking you to input personal information for the sake of contact tracing. We value the data privacy so your data will be safe with us. Thank you for your cooperation.\n")

# 2. display the menu list
print("==========MENU==========")
print('1 ---> Add an item')
print('2 ---> Search')
print('3 ---> Exit (y/n)')
print('========================')
print ()

# 3. Ask the user to choose between the provided menu
def menu ():
    askInput = int(input('What do you want to do? (1-3): '))
    num = askInput

    if num == 1:
        print("Option 1")

    elif num == 2:
        print("Option 2")

    elif num == 3:
        print('Option 3')

menu()    
