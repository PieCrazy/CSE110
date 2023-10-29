# #Yes, you can use the typing effect with inputs as well. Here’s an example:

# #Python
# #This code is AI-generated. Review and use carefully. Visit our FAQ for more information.

# # import sys
# # import time

# # def slow_type(text):
# #     for char in text:
# #         sys.stdout.write(char)
# #         sys.stdout.flush()
# #         time.sleep(0.1)

# # def type_with_input(prompt):
# #     slow_type(prompt)
# #     return input()

# # name = type_with_input("What is your name? ")
# # slow_type(f"Hello, {name}! This is a typing effect in an f-string.")
# # In this example, the slow_type function is defined as before. A new function type_with_input is defined that takes a prompt as input, displays the prompt with the typing effect, and then returns the user’s input. You can use this function to get input from the user with a typing effect.

# # You can replace "What is your name? " with any prompt you want to display. When you run the program, it will display the prompt with the typing effect and then wait for the user to enter their input.

# # Please note that the typing effect will only be visible if you run the code in a terminal or console environment. If you are using an integrated development environment (IDE) with its own output window, the typing effect may not be visible.

# # import time
# # import sys
# # text = "Hello, this is a test text to see if all works fine."
# # for char in text:
# #     print (char, end="", flush=True)
# #     time.sleep(0.2)

# #I'm trying to global import these, but idk if my logic is correct here or not.
# import time
# def slow_type(text_output):
#     for letter in text_output:
#         print (letter, end="", flush=True)
#         time.sleep(0.06)



# import os
# import sys
# # this is the typing effect the way i figured out first. trying this instead.
# # def slow_type(text_output):
# #     for letter in text_output:
# #         sys.stdout.write(letter)
# #         sys.stdout.flush()
# #         time.sleep(0.07)
# # this is the typing effect added to input so you can ask a question and have that slow type effect
# # def type_with_input(prompt):
# #     slow_type(prompt)
# #     return input()
# def type_with_input(prompt):
#     slow_type(prompt)
#     return input()

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

#     def clear():
#         os.system('cls' if os.name == 'nt' else 'echo -e \\\\033c')
#     clear()
#     #Cleared the title
#     #this function will be called alot to clear the terminal to keep things nice and tighty.
#     slow_type('TESTING INTRO NAMES\n')
#     #Gathering the information
#     player_name = type_with_input('What is your name? \n')
#     # This part will intoduce the concept of making choices. This will be a simple one that 
#     # basically explain the idea no matter the choice
#     # this also should cause the player to ease up and get them hooked into the story.
#     slow_type(f'Hello {player_name.capitalize()}. This will be...')
#     print('\n\n\n\n\n') #6 spaces
#     time.sleep(2)
#     slow_type('Well an adventure of course!\n') #if iput this at he end i just want spacing to be there in fewer print statements
#     time.sleep(1)
#     slow_type('What else would this be?\n\n') #adding a space by \n at the end.
#     time.sleep(2)
#     slow_type(f'You know {player_name.capitalize()} we need to get our story in order before the \nauthorities get here and have us turning on eachother. ')
#     slow_type(f'So tell me.... where were you when this all starte to happen?            \n{player_name.capitalize()}, remember not only your reputation is on the line. ?')
#     time.sleep(2)
#     print('                     Please type your choice.\n Please type 1 or 2 for this question.')
#     time.sleep(2)
#     slow_type('"Who are you?!.... What even are you?')
#     print('                             ANSWER 1')
#     time.sleep(1)
#     slow_type('"It started when I woke up in my room. ')
#     print('                           ANSWER 2')
#     time.sleep(1)
#     #This question is not a all caps on purpose please dont dock me in the rubric for this.
#     # I'm going to try and use a few differnt ways based on what i learend for how to do loops and 
#     # if statments i want to test which one i like best. 
#     intro_c1 = input()
#     time.sleep(2)
#     intro_ans1 = 'no_answer'
#     while (intro_ans1 == 'no_answer'):
#         if (intro_c1 == '1'):
#             slow_type("\nWell I for one thought this was obvious... Its me. Your guilty conscious. ")
#             slow_type('All jokes and sarcasm aside, I will be the story narrator for this adventure. So really,\nit is not important who I am. Next time think about these choices you make.\n The story can chnage depending on what you choose to say or do.')
#             slow_type('Well now that you undertand the concept of how this will play out, lets proceed to the real adventure!')
#             select1()
#             intro_ans1 = 'answer'
#         elif(intro_c1 == '2'):
#             slow_type("Wow you're just gunna start like that??!\n Not even a question about what the heck is going on?\n That...\n That is is a bold stratgey.")
#             slow_type('\n All jokes and sarcasm aside, i will be the story narrator for this adventure. So really,\nit is not important who I am. Next time think about these choices you make.\n The story can chnage depending on what you choose to say or do.')
#             slow_type('Well now that you undertand the concept of how this will play out, lets proceed to the real adventure!')
#             select1()
#         else:
#             slow_type('That is not an acceptable answer! You can onl type "1"  or  "2" ')
#             intro_c1 = input()
# main()

# def select1():
#         select1_ans1 = 'no_answer'
#         while (select1_ans1 == 'no_answer'):
#             if (select1_ans1 == '1'):
                
#                 scene1_choice_1()
#             elif(select1_ans1 == '2'):
#                 scene1_choice_2()
                
#             else:
#                 print('That is not an acceptable answer. You can onl type "1"  or  "2" ')
#                 select1_ans1 = input()        
# select1()

# def scene1_choice_1():
#         scene1_ans1_choice_1 = 'no_answer'
#         while (scene1_ans1_choice_1 == 'no_answer'):
#             if(scene1_ans1_choice_1 == 'A'):
#                 print('DEBUG scene 1 choice 1  if statment')
#             elif(scene1_ans1_choice_1 == 'B'):
#                 print('DEBUG scene 1 choice1  elif statment')
#             else:
#                 print('That is not an acceptable answer. You can onl type "1"  or  "2" ')
#                 scene1_ans1_choice_1 = input()
# scene1_choice_1()

# def scene1_choice_2():
#         scene1_ans2_choice1 = 'no_answer'
#         while (scene1_ans2_choice1 == 'no_answer'):
#             if (scene1_ans2_choice1 == 'A'):
#                 print()
                
#                 #another if statment fora second choice in this scene
                
#             elif(scene1_ans2_choice1 == 'B'):
#                 print()
#                 #another if statment for a second choice in this scene
#             else:
#                 print('That is not an acceptable answer. You can onl type "1"  or  "2" ')
#                 scene1_ans2_choice1 = input()      
# scene1_choice_2()




print('wehpgjodsjgdslg\ndfkjdjksjflsdfjdlskfjskdlfjdsklfjlkds\nfdsadfksjfdksjfdskjfdlksjfksdjfkdls    '   )
print('this is a new line')










