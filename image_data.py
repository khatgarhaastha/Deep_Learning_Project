# import restaurant_photos.csv
# create numpy arrays of pixle data fron the images in 
# photos file corresponsding to the photo id in restaurant_photos.csv

import pandas as pd
import numpy as np
import os
from PIL import Image
from tqdm import tqdm

# read CSV file
#image_df = pd.read_csv('Data/restaurant_photos.csv')
chunksize = 1000  # Adjust as needed
for chunk in pd.read_csv('Data/restaurant_photos.csv', chunksize=chunksize):
    process(chunk)  # Replace with your processing logic


# directory where the .npy files will be saved
npy_imge_dir = 'Data/npy_images'
os.makedirs(npy_imge_dir, exist_ok=True)

# Initialize tqdm for the DataFrame iteration
for index, row in tqdm(image_df.iterrows(), total=image_df.shape[0], desc="Processing images"):
    img_path = os.path.join('Data/yelp_photos/photos/', row['photo_id'] + '.jpg')
    npy_path = os.path.join(npy_imge_dir, row['photo_id'] + '.npy')
    
    if os.path.exists(img_path):
        img = Image.open(img_path)
        img = img.resize((128, 128))  # Resize the image
        img_array = np.array(img)  # Convert image to numpy array
        np.save(npy_path, img_array)  # Save numpy array to .npy file
        # Store the path to the .npy file in the DataFrame
        image_df.at[index, 'npy_path'] = npy_path

# Save the updated DataFrame with paths to .npy files
image_df.to_csv('Data/restaurant_photos_with_npy.csv', index=False)

'''
# Process each image
for index, row in image_df.iterrows():
    print(f"Processing image {index+1}/{len(image_df)}: {row['photo_id']}.jpg")  # Progress indication
    img_path = os.path.join('Data/yelp_photos/photos/' + row['photo_id'] + '.jpg')
    npy_path = os.path.join(npy_imge_dir, row['photo_id'] + '.npy')
    if os.path.exists(img_path):
        img = Image.open(img_path)
        img = img.resize((128, 128))
        img = np.array(img)
        np.save(npy_path, img)
        # Store the path to the .npy file in the dataframe
        image_df.at[index, 'npy_path'] = npy_path
        print(f"Saved {row['photo_id']}.npy to {npy_path}")  # Confirmation of save

# Save the dataframe with the .npy paths
image_df.to_csv('Data/restaurant_photos_with_npy.csv', index=False)
print("All images processed and DataFrame updated.")


'''
