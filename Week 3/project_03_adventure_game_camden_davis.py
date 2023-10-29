# This code is writen by Camden Davis for CSE110 week 3 Adventure Game
# I have listed sources as i first learned them for the first two weeks projects, and where I went to learn new things for this project.
# I have spent time trying to learn some more advanced concepts, and rely on knowlege/ logic from my c++ classes i took a few years back
# i have group serveral comments to gether with the # all being one connected thought.

#PLEASE  SEE THE NOTES HERE
"""_summary_    #PLEASE  SEE THE NOTES HERE
 
#                                    SHOWING CREATIVITY AND EXCEEDING REQUIREMENTS AND SOURCES
# 
#
# I added functions in general (I remembered how to do that or the basicas from c++ class i took)
# SHOWING CREDIT FOR LEARNING MORE ON PYTHON TO MAKE THE EXCEEDING THINGS TO WORK 
#
# SOURCES THAT I LEARNED STUFF ON WEEK ONE and two but will drop links just in case at this point.
# I've given credit as needed every time. don't want to get in trouble.
# not sure when its not neccisary to do these as 've learned them already.
#
#  I had to look up the clear terminal for python
# https://stackoverflow.com/questions/2084508/clear-terminal-in-python
#
# I also wanted a time delay 
# https://realpython.com/python-sleep/
# i've learned and used this in every project for animation efffect or a natural pause feel.
#
#  Week 3 and 4 combined lessons go over if statements and Loops. but heres the first way i learned it.
# I've Since gone through the lessons on week 3 and 4 to solidify this. however if needed i will provide the link
#intital find in week 1 https://stackoverflow.com/questions/11459102/how-do-i-re-run-code-in-python and
# https://codeigo.com/python/yes-or-no-question/ 
#
#
# In an intrest to try and make neat code but also effcient code, ai weant to make sure i understand pythons 
# nomenclature a bit better.  i know in C++ you had you're main function, and you could call other functions into
# main that were seperate and could be used in serveral places.
# 1  https://stackoverflow.com/questions/26490096/do-i-have-to-have-main-function-in-my-python-code
# 2  https://stackoverflow.com/questions/25069359/should-i-define-functions-inside-or-outside-of-main
# 3  https://stackoverflow.com/questions/49286011/can-you-return-a-value-from-a-main-function-in-python

# This question helped me undertand that the understanding comes from these 3 sources.
#
# Yes, you can have functions outside of main in Python                                               (Source 1)
# Writing separate files without a main function, to be imported into other programs,
# is the normal and correct way of doing Python programming                                           (Source 1)
# However, functions defined inside main() cannot be imported elsewhere                               (source 2) 
# It is also possible to return a dictionary (or list, or tuple, or whatever) in utility.main() 
# and then grab all the dictionaries and store them in a list in rollup.main()                        (Source 3)
#
# I do not know what utility.main() is yet but i'm sure i'll figure it out soon enough 
# lists is on week 5 things
#
# https://stackoverflow.com/questions/18794873/should-function-be-defined-before-it-is-used-in-python
#
# This one cleared things up a bit.
#
#    # def main():
#    #     dog()
#
#    # def dog():
#    #     print("This is a dog.")
#
#    # if __name__ == '__main__':
#    #     main()
#    
#    # the dog() is defined after it is called?
#    
#   Actually it's not (defined after it's called). This script will do the following:
#
#  create function and assign it to "main"
#  create function and assign it to "dog"
#  call "main"
#  At that point dog is already known in global scope and main can call it.
#  gunna try that




#                                              WHAT THE PROGRAM DOES.
#
#
#
# I have the main code run within my MAIN program which keeps the game orgonized. i'll put a few functions before main as need before 
# and after main will be the different scenes and the restart game function.
#
# the program will then ask a choice and call a function. I will make each level or scene a seperate function.
# the program will then be able to bounce around to different scnarios based on if thens, and what functions get called
# main also clalls the function clear a few times to clear the screen to make it nice and pretty.
#
#  There is a restart game function that gets called at the end of main, and this is simply to play again.
# the restart function has the while loop runnning and checks for specfic answers on whether or not to restart
# if no valid anser is entered it gives you valid ansers you can type and then prompts you again until you type a valid answer
# if yes it calls main again and the program resarts. If no it will clear and exit




#                            THIS IS SUPER DUPER IMPORTANT TO UNDERSTAND
#
#
#
#
#
# I wanted to make a  to learn how to make a typing effect on the screen like it was being told to you versus just having 
# it all appear immediately.
# https://stackoverflow.com/questions/4099422/printing-slowly-simulate-typing helped me learn this particular thing.
#
# heres my attempt to make it work based of reading here. 
# 
# This opened a car of worms and yeah there was somones solution ther but how did it work? so i started researching and
# asking questions about how python itself was working. It got pretty hard to understand but i was able to learn some basics relating
# to my question still so i could try to write code to do my animation effect for the story. 
# 
# there are two ways this works. I learned that the print() we've been using in class in python 3
# was actually a function that was just built in. With that being said you can make your own print function.
# sources below helped tramendously. Litterally every comment was a gold mine of information.
# https://docs.python.org/3/library/functions.html#print and https://stackoverflow.com/questions/3263672/the-difference-between-sys-stdout-write-and-print 
# This helped me understand what print() actually does.
#
#       the highlight being  a comment by dogbane on stackoverflow as listed above ^
#
# "
# print first converts the object to a string (if it is not already a string). It will also put a space before the object
# if it is not the start of a line and a newline character at the end.
# When using stdout, you need to convert the object to a string yourself (by calling "str", for example) and there is no newline character. 
# so for example
# print 99
# is equivalent to:
#
# import sys
# sys.stdout.write(str(99) + '\n')
# "
#
# I was then able to understand how to make a couple animation effects using sys.stdout   but i had to be mindfull to put new lines otherwise
# it all jumbled up while i was learning. There is probably and easier or more effcient way to do this but this was what i was able to come up with.
# i also learned that using  sys.stdout you could make a progress bar  
# A comment by Carlos on that same page of stack overflow. 
# (told you it was a gold mine of information)
# 
# "There's at least one situation in which you want sys.stdout instead of print.
#
# When you want to overwrite a line without going to the next line, for instance while drawing a progress bar or a status message,
# you need to loop over something like
#
# Note carriage return-> "\rMy Status Message: %s" % progress
#
# And since print adds a newline, you are better off using sys.stdout. 
#"
#
# This made me want to also try to make a loading screen. If implement it, I was inspired by that comment.
#
# I Fought this for a really long time which brought me back to 
# https://stackoverflow.com/questions/4627033/how-to-print-a-string-with-a-little-delay-between-the-chars
# Comment from Gino Mempin said i could use print(char, end="", flush=True) forthe exmaple by steven rumbalski
# Stevens code said this
# text = "Hello, this is a test text to see if all works fine."
# for char in text:
#     sys.stdout.write(char)
#     time.sleep(0.2)
# so ultimatley you write it like 
#
# import time
# text = "Hello, this is a test text to see if all works fine."
# for char in text:
#     print (char, end="", flush=True)
#     time.sleep(0.2)
#
#This makes it so i canuse python 3 and not make my brain hurt as much as i'm now hours into this.
#
#
#
# Listing this function now as i want to Start main with it and i get having a problem when it was at the end of main.
# listing it first to just make it work.
#
#
# learned about lists.
#
#https://stackoverflow.com/questions/67065972/building-a-simple-text-based-game
# this talked about different rooms. i might try and implement that too.
    Returns:
        _type_: _description_
    """

