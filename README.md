# Dataset Split Calculator with Augmentation Control 🎛️

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://python.org)
[![Flask](https://img.shields.io/badge/Flask-2.0.1-lightgrey.svg)](https://flask.palletsprojects.com/)

A Python-based web application to calculate the initial split of a dataset into training, validation, and test sets, ensuring proper proportions after augmentation in Roboflow.
Try it on : https://robosplit.pythonanywhere.com/
## ✨ Key Features

- **Dynamic Augmentation Control**  
  Set any multiplier from 2× to 50× with direct numerical input
- **Professional Visualization**  
  Modern grid layout with color-coded percentages
- **Smart Validation**  
  Real-time input checks with error feedback
- **Precision Calculations**  
  Results rounded to 0.1% accuracy
- **Responsive Design**  
  Perfectly usable on desktop and mobile devices

## 🎨 New Modern Interface

Experience a professional-grade interface with:
- Clean minimalist design
- Interactive input fields
- Card-based result displays
- Color-coded percentages
- Smooth hover effects
- Enhanced readability

## 🚀 Quick Start

### Basic Usage
1. Input total dataset size
2. Set augmentation multiplier (default 3×)
3. Define target percentages
4. Get instant split calculations

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
