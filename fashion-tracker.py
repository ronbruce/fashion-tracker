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
    closetlist.append(item)

# Test function. 
def test():
    # Load data from 'clothing.json'
    data = load_data()

    # Use json.dumps with an indent to format the data for printing.
    formatted_data = json.dumps(data, indent=4)

    # Display the loaded data
    print(formatted_data)

test()

