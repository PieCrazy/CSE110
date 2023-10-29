# This code is writen by Camden Davis for CSE110 week 3 Adventure Game
# I have listed sources as i first learned them for the first two weeks projects, and where i went to learn new things for this project.
# I have spent time trying to learn some more advanced concepts, and rely on knowlege/ logic from my c++ classes i took a few years back
# i have group serveral comments to gether with the # all being one connected thought.


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



#I'm trying to global import these, but idk if my logic is correct here or not.
import time
def slow_type(text_output):
    for letter in text_output:
        print (letter, end="", flush=True)
        time.sleep(0.06)



import os
import sys
# this is the typing effect the way i figured out first. trying this instead.
# def slow_type(text_output):
#     for letter in text_output:
#         sys.stdout.write(letter)
#         sys.stdout.flush()
#         time.sleep(0.07)
# this is the typing effect added to input so you can ask a question and have that slow type effect
# def type_with_input(prompt):
#     slow_type(prompt)
#     return input()
def type_with_input(prompt):
    slow_type(prompt)
    return input()
# example of how that would work for reference
#  name = type_with_input("What is your name? ")
#  slow_type(f"Hello, {name}! This is a typing effect in an f-string.")


# this was how a comment said to do it with a \n. I somehow when trying to make mine kept messing up the \n
# # import sys,time
# # def sprint(str):
# #    for c in str + '\n':
# #      sys.stdout.write(c)
# #      sys.stdout.flush()
# #      time.sleep(3./90)

# # sprint('hello world')

# leaving this here to see if i can figure out the \n later


# figured it out took a couple days but i got it.

#orginal way i got this all to work. back up jsut in case i mess up the intro

# def main():
#     #I realized in the past to, I reduntly imported time and os every time i wanted to do those time delays and clear console
#     # I'll put them here and for good measure i'll import them at the beginning of tyhe functions to.( but not type them everytime.)
#     #
#     import time
#     import os
#     # time.sleep(2)  I'm puting this around alot for pacing and 
#     # so the game has an animation pasuing  effect
#     import sys  #adding this to get the typing animation function to try and work correctly. 
#     print()
#     print()
#     print()
#     slow_type("Camden Proudly Presents ")
#     # time delay
#     time.sleep(3) # Sleep for 3 seconds
#     #Clearing the title
#     def clear_screen():
#         os.system('cls' if os.name == 'nt' else 'echo -e \\\\033c')
#     clear_screen()
#     #Cleared the title
#     #this function will be called alot to clear the terminal to keep things nice and tighty.
    
#     #Gathering the information
#     player_name = input('What is your name? ')
#     # This part will intoduce the concept of making choices. This will be a simple one that 
#     # basically explain the idea no matter the choice
#     # this also should cause the player to ease up and get them hooked into the story.
#     print(f'Hello {player_name.capitalize()}. This is will be...')
#     print('\n\n\n\n\n') #6 spaces
#     time.sleep(2)
#     print('Well an adventure of course!\n ') #if iput this at he end i just want spacing to be there in fewer print statements
#     time.sleep(1)
#     print('What else would this be?\n\n') #adding a space by \n at the end.
#     time.sleep(2)
#     print(f'You know {player_name.capitalize()} we need to get our story in order before the\n the authorities get here and have us turning on eachother. ')
#     print(f'So tell me.... where were you when this all starte to happen? \n{player_name.capitalize()}, remember not only your reputation is on the line. ?')
#     time.sleep(2)
#     print('                     Please type your choice.\n Please type 1 or 2 for this question.')
#     time.sleep(2)
#     print('"Who are you?!.... What even are you?  \nANSWER 1\n')
#     time.sleep(1)
#     print('"It started when I woke up in my room. \nANSWER 2\n')
#     time.sleep(1)
#     intro_c1 = input()
#     time.sleep(2)
#     #This question is not a all caps on purpose please dont dock me in the rubric for this.
#     # I'm going to try and use a few differnt ways based on what i learend for how to do loops and 
#     # if statments i want to test which one i like best.  
# main()





def main():
    #I realized in the past to, I reduntly imported time and os every time i wanted to do those time delays and clear console
    # I'll put them here and for good measure i'll import them at the beginning of tyhe functions to.( but not type them everytime.)
    #
    import time
    import os
    # time.sleep(2)  I'm puting this around alot for pacing and 
    # so the game has an animation pasuing  effect
    import sys  #adding this to get the typing animation function to try and work correctly. 
    print()
    print()
    print()
    slow_type("Camden Proudly Presents ")
    # time delay
    time.sleep(3) # Sleep for 3 seconds
    #Clearing the title

    def clear():
        os.system('cls' if os.name == 'nt' else 'echo -e \\\\033c')
    clear()
    #Cleared the title
    #this function will be called alot to clear the terminal to keep things nice and tighty.
    slow_type('TESTING INTRO NAMES\n')
    #Gathering the information
    player_name = type_with_input('What is your name? \n')
    # This part will intoduce the concept of making choices. This will be a simple one that 
    # basically explain the idea no matter the choice
    # this also should cause the player to ease up and get them hooked into the story.
    slow_type(f'Hello {player_name.capitalize()}. This will be...')
    print('\n\n\n\n\n') #6 spaces
    time.sleep(2)
    slow_type('Well an adventure of course!\n') #if iput this at he end i just want spacing to be there in fewer print statements
    time.sleep(1)
    slow_type('What else would this be?\n\n') #adding a space by \n at the end.
    time.sleep(2)
    time.sleep(1)
    #This question is not a all caps on purpose please dont dock me in the rubric for this.
    # I'm going to try and use a few differnt ways based on what i learend for how to do loops and 
    # if statments i want to test which one i like best. 
    intro_c1 = input()
    time.sleep(2)
    intro_ans1 = 'no_answer'
    while (intro_ans1 == 'no_answer'):
        if (intro_c1 == '1'):
            slow_type("\nWell I for one thought this was obvious... Its me. Your guilty conscious. ")
            slow_type('All jokes and sarcasm aside, I will be the story narrator for this adventure. So really,\nit is not important who I am. Next time think about these choices you make.\n The story can chnage depending on what you choose to say or do.')
            slow_type('Well now that you undertand the concept of how this will play out, lets proceed to the real adventure!')
            select1()
            intro_ans1 = 'answer'
        elif(intro_c1 == '2'):
            slow_type("Wow you're just gunna start like that??!\n Not even a question about what the heck is going on?\n That...\n That is is a bold stratgey.")
            slow_type('\n All jokes and sarcasm aside, i will be the story narrator for this adventure. So really,\nit is not important who I am. Next time think about these choices you make.\n The story can chnage depending on what you choose to say or do.')
            slow_type('Well now that you undertand the concept of how this will play out, lets proceed to the real adventure!')
            select1()
        else:
            slow_type('That is not an acceptable answer! You can onl type "1"  or  "2" ')
            intro_c1 = input()


