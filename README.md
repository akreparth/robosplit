# Dataset Split Calculator

A Python-based web application to calculate the initial split of a dataset into training, validation, and test sets, ensuring proper proportions after augmentation in Roboflow.

## Features
- **Input Customization**: Specify total dataset size and desired split percentages.
- **Augmentation Support**: Automatically accounts for training set augmentation (3x multiplier).
- **Web Interface**: Easy-to-use form for input and clear results display.

## Usage

### Input Requirements
1. **Total Dataset Size**: Number of images in your original dataset.
2. **Desired Split Percentages**:
   - Training (% after augmentation)
   - Validation (%)
   - Test (%)

### Example
For a dataset of **151 images** with a desired split of **70-20-10**:
- **Original Split**:
  - Training: 66 images
  - Validation: 57 images
  - Test: 28 images
- **After Augmentation**:
  - Training: 198 images (70%)
  - Validation: 57 images (20%)
  - Test: 28 images (10%)
