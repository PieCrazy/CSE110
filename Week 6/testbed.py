import csv
def find_min_max_life_expectancy(reader):
    # Initialize variables for minimum and maximum life expectancies
    min_life_expectancy = float('inf')
    max_life_expectancy = float('-inf')
    min_country = ''
    max_country = ''
    # Iterate through each row of data
    for row in reader:
        # Extract the year, country, and life expectancy from the row
        year = int(row[0])
        country = row[1]
        life_expectancy = float(row[3])
        # Check if this is the new minimum or maximum life expectancy
        if life_expectancy < min_life_expectancy:
            min_life_expectancy = life_expectancy
            min_country = country
            min_year = year
        if life_expectancy > max_life_expectancy:
            max_life_expectancy = life_expectancy
            max_country = country
            max_year = year
    return (min_life_expectancy, min_country, min_year, max_life_expectancy, max_country, max_year)
def find_avg_min_max_life_expectancy(reader, year_input):
    # Initialize variables for calculating the average and finding the minimum and maximum countries for that year
    total_life_expectancy = 0.0
    num_countries = 0
    min_life_expectancy_for_year = float('inf')
    max_life_expectancy_for_year = float('-inf')
    min_country_for_year = ''
    max_country_for_year = ''
    # Iterate through each row of data again to find the average and minimum/maximum countries for the given year
    csvfile.seek(0)
    next(reader)
    for row in reader:
        # Extract the year, country, and life expectancy from the row
        year = int(row[0])
        country = row[1]
        life_expectancy = float(row[3])
        # Check if this is the correct year
        if year == int(year_input):
            # Add to the total and count for calculating the average
            total_life_expectancy += life_expectancy
            num_countries += 1
            # Check if this is a new minimum or maximum for this year
            if life_expectancy < min_life_expectancy_for_year:
                min_life_expectancy_for_year = life_expectancy
                min_country_for_year = country
            if life_expectancy > max_life_expectancy_for_year:
                max_life_expectancy_for_year = life_expectancy
                max_country_for_year = country
    return (total_life_expectancy, num_countries, min_life_expectancy_for_year, min_country_for_year, max_life_expectancy_for_year, max_country_for_year)
def analyze_data():
    # Open the CSV file
    with open('life-expectancy.csv', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='"')
        # Skip the header row
        next(reader)
        # Find the lowest and highest life expectancies in the dataset
        (min_life_exp, min_country, min_year, max_life_exp, max_country, max_year) = find_min_max_life_expectancy(reader)
        # Print the results for the lowest and highest life expectancies
        print(f'The year and country with the lowest life expectancy is {min_country} in {min_year} with a life expectancy of {min_life_exp:.2f}.')
        print(f'The year and country with the highest life expectancy is {max_country} in {max_year} with a life expectancy of {max_life_exp:.2f}.')
        # Prompt the user to enter a year to find the average life expectancy for that year
        year_input = input('Enter a year to find the average life expectancy: ')
        # Find the average and minimum/maximum countries for that year
        (total_exp, num_countries, min_exp_for_yr, min_ctry_for_yr, max_exp_for_yr, max_ctry_for_yr) = find_avg_min_max_life_expectancy(reader, year_input)
        # Calculate and print the average for the given year, along with the minimum and maximum countries for that year
        if num_countries > 0:
            avg_exp_for_yr = total_exp / num_countries
            print(f'The average life expectancy in {year_input} was {avg_exp_for_yr:.2f}.')
            print(f'The country with the lowest life expectancy in {year_input} was {min_ctry_for_yr} with a life expectancy of {min_exp_for_yr:.2f}.')
            print(f'The country with the highest life expectancy in {year_input} was {max_ctry_for_yr} with a life expectancy of {max_exp_for_yr:.2f}.')
def main():
    analyze_data()
if __name__ == '__main__':
    main()

















# # Initialize variables
# data = []
# min_life_exp = float('inf')
# max_life_exp = float('-inf')
# min_life_exp_info = ""
# max_life_exp_info = ""

# # Load the dataset
# with open('life-expectancy.csv') as world_data:
#     next(world_data)
#     for line in world_data:
#         line = line.strip()
#         parts = line.split(',')
#         name_country = parts[0]
#         code = parts[1]
#         year = int(parts[2]) #convert string to int
#         expectancy = float(parts[3]) #convert string to float

#         # Add data to list
#         data.append((name_country, code, year, expectancy))

#         # Update min and max life expectancy
#         if expectancy < min_life_exp:
#             min_life_exp = expectancy
#             min_life_exp_info = (name_country, year)
#         if expectancy > max_life_exp:
#             max_life_exp = expectancy
#             max_life_exp_info = (name_country, year)

# print(f"Lowest life expectancy: {min_life_exp} in {min_life_exp_info[0]} ({min_life_exp_info[1]})")
# print(f"Highest life expectancy: {max_life_exp} in {max_life_exp_info[0]} ({max_life_exp_info[1]})")

# # Function to find average, min, and max life expectancy for a given year
# def life_expectancy_in_year(year):
#     year_data = [d for d in data if d[2] == year]
#     avg_life_exp = sum(d[3] for d in year_data) / len(year_data)
#     min_life_exp = min(d[3] for d in year_data)
#     max_life_exp = max(d[3] for d in year_data)
#     print(f"In {year}, average life expectancy: {avg_life_exp}, min: {min_life_exp}, max: {max_life_exp}")

# # Function to find min, max, and average life expectancy for a given country
# def life_expectancy_in_country(country):
#     country_data = [d for d in data if d[0] == country]
#     avg_life_exp = sum(d[3] for d in country_data) / len(country_data)
#     min_life_exp = min(d[3] for d in country_data)
#     max_life_exp = max(d[3] for d in country_data)
#     print(f"In {country}, average life expectancy: {avg_life_exp}, min: {min_life_exp}, max: {max_life_exp}")