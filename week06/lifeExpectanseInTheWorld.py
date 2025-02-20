""" 
Author: Santiago Bergerat

Task: Life Expectancy Data
Description: 
- This program analyzes life expectancy data in the world.
- Find the year and country with the lowest and highest life expectancy.
- Allows the user to enter a year to obtain the average life expectancy,
  as well as the country with the minimum and maximum life expectancy in that year.
- It also allows you to enter a country and show its minimum, maximum and average life expectancy.
"""

year_min_expectancy = 0
country_min_expectancy = " "
min_expectancy = 9999
year_max_expectancy = 0 
country_max_expectancy = " "
max_expectancy = 0
total_expectancy = 0
count_year = 0
min_year_expectancy = 9999
country_min_year = " "
max_year_expectancy = 0
country_max_year = ""
total_country_expectancy = 0
count_country = 0
min_country_expectancy = 9999
max_country_expectancy = 0


year_search = input("Enter a year to search: ")
country_search = input("Enter a country to search (or press enter to skip): ").strip().lower()


with open("life-expectancy.csv") as expectancy:
    next(expectancy) 

    for expec in expectancy:
        parts = expec.strip().split(",")
        country = parts[0].strip()
        year = parts[2].strip()
        expectancy_value = float(parts[3].strip())

        if expectancy_value < min_expectancy:
            min_expectancy = expectancy_value
            country_min_expectancy = country
            year_min_expectancy = year

        if expectancy_value > max_expectancy:
            max_expectancy = expectancy_value
            country_max_expectancy = country
            year_max_expectancy = year

        if year == year_search:
            total_expectancy += expectancy_value
            count_year += 1

            if expectancy_value < min_year_expectancy:
                min_year_expectancy = expectancy_value
                country_min_year = country

            if expectancy_value > max_year_expectancy:
                max_year_expectancy = expectancy_value
                country_max_year = country

        if country.lower() == country_search:
            total_country_expectancy += expectancy_value
            count_country += 1

            if expectancy_value < min_country_expectancy:
                min_country_expectancy = expectancy_value

            if expectancy_value > max_country_expectancy:
                max_country_expectancy = expectancy_value

print(f"\nThe country with the lowest life expectancy overall is {country_min_expectancy} in the {year_min_expectancy} with {min_expectancy} years.")
print(f"The country with the highest life expectancy overall is {country_max_expectancy} in the   {year_max_expectancy} with {max_expectancy} years .")

if count_year > 0:
    avg_expectancy = total_expectancy / count_year
    print(f"\nFor the year {year_search}:")
    print(f"The average life expectancy was {avg_expectancy:.2f} years.")
    print(f"The country with the lowest life expectancy was {country_min_year} with {min_year_expectancy} years .")
    print(f"The country with the highest life expectancy was {country_max_year} with {max_year_expectancy} years.")
else:
    print(f"\nNo data available for the year {year_search}.")



if count_country > 0:
    avg_country_expectancy = total_country_expectancy / count_country
    print(f"\nFor the country {country_search.capitalize()}:")
    print(f"- The average life expectancy was {avg_country_expectancy:.2f} years.")
    print(f"- The lowest life expectancy recorded was {min_country_expectancy} years .")
    print(f"- The highest life expectancy recorded was {max_country_expectancy} years.")
elif country_search:
    print(f"\nNo data available for the country {country_search.capitalize()}.")