import os
import time
import sys

def main():   #The Main Program. Its actually really small.
    title()
    intro() # intro gets player name and explains what happens
    tutorial() # this function runs an example. At this point this function will begin to run the rest of the story.
    # No MORE are called from main.         as it will call selcet funtion and from there the diferent functions will give you the story.

def slow_type(text_output):   # Custom Print function to write as if someone is typeing.
    for letter in text_output:
        print (letter, end="", flush=True)
        time.sleep(0.04)

# def type_with_input function notes         
# I don't use this one I did test it and verfied it worked but during the trial and error period, 
# i saw it worked but as it typed it out, but it dragged on too much. need to change things up
# i need the part where the answers just apeared to signify i need input from you i kept it just incase i might use it later

#Scenarios that follow an earlier answer should be handled with nested if statements.
# In other words, the body/block of the first if statement will contain a print statement and then another if statement inside it.

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
    slow_type('A RANDOM STORY.\n')
    time.sleep(5)
    clear_screen()
       
def intro():
    #Gathering the information   i make the player name variable global so i can call
    # it and use the name through out the story
    global player_name
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
        
def tutorial():    # this has my nested if statment if you select freeze.
    slow_type(f'See this for example {player_name.capitalize()}.\n')
    slow_type('blah blah blah blah blah blah a cow jumped. blah blah blah\n')
    slow_type('when the cops showed up blah blah blah blah\n')
    slow_type('and then they asked you to freeze.\n')
    print()
    slow_type('Please type one of the following:\n')
    print('         RUN         FREEZE          BLAME')
    time.sleep(2)
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
            select1()
        elif(intro_c1 == 'freeze'):
            slow_type('Freeze? The cow jump and cops showed up. Really? whatever your story...')
            print()
            print()
            #obligation to instruction two to have a nexted if statement.
            #Scenarios that follow an earlier answer should be handled with nested if statements.
            # In other words, the body/block of the first if statement will contain a print statement 
            # and then another if statement inside it.
            slow_type("I'm goin to add another question here to fufil my obligation to section 2 of the instructions.\n")
            time.sleep(3)
            print('Why did you devide to freeze?')
            print('    IDK     BECAUSE')
            nested_if =input().strip().lower()
            if(nested_if == 'idk'):
                print('That was not smart oh well ')
                time.sleep(3)
            
            elif(nested_if == 'because'):
                print('fair enough')
                time.sleep(3)     
            else:
                print("That is not an acceptable answer! .")
                print('Please Type one of the following answers: ')
                print('IDK or BECAUSE')
                nested_if =input().strip().lower()
            slow_type("Honestly I just gave you the illusion of choice. All the choices in this case lead to\n")
            slow_type('the real game. Thats it the Tutorial is over. \n')
            slow_type('Well now that you undertand the concept of how this will play out, lets proceed to the real adventure!\n')
            time.sleep(3)
            intro_ans1 = 'answererd'
            clear_screen()
            select1()
        elif(intro_c1 == 'blame'):
            slow_type('Thats right DENY DENY DENY you blame that cow.\n')
            slow_type("Honestly I just gave you the illusion of choice. All the choices in this case lead to\n")
            slow_type('the real game. Thats it the Tutorial is over. \n')
            slow_type('Well now that you undertand the concept of how this will play out, lets proceed to the real adventure!\n')
            time.sleep(3)
            intro_ans1 = 'answererd'
            clear_screen()
            select1()
        else:
            print("That is not an acceptable answer! heck I'm even typing slow for you to read.")
            print('I know this is not typing slow but you had 1 job...')
            print('PLEASE CHOOSE 1 of the following: "RUN" FREEZE" "BLAME"')
            intro_c1 = input().strip().lower()

