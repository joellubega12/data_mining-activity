import csv  # For handling CSV file operations
import pandas as pd  # For advanced data manipulation and analysis


# Defining a class to represent a university and its attributes
class University:
    def __init__(university, name, country, overall_score, world_rank, year):
        # Initializing the attributes of the University object
        university.name = name
        university.country = country
        university.overall_score = float(overall_score)  # Convert score to float for calculations
        university.world_rank = int(world_rank)  # Convert rank to integer for sorting
        university.year = int(year)  # Convert year to integer for filtering

    def display_info(university):
        # Method to display the details of a university in a formatted way
        print(f"  Name: {university.name} ({university.year})")
        print(f"  Country: {university.country}")
        print(f"  World Rank: {university.world_rank}")
        print(f"  Score: {university.overall_score:.2f}")
        print("-" * 30)


# Function to load university data from a CSV file
def load_university_data(filepath="cwurData.csv"):
    # Initialize an empty list to store University objects
    universities_list = []
    try:
        # Open the CSV file in read mode with UTF-8 encoding
        with open(filepath, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)  # Read the file as a dictionary

            # Iterate through each row in the CSV file
            for row in reader:
                try:
                    # Create a University object for each valid row
                    uni_object = University(
                        name=row['institution'],
                        country=row['country'],
                        overall_score=row['score'],
                        world_rank=row['world_rank'],
                        year=row['year']
                    )
                    # Add the University object to the list
                    universities_list.append(uni_object)
                except (ValueError, KeyError):
                    # Skip rows with missing or invalid data
                    pass
    except FileNotFoundError:
        # Handle the case where the file is not found
        print(f"Error: The file '{filepath}' was not found.")
        print("Please make sure it is in the same directory as this Python script.")
    except Exception as e:
        # Handle any other exceptions that occur while reading the file
        print(f"An error occurred while reading the file: {e}")
    return universities_list


# Function to group universities by country and sort them by world rank
def group_and_rank_by_country(universities_list):
    grouped_data = {}  # Dictionary to store grouped data by country

    # Iterate through the list of universities
    for uni in universities_list:
        country = uni.country  # Extract the country of the university

        # Check if the country is already in the dictionary
        if country not in grouped_data:
            grouped_data[country] = []  # Initialize an empty list for the country
        grouped_data[country].append(uni)  # Add the university to the country's list

    # Sort the universities in each country by their world rank
    for country, unis in grouped_data.items():
        unis.sort(key=lambda u: u.world_rank)

    return grouped_data


# Main execution block
if __name__ == "__main__":
    print("--- World University Rankings Analysis ---")

    # Load all university data from the CSV file
    all_universities = load_university_data()

    if all_universities:
        # Display the total number of valid university entries loaded
        print(f"\nSuccessfully loaded data for {len(all_universities)} valid university entries.")

        # Filter the data to include only universities from the year 2015
        universities_2015 = []
        for uni in all_universities:
            if uni.year == 2015:
                universities_2015.append(uni)

        # Display the number of universities found for the year 2015
        print(f"Found {len(universities_2015)} entries for the year 2015.")

        # Group the 2015 data by country and sort by rank
        ranked_by_country_2015 = group_and_rank_by_country(universities_2015)

        # List of countries to display rankings for
        countries_to_display = ["USA", "United Kingdom", "Canada", "Germany", "Japan", "France", "Switzerland", "Australia", "Italy", "Netherlands"]

        # Display the top 10 universities for each selected country
        for country in countries_to_display:
            if country in ranked_by_country_2015:
                print(f"\n--- Top 10 Universities in {country} (2015) ---")
                top_universities = ranked_by_country_2015[country]

                # Display up to 10 universities for the country
                for i in range(min(10, len(top_universities))):
                    uni = top_universities[i]
                    print(f"National Rank: {i+1}")
                    uni.display_info()
            else:
                # Handle the case where no data is available for the country
                print(f"\n--- No data found for {country} in 2015 ---")