# Yelp Image Classifier

## Project Overview

The Yelp Image Classifier project aims to categorize images from Yelp into distinct categories, facilitating better organization and accessibility of visual content on the platform. This project is structured around two primary tasks:

1. **Label Classification:** Classify images into one of five distinct labels: Food, Drinks, Outside, Inside, Menu. This is a single-label image classification problem.
2. **Business Classification:** Assign multiple labels to images, representing different business categories based on the visual content. This is a multi-label classification problem.

## Dataset

The data for this project comes from the Yelp dataset, comprising business and photo JSON files. The business JSON includes fields like business ID, name, and categories, while the photo JSON contains photo IDs, business IDs, and labels.

## Methodology

### Task 1: Label Classification
- A custom CNN model and pre-trained models like VGG16 and ResNet18 were used.
- The models were fine-tuned to classify images into the specified five labels.

### Task 2: Business Classification
- A custom CNN model was designed for multi-label classification.
- Pre-trained VGG16 and ResNet18 models were also adapted for this task.

## Results

The project demonstrated high accuracy in classifying images into the specified categories. VGG16 showed superior performance in label classification, while the custom CNN model excelled in business classification.

## Future Directions

The project identifies potential areas for improvement such as computational resource optimization, dataset balancing, addressing incorrect labeling, and enhancing model convergence for multi-label classification.

## Usage and Contribution

This repository contains the code, dataset links, and documentation for the Yelp Image Classifier project. Contributors can explore the models, experiment with different configurations, and potentially enhance the classifier's performance and applicability to other datasets.