def select1():  # this chooses the story start location isn't really to different.
    slow_type(f'Where do you want to begine the story at {player_name.capitalize()}?\n')
    print()
    slow_type('Please type one of the following\n')
    print('     BEDROOM          KITCHEN')
    select1_c1 = input().strip().lower()
    #select1_c1 = select1_c1.strip().lower()
    select1_ans1 = 'no_answer'
    while (select1_ans1 == 'no_answer'):
        if (select1_c1 == 'bedroom'):
            slow_type("You've chosen to start in your bedroom.\n")
            print("One moment to generate you're Story")
            time.sleep(4)
            select1_ans1 = 'answered'
            clear_screen()
            scene1_choice_1()
        elif(select1_c1 == 'kitchen'):
            slow_type("You've chosen to start in your kitchen.\n")
            print("One moment to generate you're Story")
            time.sleep(4)
            select1_ans1 = 'answered'
            clear_screen()
            scene1_choice_2()
        else:
            print("That is not an acceptable answer! .")
            print('Please Type one of the following answers: BEDROOM  or KITCHEN')
            select1_c1 = input().strip().lower()       
                
def scene1_choice_1():  #bedroom start
    slow_type('You find yourself sitting in your bedroom. You are about to get up and finish getting ready for bed\n')
    slow_type('when you start to feel a bit uneasy. The uneasy feeling is coming from downstairs.\n')
    slow_type('You begin to wonder if your are just finally feeling the stress of the day catching up to you\n')
    slow_type('or if something might actually be wrong.\n')
    slow_type('You think should I "Stay," or should I figure out where its coming from. It probably the "kitchen."\n')
    slow_type('Please type one of the following actions:\n')
    print('     STAY          KITCHEN')
    scene1_ans1_choice_1_tf = 'no_answer'
    scene1_ans1_choice_1 = input().strip().lower()
    while (scene1_ans1_choice_1_tf == 'no_answer'):
        if(scene1_ans1_choice_1 == 'stay'):
            slow_type('You decided to stay, and just sleep it off. You reason to youself that it is just a\n')
            slow_type('long day of work finally catching up to you. As you finish getting ready for bed the power cuts off\n')
            slow_type('"Oh no" you start to panic. In the dark a glowing mist comes from under the door.\n')
            slow_type('The door suddenly gets ripped of the frame and a giant lizzard comes in.\n')
            slow_type('You start to scream!\n')
            slow_type('The lizard screams back...\n')
            time.sleep(4)
            scene1_ans1_choice_1_tf = 'answered'
            clear_screen()
            dead_story1()
        elif(scene1_ans1_choice_1 == 'kitchen'):
            slow_type('You decided that its probably in your best interest to figure out what is going on downstair,\n')
            slow_type('if only for you own sake. You open the door and start down the stairs when out of no where you hear\n')
            slow_type('"Finally! I have been waitng for you to come help me." in a aggresive yet somewhat purring voice.\n')
            slow_type('You jump as you live alone. "Who could have possibly said that?" you say as you start looking frantically\n')
            slow_type('for the mysterious voice. Suddenly a... . a cat? but like a 30lbs cat thats like the size of dog is just\n')
            slow_type('sitting in your kitchen. "I am sir Dingspitz Gloombottom and I have been sent to warn you of danger."\n')
            slow_type('Your brain locks up as its trying to comprehend what in the what is happening.\n')
            slow_type('"uhh hi." you finally manage. "I have some questions"\n')
            slow_type('"First, how are you talking? Where did you come from, and Who sent you?"\n')
            slow_type('"I came from the garage as you call it. More specifcally i came from the year 1243."\n')
            slow_type('"I was sent by a wizard to help stop the end of times, which if we do not speed this up will be soon."\n')
            slow_type(f'"Will you help me {player_name.capitalize()}? The wizard does not make mistakes so you are the chosen wizard to stop this," Gloombottom said.\n')
            slow_type('The wizard does not make mistakes so you are the chosen wizard to stop this," Gloombottom said.\n')
            slow_type('"You begin to wonder what to do when the cat begins to hiss.\n')
            slow_type('"It is time to get to the garage now!" the cat said. " We do not have time. WE have to close the portal."\n')
            time.sleep(5)
            clear_screen()
            scene2()
        else:
            print("That is not an acceptable answer! .")
            print('Please Type one of the following answers: STAY  or KITCHEN')
            scene1_ans1_choice_1 = input().strip().lower()

