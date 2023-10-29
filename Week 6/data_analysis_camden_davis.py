# This code is writen by Camden Davis for CSE110 week 6 Data Analysis Project

# This program will first read the CSV file and calculate the minimum and maximum life expectancies 
# and the corresponding countries and years. It will also calculate the largest drop in life expectancy 
# from one year to the next for each country. Then it will allow the user to enter a year or a country 
# and display the average life expectancy for that year or the minimum, maximum, and average life expectancies
# for that country.
# The user can continue to enter years or countries until they choose to quit the program.












# I tried a few ways to do this  i've commentted them out for sake of trying to see what I would do.

'''



# analyze_life_expectancy function reads and analyzes the CSV file and returns the results of the 
# analysis along with the dictionaries containing the data by year and by country. 
# The user_interaction function then takes these results and dictionaries as parameters and handles the
# user interaction. This separates the data analysis from the user interaction.


#this was very helpful in understanding the data structures. I stumbled upon it when researching how to better complete this asiignment.
# 
# https://www.geeksforgeeks.org/difference-between-list-and-dictionary-in-python/#


# #https://stackoverflow.com/questions/72905365/how-to-print-the-average-min-and-max-for-a-specific-year-from-a-csv-file
# # Found this when i had a question. It appears to be the same as what we've been asked to do. i looked to see if possible
# # to learn about this list. However you can learn that by combining our team activty from week 5 and the lessons from this 
# # week and you get the same answers as listed here. I looked so i listed this as a source for something i learned about.






# # A csv.reader object is something that can be used to read the contents of a CSV file.
# # The csv.reader function takes in a file object (csvfile in this case), and optional parameters such 
# # as the delimiter and quote character used in the CSV file. The delimiter parameter specifies the 
# # character that separates the values in each row of the CSV file, while the quotechar parameter 
# # specifies the character used to enclose values that contain the delimiter character. In this case, 
# # the delimiter is set to , and the quote character is set to ". Once you have initialized a csv.reader
# # object, you can use it to iterate over the rows of the CSV file and extract the data you need.





# import csv

# # Open the CSV file
# with open('life-expectancy.csv') as world_data:
#     the_data = csv.reader(world_data, delimiter=',', quotechar='"') 
# # This line of code   ^   initializes a csv.reader object that can be used to read the contents of a CSV file.
# # The csv.reader function takes in a file object, and optional parameters, delimiter and quote character used
# # in the CSV file. The delimiter parameter specifies the 
# # character that separates the data or things int he file you want to rea, in each row of the CSV file, while the quotechar parameter 
# # specifies the character used to enclose values that contain the delimiter character. In this case, 
# # the delimiter is set to , and the quote character is set to ". Once initialized the csv.reader
# # object, you can use it to iterate over the rows of the CSV file and extract the data you need.

# # https://docs.python.org/3/library/csv.html
# # https://python.readthedocs.io/en/v2.7.2/library/csv.html
# # https://realpython.com/python-csv/
# # https://docs.python.org/3.5/library/csv.html
# # https://python-adv-web-apps.readthedocs.io/en/latest/csv.html
# # https://stackoverflow.com/questions/37240535/how-to-read-csv-file-in-python

# # i had to google how what we should do with opening files aside from the lessons in week six this week.
# #below is how i first did based of of the hint, and our intruction videos from this week. i have since changed
# #varible names and how i opened the file.

# with open('life-expectancy.csv') as world_data:
#      next(world_data)
#      for line in world_data:
#          line = line.strip()
#          parts = line.split(',')
#          name_country = parts[0]
#          code = parts[1]
#          year = int(parts[2]) #convert string to int
#          expectancy = float(parts[3]) #convert string to float
        
                
#     # Skip the header row as shown in the mid week email.
#     next(the_data)

#     # set some variables for minimum and maximum life expectancies
#     # They are set to positive and negative infinity. This is done so that any value of life 
#     # expectancy in the file will be less than min_life_expectancy and greater than max_life_expectancy 
#     # initially. This ensures that the first value of life expectancy encountered in the dataset will go 
#     #  to both min_life_expectancy and max_life_expectancy, no matter the real value.
#     # I did not know you could do this until I read about it in this spot. 
#     # I always just chose a big or small number before. so -inf and inf can be actual thing
    
#     # https://stackoverflow.com/questions/34264710/what-is-the-point-of-floatinf-in-python
#     # https://copyprogramming.com/howto/python-float-inf-what-does-it-mean
#     # https://favtutor.com/blogs/infinity-python
#     # https://www.tutorialexample.com/understand-python-floatinf-or-float-inf-with-examples-python-tutorial/
    
    
#     min_life_expectancy = float('inf') # its big so a low number doensn't acidently get set here.
#     max_life_expectancy = float('-inf') # its very small so a high number doesn't get set here.
#     min_country = ''
#     max_country = ''

#     # Iterate through each row of data
#     for row in the_data:  # made it row this time instead of line. its the same thing but i like this name more
#         # Extract the year, country, and life expectancy from the row
#         year = int(row[0])
#         country = row[1]
#         life_expectancy = float(row[3])

#         # Check if this is the new minimum or maximum life expectancy
#         if life_expectancy < min_life_expectancy:
#             min_life_expectancy = life_expectancy
#             min_country = country
#             min_year = year
#         if life_expectancy > max_life_expectancy:
#             max_life_expectancy = life_expectancy
#             max_country = country
#             max_year = year

#     # Print the results for the lowest and highest life expectancies
#     print(f'The country with the lowest life expectancy is {min_country} in {min_year} with a life expectancy of {min_life_expectancy:.2f}.')
#     print(f'The country with the highest life expectancy is {max_country} in {max_year} with a life expectancy of {max_life_expectancy:.2f}.')

#     # Prompt the user to enter a year to find the average life expectancy for that year
#     year_input = input('Enter a year to find the average life expectancy: ')

#     # set some  variables for calculating the average and finding the minimum and maximum countries for that year
#     total_life_expectancy = 0.0
#     num_countries = 0
#     min_life_expectancy_for_year = float('inf')
#     max_life_expectancy_for_year = float('-inf')
#     min_country_for_year = ''
#     max_country_for_year = ''

#     # Iterate through each row of data again to find the average and minimum/maximum countries for the given year
#     world_data.seek(0)
#     next(the_data)
#     for row in the_data:
#         # Extract the year, country, and life expectancy from the row
#         year = int(row[0])
#         country = row[1]
#         life_expectancy = float(row[3])

#         # Check if this is the correct year
#         if year == int(year_input):
#             # Add to the total and count for calculating the average
#             total_life_expectancy += life_expectancy
#             num_countries += 1

#             # Check if this is a new minimum or maximum for this year
#             if life_expectancy < min_life_expectancy_for_year:
#                 min_life_expectancy_for_year = life_expectancy
#                 min_country_for_year = country
#             if life_expectancy > max_life_expectancy_for_year:
#                 max_life_expectancy_for_year = life_expectancy
#                 max_country_for_year = country

#     # Calculate and print the average for the given year, along with the minimum and maximum countries for that year
#     if num_countries > 0:
#         avg_life_expectancy_for_year = total_life_expectancy / num_countries
#         print(f'The average life expectancy in {year_input} was {avg_life_expectancy_for_year:.2f}.')
#         print(f'The country with the lowest life expectancy in {year_input} was {min_country_for_year} with a life expectancy of {min_life_expectancy_for_year:.2f}.')
#         print(f'The country with the highest life expectancy in {year_input} was {max_country_for_year} with a life expectancy of {max_life_expectancy_for_year:.2f}.')





# import csv

# def find_min_max_life_expectancy(reader):
#     # Initialize variables for minimum and maximum life expectancies
#     min_life_expectancy = float('inf')
#     max_life_expectancy = float('-inf')
#     min_country = ''
#     max_country = ''

#     # Iterate through each row of data
#     for row in reader:
#         # Extract the year, country, and life expectancy from the row
#         year = int(row[0])
#         country = row[1]
#         life_expectancy = float(row[3])

#         # Check if this is the new minimum or maximum life expectancy
#         if life_expectancy < min_life_expectancy:
#             min_life_expectancy = life_expectancy
#             min_country = country
#             min_year = year
#         if life_expectancy > max_life_expectancy:
#             max_life_expectancy = life_expectancy
#             max_country = country
#             max_year = year

#     return (min_life_expectancy, min_country, min_year, max_life_expectancy, max_country, max_year)

# def find_avg_min_max_life_expectancy(reader, year_input):
#     # Initialize variables for calculating the average and finding the minimum and maximum countries for that year
#     total_life_expectancy = 0.0
#     num_countries = 0
#     min_life_expectancy_for_year = float('inf')
#     max_life_expectancy_for_year = float('-inf')
#     min_country_for_year = ''
#     max_country_for_year = ''

#     # Iterate through each row of data again to find the average and minimum/maximum countries for the given year


# i kept getting an error here and it was veryf rustrating. i had to come back and just rethink how i wanted to approach this.



#     next(reader)
#     for row in reader:
#         # Extract the year, country, and life expectancy from the row
#         year = int(row[0])
#         country = row[1]
#         life_expectancy = float(row[3])

#         # Check if this is the correct year
#         if year == int(year_input):
#             # Add to the total and count for calculating the average
#             total_life_expectancy += life_expectancy
#             num_countries += 1

#             # Check if this is a new minimum or maximum for this year
#             if life_expectancy < min_life_expectancy_for_year:
#                 min_life_expectancy_for_year = life_expectancy
#                 min_country_for_year = country
#             if life_expectancy > max_life_expectancy_for_year:
#                 max_life_expectancy_for_year = life_expectancy
#                 max_country_for_year = country

#     return (total_life_expectancy, num_countries, min_life_expectancy_for_year, min_country_for_year, max_life_expectancy_for_year, max_country_for_year)

# # Open the CSV file
# with open('life-expectancy.csv', newline='') as csvfile:
#     reader = csv.reader(csvfile, delimiter=',', quotechar='"')

#     # Skips the header row as shown in th class hint
#     next(reader)

#     # Find the lowest and highest life expectancies in the dataset
#     (min_life_exp, min_country, min_year, max_life_exp, max_country, max_year) = find_min_max_life_expectancy(reader)

#     # Print the results for the lowest and highest life expectancies
#     print(f'The year and country with the lowest life expectancy is {min_country} in {min_year} with a life expectancy of {min_life_exp:.2f}.')
#     print(f'The year and country with the highest life expectancy is {max_country} in {max_year} with a life expectancy of {max_life_exp:.2f}.')

#     # Prompt the user to enter a year to find the average life expectancy for that year
#     year_input = input('Enter a year to find the average life expectancy: ')

#     # Find the average and minimum/maximum countries for that year
#     (total_exp, num_countries, min_exp_for_yr, min_ctry_for_yr, max_exp_for_yr, max_ctry_for_yr) = find_avg_min_max_life_expectancy(reader, year_input)

#     # Calculate and print the average for the given year, along with the minimum and maximum countries for that year
#     if num_countries > 0:
#         avg_exp_for_yr = total_exp / num_countries
#         print(f'The average life expectancy in {year_input} was {avg_exp_for_yr:.2f}.')
#         print(f'The country with the lowest life expectancy in {year_input} was {min_ctry_for_yr} with a life expectancy of {min_exp_for_yr:.2f}.')
#         print(f'The country with the highest life expectancy in {year_input} was {max_ctry_for_yr} with a life expectancy of {max_exp_for_yr:.2f}.')

'''


