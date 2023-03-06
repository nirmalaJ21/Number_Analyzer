#Number Analyzer code
print("*" * 50)                         # Print * 50 times
welcome_str = '\tWelcome to number analyzer'  # Print Welcome to number analyzer
print(welcome_str.upper())              # Here string is converted to upper case using upper function
print("*" * 50)
user_num = 0                            # variable  to store user provided number to
while True:                             # While  loop continues till the time user proving invalid name ,condition remain true
    user_name = input('\t \nPlease enter you name').capitalize()  # input User's name  First character is capitalized using  capitalized function
    if user_name.isalpha() != True:   # Using isalpha function checking if  not user's name is all character
        print("\t\n Please enter valid name")
    else:                               # If user name is valid break out of the loop to continue further with code execution
        break
while True:                             #While loop to contuinue till the time  user  enter 'y' to contiune some more time
        while True:                     # While  loop continues till the time user proving invalid number negative or grater then 100 ,condition remain true
           print("\nWelcome {} ,please enter any number between 1 - 100".format(user_name).title())
           user_num = int(input())      #Ask for the  number
           if int(user_num) <= 0 or int(user_num) >100:  # checking condition for negative and number greater than 100)
                print("\t\n Please enter a valid positive  number in the range 1 -100")   #print valid message and set while loop condition to false, it will ask for valid number again
                continue         # continue to  check for valid input
           else:
                break            # if number is in the range of 1 to 100  continue with rest of the code

        def is_odd(user_num):                   # function to check if number is odd or even
              if user_num % 2 != 0:               # Math operator % to check reminder , if 0  (even) return false else true (odd)
                return True
              else:
                return False
        if is_odd(user_num) == True and user_num < 60:                      #if condition to check  odd number(function call) less than 60 and is_odd return true
                    print('\t The number {} is odd and less than 60'.format(user_num))
        elif is_odd(user_num) == False and user_num >= 2 and user_num <= 24:  #if condition to check even number >= 2  and < =24
                    print('\t The number {} is Even and less than 25'.format(user_num))
        elif is_odd(user_num) == False and user_num >= 26 and user_num <= 60: #if condition to check even number >= 26  and < =60
                    print('\t The number {} is Even and between 26 and 60 inclusive.'.format(user_num))
        elif is_odd(user_num) == False and user_num > 60:                      #if condition to check even number > 60
                    print('\t The number {} is even and grater than  60'.format(user_num))
        else:                                                                   # rest all odd number >= 60 will be part of this else statement
                    print('\t The number {} is odd and grater than 60'.format(user_num))
        loop_more = input(f" \n Would like to  continue y/n")                           #Ask user to continue and based on the choice break out of the loop or continue further to ask for next number check
        if loop_more == 'n':
            print("\033[5m " + 'Thanks!' + "\033[5m ")
            break                                                                       # Out of the  while loop,Exit the loop

        elif loop_more =='y':
            continue                                                                    # Continue with the next choice of number
        else :
             print ('Opp!, Please enter valid choice ''y'' or ''n''')