def scene1_choice_2():  # Kitchen start it is slightly different then the starting the bedroom but thats okay
    slow_type('You decided that its probably in your best interest to figure out what is going on downstair,\n')
    slow_type('if only for you own sake. You open the door and start down the stairs when out of no where you hear\n')
    slow_type('"Finally! I have been waitng for you to come help me." in a aggresive yet somewhat purring voice.\n')
    slow_type('You jump as you live alone. "Who could have possibly said that?" you say as you start looking frantically\n')
    slow_type('for the mysterious voice. Suddenly a... . a cat? but like a 30lbs cat thats like the size of dog is just\n')
    slow_type('sitting in your kitchen. "I am Sir Dingspitz Gloombottom and I have been sent to warn you of danger."\n')
    slow_type('Your brain locks up as its trying to comprehend what in the what is happening.\n')
    slow_type('"uhh hi." you finally manage. "I have some questions"\n')
    slow_type('"First, how are you talking? Where did you come from, and Who sent you?"\n')
    slow_type('"I came from the garage as you call it. More specifcally I came from the year 1243."\n')
    slow_type('"I was sent by a wizard to help stop the end of times, which if we do not speed this up will be soon."\n')
    slow_type(f'"Will you help me {player_name.capitalize()}? The wizard does not make mistakes so you are the chosen wizard to stop this," Gloombottom said.\n')
    print('Please type one of the following actions:\n')
    print('    HELP      DENY   \n')
    scene1_ans2_choice1 = input().strip().lower()
    scene1_ans2_choice1_tf = 'no_answer'
    while (scene1_ans2_choice1_tf == 'no_answer'):
        if (scene1_ans2_choice1 == 'help'):
            slow_type('"Alright I will help you" you say. "But what am I helping you from?"\n')
            slow_type('"As i was saying we do not have much time." the cat said. "We need to get to the garage and stop this portal!"\n')
            slow_type('The cat started to hiss and do that thing cats do before they strike. "It is time!" the cat hissed.\n')
            time.sleep(4)
            scene1_ans2_choice1_tf == 'answered'
            clear_screen()
            scene2()
        elif(scene1_ans2_choice1 == 'deny'): #Loads the same death as in bedroom do nothing 
            slow_type('A GIANT LIZARD burst in from the garage.\n')
            slow_type('You start to scream!\n')
            slow_type('The lizard screams back...\n')
            slow_type('mist starts to poor in the kitchen\n')
            slow_type('You beign to cough\n')
            time.sleep(4)
            scene1_ans2_choice1_tf == 'answered'
            clear_screen()
            dead_story1()
        else:
            print("That is not an acceptable answer! .")
            print('Please Type one of the following answers: HELP  or DENY')
            scene1_ans2_choice1 = input().strip().lower()      
                
