# Read business_restaurant.csv file
# extracts photoids from photos.json corresponding to business id in business_restaurant.csv
# create a new json file with the following fields busines id, image id, labels
# labels are extracted from the image labels file
# Output: restaurant_photos.csv

import json
import csv
import os
import pandas as pd
import numpy as np
import re
from tqdm import tqdm # for progress bar

# Read business_restaurant.csv file
print("Loading business_restaurant.csv...")
business_restaurant = pd.read_csv('Data/business_restaurant.csv')

# Load the photo data from the JSON file
print("Loading photos.json...")

photo_data = []
with open('Data/yelp_photos/photos.json') as f:
    for line in f:
        photo_data.append(json.loads(line))
photos_df = pd.DataFrame(photo_data)

# filter the photos_df to only include the business ids in business_restaurant.csv
print("Filtering photos based on business IDs...")
filtered_photos_df = photos_df[photos_df['business_id'].isin(tqdm(business_restaurant['business_id'], desc="Filtering"))]
#photos_df = photos_df[photos_df['business_id'].isin(business_restaurant['business_id'])]

# export the photos_df to a csv file
print("Exporting to restaurant_photos.csv...")
filtered_photos_df.to_csv('restaurant_photos.csv', index=False)

print("Done!")