import csv




# This program will first read the CSV file and calculate the minimum and maximum life expectancies 
# and the corresponding countries and years. It will also calculate the largest drop in life expectancy 
# from one year to the next for each country.



def analyze_life_expectancy():
    with open('life-expectancy.csv') as world_data:
        next(world_data)
        data = csv.reader(world_data)
        year_dict = {}
        country_dict = {}
        min_life_exp = float('inf')
        max_life_exp = float('-inf')
        min_life_exp_country_year = ""
        max_life_exp_country_year = ""
        prev_life_exp = {}
        max_drop = float('-inf')
        max_drop_country_year = ""

# above idecared some variables so we could call them


#i'm anaylising the data here and splitting it.

        for row in data:
            country, year, life_exp = row[0], int(row[2]), float(row[3])
            if life_exp < min_life_exp:
                min_life_exp = life_exp
                min_life_exp_country_year = (country, year)
            if life_exp > max_life_exp:
                max_life_exp = life_exp
                max_life_exp_country_year = (country, year)

            if year not in year_dict:
                year_dict[year] = []
            year_dict[year].append(life_exp)

            if country not in country_dict:
                country_dict[country] = []
            country_dict[country].append(life_exp)

            if country in prev_life_exp:
                drop = prev_life_exp[country] - life_exp
                if drop > max_drop:
                    max_drop = drop
                    max_drop_country_year = (country, year-1, year)
            prev_life_exp[country] = life_exp