def scene2(): #GARGE 3 answers to choose from because i'll add a third choice again.
    slow_type('You and Sir Dingspitz Gloombottom head to the garage. You can feel a weird energy coming\n')
    slow_type('from the other side of the door. You wisper " Alright cat. What is this about being a wizard?\n')
    slow_type('Gloombottom, sighed, "The world of magic is being over run by evil. Very few in your world have the\n')
    slow_type('needed gifts to do actually perform magic. You are one of them. I will bestow this gift of knowledge to you.\n')
    slow_type('Suddenly the cat rubbed his scent on your legs like all cats would do, but your mind begins to flood with\n')
    slow_type('information from centeries of civilization. You understand the good, and the bad that can now be done.\n')
    slow_type('You also understand you feel alone and you need to defend your home and ignore that cats advice.\n')
    slow_type('Do you close do it with your magical cat friend, and conquer this evil threat?\n')
    slow_type('You could have all the power if you decied to take your new information and make everyone bow to your power..\n')
    slow_type('Do you choose to betray your only magical friend?\n')
    print('Please type one of the following actions:\n')
    print('    CLOSE       DEFEND     BETRAY   \n')
    scene2_ans1 = input().strip().lower()
    scene2_ans1_tf = 'no_answer'
    while (scene2_ans1_tf == 'no_answer'):
        if (scene2_ans1 == 'close'):
            slow_type('That cat quickly asks if you are ready to destroy the portal, before it grows too big and allows all sorts of\n')
            slow_type('evil into this world. You nod your head yes. and grab the door handle to the garage.\n')
            slow_type('"On three. one, two three!" You open the door and the cat springs into action.\n')
            slow_type('There is a giant lizzard starting to poke its head ouf of this odd shaped void in space time.\n')
            slow_type(f'The cat screams, "NOW {player_name.capitalize()}" and you shoot a fireball at the edge of this portal and it begins to weaken.\n')
            slow_type('The cat is darting around keeping the lizzard distracted. You are able to shoot another one and this time\n')
            slow_type('the portal begins to fade. You shoot one last one and it blinks out of existance all at once.\n')
            scene2_ans1_tf = 'answer'
            time.sleep(4)
            scene4()
        elif(scene2_ans1 == 'defend'):
            slow_type('You feel a sense of not being able to do this on your own. "Im sorry, I do not think i can do this."\n')
            slow_type('You pick up a phone and call 911. You call for backup. Gloombottom looks with sadness in his eyes. "WE HAVE TO DO THIS NOW"\n')
            slow_type('"You said you would help me. Help us. If you do not close this portal, were all going to die."\n')
            slow_type('You pause, "I just will not be able to do this all on my own."\n')
            slow_type('As you go back and forth, the phone picks up. A laugh comes from it and you look confused.\n')
            scene2_ans1_tf = 'answer'
            time.sleep(4)
            dead_story2()
        elif(scene2_ans1 == 'betray'):
            print()#NEEEEEEEEED MORE STORY
            scene2_ans1_tf = 'answer'
            slow_type(f'{player_name.capitalize() }\n')
            slow_type('you\n')
            slow_type('sicken\n')
            slow_type('me...\n')
            slow_type('-The Narrator.\n')
            time.sleep(4)
            scene3()
        else:
            print("That is not an acceptable answer! .")
            print('Please Type one of the following answers: CLOSE   DEFEND  BETRAY ')
            scene2_ans1 = input().strip().lower()

