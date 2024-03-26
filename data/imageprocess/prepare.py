import os
import requests
from PIL import Image
import numpy as np

# Function to download and save image
def download_image(url, filename):
    response = requests.get(url)
    with open(filename, 'wb') as f:
        f.write(response.content)

# Example image URLs
image_urls = [
    'https://i.natgeofe.com/n/548467d8-c5f1-4551-9f58-6817a8d2c45e/NationalGeographic_2572187_square.jpg',
    'https://upload.wikimedia.org/wikipedia/commons/thumb/1/15/Cat_August_2010-4.jpg/1200px-Cat_August_2010-4.jpg',
    # Add more image URLs as needed
]

# Download and save images
for i, url in enumerate(image_urls):
    filename = f'image_{i}.jpg'
    download_image(url, filename)

# Process images
for i in range(len(image_urls)):
    filename = f'image_{i}.jpg'
    img = Image.open(filename)
    # Perform image processing tasks here (e.g., resize, convert to numpy array, etc.)
    # Example:
    img_resized = img.resize((224, 224))  # Resize image to 224x224
    img_array = np.array(img_resized)  # Convert image to numpy array
    # Further processing can be done here
