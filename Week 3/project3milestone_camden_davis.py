# This code is writen by Camden Davis for CSE110 week 3  Adventure game.

# SO I already Wrote the adventure Game code for project before looking at this milestone.
#So I took the code from the adventure game and implemented it here to fulfill the milestone requirements
#This code will leave wondering what happens next as it will just give you the first part 
# i'll change the call to select1() which lets you pick what place youd like to start the real story at, 
# to my restart function instead.
# ALSO I WROTE A CUSTOM SLOW_TYPE function which i expalin i ndetail in the notes
# on my actaull project side. 




# Milestone Requirements
# By the middle of the week, to help make sure you are on track to finish the assignment, 
# you need to complete the following:

# The program should work correctly for the first question and possible choices, 
# and displays a follow-up response to each choice (including an else condition).

# For the milestone, you do not need to implement any additional scenarios/questions, 
# you only need the first one.
# Create a design for your complete game.

# Prepare for the rest of your game by deciding on all the possible prompts, 
# choices, and responses that the user might see. You should design the complete game, 
# including else conditions. Then, to finish up the assignment for the next lesson, 
# you'll just need to code up all of these options.
# Feel free to write this design out on paper or in a document (Word, Google Docs, Powerpoint, etc.),
# whatever is most convenient for you. You should write each possible scenario along with its choices. 
# Then, for each choice, write the resulting scenario with its choices, etc.
# You are not required to submit this design to I-Learn, but you should complete 
# it as part of your Milestone to make sure you are prepared to finish the program.

import os
import time
import sys
def main():
    title()
    intro()
def slow_type(text_output):
    for letter in text_output:
        print (letter, end="", flush=True)
        time.sleep(0.045)
# I don't use this one as much as i saw it worked but as it typed it out, i need the part where the answers just apeared to signify i need imout from you
def type_with_input(prompt):
    slow_type(prompt)
    return input()    
def title():
    print()
    print()
    print()
    slow_type("Camden Proudly Presents\n")
    # time delay for dramatic entrance
    time.sleep(2) # Sleep for 3 seconds
    slow_type('Hours and hours of hurting his brain\n')
    time.sleep(1)
    slow_type('To bring you\n')
    time.sleep(1)
    slow_type('...\n')
    time.sleep(1)
    slow_type('The adventure, you hope it is.\n')
    time.sleep(3)
    #this function will be called alot to clear the terminal to keep things nice and tighty.
    clear_screen()         
def intro():
    #Gathering the information
    player_name = type_with_input('What is your first name? \n')
    # This part will intoduce the concept of making choices. This will be a simple one that 
    # basically explain the idea no matter the choice
    # this also should cause the player to ease up and get them hooked into the story.
    #i try to be funny idk if it works but whatever.
    slow_type(f'Hello {player_name.capitalize()}. This will be...')
    print('\n\n\n\n\n') #6 spaces
    time.sleep(1.4)
    slow_type('Well an adventure of course!\n') #if iput this at he end i just want spacing to be there in fewer print statements
    time.sleep(1)
    slow_type('What else would this be?\n\n') #adding a space by \n at the end.
    time.sleep(2)
    slow_type('Before we begin this adventure, we need to set some ground rules.\n')
    slow_type('You will be placed into this story. After I finish typing what your\n')
    slow_type('scenario or scene is, I the Narrator will present to you a few choices.\n')
    slow_type('Your choices will be displayed seperated from story and in ALL CAPS\n')
    slow_type('See this for example.\n')
    slow_type('blah blah blah blah blah blah a cow jumped. blah blah blah\n')
    slow_type('when the cops showed up blah blah blah blah\n')
    slow_type('and then they asked you to freeze.\n')
    print()
    slow_type('Please type one of the following:\n')
    print('         RUN         FREEZE          BLAME')
    time.sleep(4)
    slow_type("I'm actually asking you the first question now.\n")
    slow_type(f'{player_name.capitalize()} Please choose one of those bold words above so we can see what adventure awaits!\n')
    intro_c1 =input().strip().lower()
    intro_ans1 = 'no_answer'
    while (intro_ans1 == 'no_answer'):
        if (intro_c1 == 'run'):
            slow_type('Run. Really? Well alright\n')
            slow_type("Honestly I just gave you the illusion of choice. All the choices in this case lead to\n")
            slow_type('the real game. Thats it the Tutorial is over.\n')
            time.sleep(1)
            slow_type('Well now that you undertand the concept of how this will play out, lets proceed to the real adventure!\n')
            time.sleep(3)
            intro_ans1 = 'answererd'
            clear_screen()
            #select1()
            restart()
        elif(intro_c1 == 'freeze'):
            slow_type('Freeze? The cow jump and cops showed up. Really? whatever your story...')
            slow_type("Honestly I just gave you the illusion of choice. All the choices in this case lead to\n")
            slow_type('the real game. Thats it the Tutorial is over. \n')
            slow_type('Well now that you undertand the concept of how this will play out, lets proceed to the real adventure!\n')
            time.sleep(3)
            intro_ans1 = 'answererd'
            clear_screen()
            #select1()
            restart()
        elif(intro_c1 == 'blame'):
            slow_type('Thats right DENY DENY DENY you blame that cow.\n')
            slow_type("Honestly I just gave you the illusion of choice. All the choices in this case lead to\n")
            slow_type('the real game. Thats it the Tutorial is over. \n')
            slow_type('Well now that you undertand the concept of how this will play out, lets proceed to the real adventure!\n')
            time.sleep(3)
            intro_ans1 = 'answererd'
            clear_screen()
            #select1()
            restart()
        else:
            print("That is not an acceptable answer! heck I'm even typing slow for you to read.")
            print('I know this is not typing slow but you had 1 job...')
            print('PLEASE CHOOSE 1 of the following: "RUN" FREEZE" "BLAME"')
            intro_c1 = input().strip().lower()
def clear_screen():
        os.system('cls' if os.name == 'nt' else 'echo -e \\\\033c')
def restart():
    #this uses boolean logic.   Iknow i can call the clear_sreen() function
    # but i wanted to look at nesting thee function with in a function, which main can't see so made i 
    # clear() inside of restart, which is the same as clear_screen()
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
if __name__ == '__main__':
     main()     

