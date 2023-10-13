import json

# Load data from 'clothing.json'.
# 'try' and 'except' are used to catch errors.
# If the file 'closet.json' is not found, it will set 'data' to an empty dictionary '{categories": []}' as a default.
def load_data():
    try:
        with open('closet.json', 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        data = {"categories": []}
    return data

# Initialize closetlist with data from 'closet.json'.
# closetlist contains the data from the 'closet.json' file.
closetlist = load_data()
closetlist = load_data()

# Add a new item to the closet.
# 'closetlist.append(item)' adds the 'item' provided as an argument to your 'closetlist'.
def create(item):
    if "categories" not in closetlist: # Checks to see if 'categories' key is present in 'closetlist'
        closetlist["categories"] = [] # If no categories then create empty list
    category = closetlist["categories"][0] # Access the first categories for demonstration.
    category["items"].append(item)
    save_data()

# Function to save data back to 'closet.json'.
def save_data():
    with open('closet.json', 'w') as file:
        json.dump(closetlist, file, indent=4)

# Input an item to add to the closet.
item = input("Hey! Enter the drip to add to your closet: ")
create(item) # Call the create function to add to the item.

print(f"{item} added to your closet.")

# Test function. 
# def test():
#     # Load data from 'clothing.json'
#     data = load_data()

#     # Use json.dumps with an indent to format the data for printing.
#     formatted_data = json.dumps(data, indent=4)

#     # Display the loaded data
#     print(formatted_data)

# test()

