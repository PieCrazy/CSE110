# This code is writen by Camden Davis for CSE110 week 6 Milestone

# This program will first read the CSV file and calculate the minimum and maximum life expectancies 
# and the corresponding countries and years. It will also calculate the largest drop in life expectancy 
# from one year to the next for each country. Then it will allow the user to enter a year or a country 
# and display the average life expectancy for that year or the minimum, maximum, and average life expectancies
# for that country.
# The user can continue to enter years or countries until they choose to quit the program.

# analyze_life_expectancy function reads and analyzes the CSV file and returns the results of the 
# analysis along with the dictionaries containing the data by year and by country. 
# The user_interaction function then takes these results and dictionaries as parameters and handles the
# user interaction. This separates the data analysis from the user interaction.


#this was very helpful in understanding the data structures. I stumbled upon it when researching how to better complete this asiignment.
# 
# https://www.geeksforgeeks.org/difference-between-list-and-dictionary-in-python/#




# MILESTONE REQUIREMENTS

# By the middle of the week, to help make sure you are on track to finish the assignment, you need to complete the following:

# Download the dataset

# Load the dataset in your Python program

# Iterate through the data line by line

# Split each line into parts

# Find the lowest value for life expectancy and the highest value for life expectancy in the dataset, and display both values. (Note that at this point, you just need the value for this, not the year and the country for that value.)


import csv

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

        print("These are being printed after reading the data.")
        print(f"Lowest Life Expectancy: {min_life_exp:.2f} in {min_life_exp_country_year}")
        print(f"Highest Life Expectancy: {max_life_exp:.2f} in {max_life_exp_country_year}")
        print(f"Largest Drop: {max_drop:.2f} from {max_drop_country_year[1]} to {max_drop_country_year[2]} in {max_drop_country_year[0]}")

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