import json
import csv
from collections import Counter, defaultdict
from nltk.corpus import stopwords
import string
from tqdm import tqdm  # Import tqdm for progress bar

# Function to clean caption and remove stop words and symbols
def clean_caption(caption):
    stop_words = set(stopwords.words('english'))
    symbols = set(string.punctuation)
    words = caption.lower().split()
    cleaned_words = [word for word in words if word not in stop_words and word not in symbols]
    return cleaned_words

# Read JSON data and process each JSON object
with open('photos.json', 'r') as file:
    data = [json.loads(line.strip()) for line in file]

# Initialize a defaultdict to store businesses and their associated photos
business_photos = defaultdict(list)

# Initialize counters for words in each label category
label_words = defaultdict(Counter)

# Process each photo in the JSON data
for photo in data:
    business_id = photo['business_id']
    label = photo['label']
    caption = photo['caption']
    
    # Clean the caption
    cleaned_caption = clean_caption(caption)
    
    # Update the counter for label words
    label_words[label].update(cleaned_caption)
    
    # Store the photo ID with the corresponding business
    business_photos[business_id].append(photo['photo_id'])

# Get the top 5 words for each label category, based on total count of occurrences
top_choices = {label: word_counter.most_common(5) for label, word_counter in label_words.items()}

# Write results to CSV file with progress bar
with open('business_photos_full.csv', 'w', newline='') as csvfile:
    fieldnames = ['label', 'top_choice', 'business_id', 'photo_id']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    
    # Initialize progress bar
    total_photos = sum(len(photos) for photos in business_photos.values())
    progress_bar = tqdm(total=total_photos, desc="Generating CSV", unit=" photo")

    # Process each business
    for business_id, photos in business_photos.items():
        # Process each photo of the business
        for photo_id in photos:
            # Check if any of the top choices for the label exist in the photo's caption
            for label, choices in top_choices.items():
                caption_words = clean_caption(next(photo['caption'] for photo in data if photo['photo_id'] == photo_id))
                if any(choice in caption_words for choice, _ in choices):
                    for choice, _ in choices:
                        writer.writerow({'label': label, 'top_choice': choice, 'business_id': business_id, 'photo_id': photo_id})
            progress_bar.update(1)  # Update progress bar

    progress_bar.close()  # Close progress bar

print("Results have been written to 'business_photos_full.csv'.")

# Read the CSV file
top_choices_counts = defaultdict(Counter)
with open('business_photos_full.csv', 'r', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        label = row['label']
        top_choice = row['top_choice']
        business_id = row['business_id']
        photo_id = row['photo_id']
        
        # Update the counter for top choices
        top_choices_counts[label][top_choice] += 1

# Print the occurrences of each top choice
print("Occurrences for each top choice:")
for label, choices_counter in top_choices_counts.items():
    print(f"\nTop choices for {label.capitalize()} category:")
    for choice, count in choices_counter.items():
        print(f"  {choice}: {count} occurrences")