def scene3(): # BETRAY ENDING
    slow_type('You decide to betry the cat.\n')
    slow_type('With your new power, not even the Evil Hosts can stop you.\n')
    slow_type('You pure magical energy into the portal.\n')
    slow_type('Your energy is so powerfule it consumes the host of evil.\n')
    slow_type('Gloombottom stares at you in shock\n')
    slow_type('"This is where your journy ends, Cat."\n')
    slow_type('Your betray the cat, and rule the world.\n')
    slow_type(f'Let it be known that {player_name.capitalize()} is a jerk -narrator note\n')
    slow_type('THE END.')
    time.sleep(5)
    restart()   

def scene4(): #Close portal ending
    slow_type('PLEASE NOTE. \n I going to be honest. This file did not save and I had much better endiong the first time.\n')
    slow_type('Sir Dingspitz Gloombottom. What a beautiful name, for your new friend.\n')
    slow_type(f'"{player_name.capitalize()}, thank you for helping me," Gloombottom said.\n')
    slow_type('"What should we do now that you have saved the world?"\n')
    slow_type('"Well I will start off, by thanking you kind Sir. Without your help we could not have won."\n')
    slow_type('you think about what to do next.\n "Can i do something to help you get home?" you say.')
    slow_type(f'"{player_name.capitalize()}, I am stuck here in your time."')
    slow_type('"Well Gloombottom, You can stay with me."')
    print('\n\n\n')
    print('THE END')
    time.sleep(5)
    clear_screen()
    restart()
    
def dead_story1(): #This plays if you stay the first time in your room. it also appears when you refuse to help the cat. 
                   #Gives you one more choice but you die either way.
    slow_type(' Everyone around you including a cat is consummed as the lizzard has just pure evil behind it.\n')
    time.sleep(4)
    slow_type("I'll be honest. That was dumb.\n")
    time.sleep(2)
    print('Please type one of the following actions. Please type only the BOLD word:\n')
    print('    restart ALL     restart STORY \n')
    dead_story1_ans1 = input().strip().lower()
    dead_story1_ans1_tf = 'no_answer'
    while (dead_story1_ans1_tf == 'no_answer'):
        if (dead_story1_ans1 == 'all'):
            print("Yeah you didn't do so well.")
            time.sleep(3)
            dead_story1_ans1_tf = 'answer'
            clear_screen()
            restart()
        elif(dead_story1_ans1 == 'story.'):
            print('You are lucky to get this option.')
            time.sleep(3)
            dead_story1_ans1_tf = 'answer'
            clear_screen()
            select1()
        else:
            print('Please type one of the following actions. Please type only the BOLD word:\n')
            print('    restart ALL     restart STORY \n')
            dead_story1_ans1 = input().strip().lower()

def dead_story2():# end of world ending. aka defend
    slow_type('The laughing continues to get louder, when suddenly the door to the garage is ripped from the frame.\n')
    slow_type('A giant lizzard is staring at you, but the army of endless hosts behind him in this other dimension scares you more.\n')
    slow_type(f'Gloombottom asks for the last time, "Do you think you can still help me die with honor {player_name.capitalize()}?"\n')
    print('Please type one of the following actions:\n')
    print('    HELP      CRY \n')
    dead_story2_ans1 = input().strip().lower()
    dead_story2_ans_tf = 'no_answer'
    while (dead_story2_ans_tf == 'no_answer'):
        if (dead_story2_ans1 == 'help'):
            
            slow_type('"This is my fault Gloombottom. Let us go out with a bang."\n')
            slow_type('You and the cat Charge head on into the sea of evil. You do not survive. But you and\n')
            slow_type('Sir Dingspitz Gloombottom have your honor as the world is consumed.\n')
            slow_type('The end.\n')
            time.sleep(5)
            dead_story2_ans_tf = 'answer'
            clear_screen()
            restart()
        elif(dead_story2_ans1 == 'cry'):
            slow_type('Sir Dingspitz Gloombottom charges into the battle and keeps his honor as the world is consumed.\n')
            slow_type(' You have none.\n')
            slow_type('The end.\n')
            time.sleep(5)
            dead_story2_ans_tf = 'answer'
            clear_screen()
            restart()
        else:
            print('Please type one of the following actions:\n')
            print('    HELP      CRY \n')
            dead_story2_ans1 = input().strip().lower()

def clear_screen():  # Clear the Screen/terminal Function
        os.system('cls' if os.name == 'nt' else 'echo -e \\\\033c')

def restart():   # This restarts the whole Game.
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

if __name__ == '__main__': # i'm still trying to figure this part out but its needed to make main be able to call the functions 
     main()     
     
# please leave notes here.