#END on intro Either anwser above loads select 1 which sets the story up. there are Main difference stories.
#       |
#       |
#       |
#       v
    def select1():
        select1_ans1 = 'no_answer'
        while (select1_ans1 == 'no_answer'):
            if (select1_ans1 == '1'):
                
                scene1_choice_1()
            elif(select1_ans1 == '2'):
                scene1_choice_2()
                
            else:
                print('That is not an acceptable answer. You can onl type "1"  or  "2" ')
                select1_ans1 = input()        
    select1()

#story selection

#         this is the scene that plays if you make choice 1 in scene 1 The first choice Ultimately changes the story
    def scene1_choice_1():
        scene1_ans1_choice_1 = 'no_answer'
        while (scene1_ans1_choice_1 == 'no_answer'):
            if(scene1_ans1_choice_1 == 'A'):
                print('DEBUG scene 1 choice 1  if statment')
            elif(scene1_ans1_choice_1 == 'B'):
                print('DEBUG scene 1 choice1  elif statment')
            else:
                print('That is not an acceptable answer. You can onl type "1"  or  "2" ')
                scene1_ans1_choice_1 = input()
    scene1_choice_1()

    def scene1_choice_2():
        scene1_ans2_choice1 = 'no_answer'
        while (scene1_ans2_choice1 == 'no_answer'):
            if (scene1_ans2_choice1 == 'A'):
                print()
                
                #another if statment fora second choice in this scene
                
            elif(scene1_ans2_choice1 == 'B'):
                print()
                #another if statment for a second choice in this scene
            else:
                print('That is not an acceptable answer. You can onl type "1"  or  "2" ')
                scene1_ans2_choice1 = input()      
    scene1_choice_2()
#                 this is teh scne that plays if you amke choice 2 in scene 1   The first choice Ultimately changes the story


    def choice1_scene1():
        scene1_ans1 = 'no_answer'
        while (scene1_ans1 == 'no_answer'):
            if (scene1_ans1 == 'blah1'):
                print()
            elif(scene1_ans1 == 'blah2'):
                scene1_ans1()
                print()
            else:
                print('That is not an acceptable answer. You can onl type "1"  or  "2" ')
                scene1_ans1 = input()
    choice1_scene1()


    def choice2_scene1():
        scene1_ans1 = 'no_answer'
        while (scene1_ans1 == 'no_answer'):
            if (scene1_ans1 == 'blah1'):
                
                restart()
            elif(scene1_ans1 == 'blah2'):
                restart()
                
            else:
                print('That is not an acceptable answer. You can onl type "1"  or  "2" ')
                scene1_ans1 = input()
    choice2_scene1()

      
    def scene4():
        scene4_ans1 = 'no_answer'
        while (scene4_ans1 == 'no_answer'):
            if (scene4_ans1 == 'blah'):
                print()
            elif(scene4_ans1 == 'blah 2'):
                print()
            else:
                print('That is not an acceptable answer. You can onl type "1"  or  "2" ')
                scene4_ans1 = input()
    scene4() 

##############                     ENDING BY DEATH STORY 1 and 2                       ###################
    def dead_story1():
        dead_story1_ans1 = 'no_answer'
        while (dead_story1_ans1 == 'no_answer'):
            if (dead_story1_ans1 == 'blah'):
                print()
            elif(dead_story1_ans1 == 'blah 2'):
                print()
            else:
                print('That is not an acceptable answer. You can onl type "1"  or  "2" ')
                dead_story1_ans1 = input()
    dead_story1()

    def dead_story2():
        dead_story2_ans1 = 'no_answer'
        while (dead_story2_ans1 == 'no_answer'):
            if (dead_story2_ans1 == 'blah'):
                print()
            elif(dead_story2_ans1 == 'blah 2'):
                print()
            else:
                print('That is not an acceptable answer. You can onl type "1"  or  "2" ')
                dead_story2_ans1 = input()
    dead_story2()


##############                     ENDING BY DEATH STORY 1 and 2                       ###################
    
    
 # This Function gets called if the Player dies or finishes the game and would like to try and do it again
 # With a different set of choices.

    def restart():
    #this uses boolean logic. 
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

# clear screen/console/terminal function

    def clear_screen():
        os.system('cls' if os.name == 'nt' else 'echo -e \\\\033c')
    clear_screen()
main()

#Please put feedback here
#
    
    
    
    
    
    

    
    