# getting the data overall printed.


        print("These are being printed after reading the data.")
        print(f"Lowest Life Expectancy: {min_life_exp:.2f} in {min_life_exp_country_year}")
        print(f"Highest Life Expectancy: {max_life_exp:.2f} in {max_life_exp_country_year}")
        print(f"Largest Drop: {max_drop:.2f} from {max_drop_country_year[1]} to {max_drop_country_year[2]} in {max_drop_country_year[0]}")


# This loops so that the user can Choose a year  or country for analysis. 
# This goes until they quit. I ran out of time this week to make it super fancy but it works. 
# (had a vacation come up and i couldn't make fancy functions and test it. had to submit this days early due to that)

        while True:
            choice = input("Enter 'Y' for Year Analysis, 'C' for Country Analysis or 'Q' to Quit: ")
            if choice.lower() == 'y':
                year = int(input("Enter a Year: "))
                if year in year_dict:
                    avg_life_exp = sum(year_dict[year]) / len(year_dict[year])
                    print(f"Average Life Expectancy in {year}: {avg_life_exp:.2f}")
                else:
                    print("Year not found in data.")
            elif choice.lower() == 'c':
                country = input("Enter a Country: ")
                if country in country_dict:
                    min_life_exp_country = min(country_dict[country])
                    max_life_exp_country = max(country_dict[country])
                    avg_life_exp_country = sum(country_dict[country]) / len(country_dict[country])
                    print(f"Life Expectancy in {country} - Min: {min_life_exp_country:.2f}, Max: {max_life_exp_country:.2f}, Avg: {avg_life_exp_country:.2f}")
                else:
                    print("Country not found in data.")
            elif choice.lower() == 'q':
                break
            else:
                print("Invalid choice. Please enter again.")

analyze_life_expectancy()
