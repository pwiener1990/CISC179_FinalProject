print("Clothing Item Generator")

import random

# User will input the current temperature and the description is determined using branching.
temperature = int(input("Enter the temperature in Fahrenheit: "))

if -20 < temperature <= 45:
    temperature = "cold"
   
elif 46 < temperature <= 75:
    temperature = "mild"
       
elif 76 < temperature <= 120:
    temperature = "hot"
   
else:
    temperature = "invalid"
 
# The choose_outfit function is defined by using the temperature description and the item_type inputted by the user.

# The clothing items and accessories are organized in the outfits dictionary by the temperature description and item type.
def choose_outfit(weather,item_type):

    outfits = {
        "cold": {
            "top": ["coat", "sweater","fleece"],
            "bottom": ["thermals", "jeans"],
            'accessory': ["gloves", "scarf", "beanie"]},
        "mild": {
            "top": ["flannel", "sweater","fleece"],
            "bottom": ["chinos", "jeans", "cargo pants"],
            "accessory": ["gloves", "sunglasses", "hat"]},
        "hot": {
            "top": ["t-shirt", "tank-top","hawaiian-shirt"],
            "bottom": ["shorts", "board-shorts"],
            "accessory": ["sunglasses", "sandals", "hat"]}}
            
# A statement to check the validity of the user inputs
    if weather not in outfits or item_type not in outfits[weather]:
        return "Invalid weather or item type input"
 
    outfit_item = random.choice(outfits[weather][item_type])

 #  A recommended outfit item is randomly selected for the appropriate temperature.
    return f"Recommended {item_type} for {weather} weather is: {outfit_item}"

item_type = input("Enter item type: top / bottom / accessory: ")

result = choose_outfit(temperature,item_type)

print(result)
