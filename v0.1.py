import time
import random
iamlordvoldemort = ["thisismypasscode", "iamcoolxxx"]
# Other user's lists...

# Combining lists
user_dict = {
    "iamlordvoldy": iamlordvoldemort
    # Others ...
}


# Logging in and Signing up ...
# Maybe make database in other version ???
# * so that things don't get deleted when you stop the program
def get_In():
    global x
    x = input("> Log in or Sign up?\n")
    x = x.lower()
    if x in ["log in", "sign up"]:
        if x == "log in":
            x = input("> Please enter your username: \n").lower()
            if x in user_dict:
                y = input("> Please enter your password: \n").lower()
                if y == user_dict[x][0]:
                    return True
                else:
                    return False
            else:
                return False
        else:
            x = input("> Please enter your username: \n").lower()
            if x in user_dict:
                return False
            else:
                y = input("> Please enter your password: \n").lower()
                z = input("> Please enter your computer's name: \n").lower()
                user_dict[str(x)] = [str(y), str(z)]
                return True
    else:
        get_In()
# x is username


j = 0
while True:
    if get_In():
        while j < 100:
            print(random.randint(0, 1))
        while True:
            i = input(str(x) + '@' + str(user_dict[x][1]) + ':~$ ')
    else:
        print('There was an error processing your request.')
        time.sleep(1)
        print('Please try again.')
        time.sleep(1)
