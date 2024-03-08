# Initially we have actual photos (n number), the name of the photo is the photo id
# we have a photo jason have photo id, business id, label
# we have a business jason file having business id and categories


'''
we have 4 labels in the photos json i.e. Food, Drinks, Outdside, Inside
For business json in the category field we have to extract every category 
and also first we have to extract only the restaurant business and the 
images corresponding to those restaurants only

We have to create a new json file with the following fields busines id, image id, labels, ctageories
what we are trying to acomplish is that we will have photos 
we will try to predict the categories for the business that 
can be associated with that photo

'''

import pandas as pd
import json
import csv

json_path = 'data/yelp_academic_dataset_business.json'
csv_path = 'data/business_restaurant.csv'

# reading the json file
data = []
with open(json_path, 'r') as f:
    for line in f:
        business = json.loads(line)
        print(business.get('categories', ''))
        if business.get('categories', '') and 'Restaurants' in business.get('categories', ''):
            # Directly filter and append restaurant businesses
            data.append(business)

# Specify the columns you want to include in your CSV
csv_columns = ['business_id', 'categories']

with open(csv_path, 'w', newline='') as csvfile:  # Ensuring correct line handling
    writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
    writer.writeheader()
    for restaurant in data:
        # Extracting only the required fields for each restaurant
        row = {col: restaurant[col] for col in csv_columns}
        writer.writerow(row)

print("CSV file has been created successfully.")














# to do

# figure out what we need in our final dataset dor the images
# colums should be image in any form, iange id, business id , multiple labels 
# figure out how to handle the labels if we have too many of them

# define main function add pass to it 