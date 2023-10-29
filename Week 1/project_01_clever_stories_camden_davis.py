# This code is writen by Camden Davis for CSE110 week 1 project clever stories
# references from https://realpython.com/python-sleep/ and https://stackoverflow.com/questions/2084508/clear-terminal-in-python
# others listed as needed

# SHOWING CREATIVITY AND EXCEEDING REQUIREMENTS
# I added an intro to the beginning. I added time delay to show transtions.
# I added clearing the console to make it nice and pretty
# I added a looping function to repeat the story so you could make the story with differnt words
# I added functions in general (i remembered how to do that or the basicas from c++ class i took)


# SHOWING CREDIT FOR LEARNING MORE ON PYTHON TO MAKE THE EXCEEDING THINGS TO WORK


#  i had to look up the clear function for python from stack overflow and i implemented it here
# https://stackoverflow.com/questions/2084508/clear-terminal-in-python
# comment from opticalMagician had the clear screen effect i ustlized for this
#
# I also wanted a time delay for the Generating portion and intro so they didn all appear at once 
# I learned how the time delay worked
# by reading on about the sleep function on this website
# https://realpython.com/python-sleep/
# 
# I also wanted to add a "Yes or no"/ true false typeQuestion with the chance to enter it more than once incase the 
# user didn't anser acceptablevaule aka not yes or no for another story time or exit comepletly.
#  i found the yes no code from https://codeigo.com/python/yes-or-no-question/ it had a nice 3 step tutorial
#  with that being said that was for if else statements. i also needed to have the program restart.
# https://stackoverflow.com/questions/11459102/how-do-i-re-run-code-in-python This comment by peter cokcrom



# WHAT THE PROGRAM DOES.

#I have the main code run within my MAIN program which i define right here
# I Then made the restart portion a seperate function that gets called at the end of main,
# the restart function has the while loop runnning and checks for specfic answers on whether or not to restart
# if no valid anser is entered it gives you valid ansers you can type and then prompts you again until you type a valid answer
# if yes it calls main again and the program resarts. If no it will clear and exit

def main():

    print()
    print()
    print('Welcome to Clever Stories ')
    print()
    print()
    # time delay
    import time
    time.sleep(3) # Sleep for 3 seconds
    print('Please enter the following:')
    print()
    # information needed from user and storage ov answers
    import time
    time.sleep(1) # adding 1 second delay for effect
    adjective = input('adjective: ')
    animal = input('animal: ')
    verb1 = input('verb: ')
    exclamation = input('exclamation: ')
    verb2 = input('verb: ')
    verb3 = input('verb: ')
    # formating the story generation and another time delay.
    print()
    print()
    print('Generating your story')
    import time
    time.sleep(4) # Sleep for 4 seconds for dramaticd effect. use to b5 but that delay was too long
    
    print()
    print('Your story is:')
    print()
    print('The other day, I was really in trouble. It all started when I saw a very')
    print(adjective.lower()+' '+animal.lower()+' '+verb1.lower() + ' down the hallway.' + '"' + exclamation.capitalize() + '" I yelled. But all')
    print('I could think to do was to ' + verb2.lower() + ' over and over. Miraculously,')
    print('that caused it to stop, but not before it tried to ' + verb3.lower() )
    print('right in front of my family.')
    print()
    print()
    print()
    print('You have 20 seconds to read this story before it clears.')
    import time
    time.sleep(20)
    #attempting to add the clear terminal here  Code from the Slack website and edited to fit my needs left orginal comment in the center

    import os
    def clear():
        os.system('cls' if os.name == 'nt' else 'echo -e \\\\033c')
    clear()
    
    # This part i'm trying to read the restart vaule and have that run MAIN again
    #i've tried tis many times now. i've decided to be more simple and just not be
    # complex until we learn more.

    def restart():
    
        while True:
            restart_tf =  'Would you like to try the story again?'  
            restart_tf_a = input(f'{restart_tf} (yes or no): ')
            restart_tf_a = restart_tf_a.strip().lower()
            if restart_tf_a in ['yes', 'y']:
                print('One moement to restart')   
                import time
                time.sleep(2)
                import os
                def clear():
                    os.system('cls' if os.name == 'nt' else 'echo -e \\\\033c')
                clear()
                main()
            elif restart_tf_a in ['no', 'n']:
                import os
                def clear():
                    os.system('cls' if os.name == 'nt' else 'echo -e \\\\033c')
                clear()
                
                print('Thank you for playing. Goodbye.')
                
                import time
                time.sleep(3)
                clear()
                exit()
                   
            else: 
                print(f'You may only input yes/y/Yes or no/n/No. You anserwed {restart_tf_a} \n That is not a valid answer. Please try again.' )
    restart()
main()