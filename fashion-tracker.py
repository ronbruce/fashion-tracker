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


# Add a new item to the closet.
# 'closetlist.append(item)' adds the 'item' provided as an argument to your 'closetlist'.
def create_item():
    category = input("Hey! Enter the category (e.g. casual, business casual, business professional)")
    name = input("Now enter the name of the item: ")
    item_type = input("Enter the type of the item: ")
    price = float(input("Enter the price of the item: "))
    brand = input("Enter the brand of the item: ")

    new_item = {
        "name": name,
        "type": item_type,
        "price": price,
        "brand": brand
    }


    for category_data in closetlist["categories"]:
        if category_data["id"] == category:
            category_data["items"].append(new_item)
            save_data()
            print(f"{name} added to the {category} category.")


def save_data():
    with open('closet.json', 'w') as file:
        json.dump(closetlist, file, indent=4)

def main():
    while True:
        create_item()
        another_item = input("Good looks! Would you like to put some more drip in your closet? (yes/no)? ").lower()
        if another_item != "yes":
            break
    
if __name__ == "__main__":
    main()


