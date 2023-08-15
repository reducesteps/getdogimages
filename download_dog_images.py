import requests
import os
from datetime import datetime

# Define the URL to fetch random dog images
url = 'https://random.dog/woof.json'

# Define the directory to save the images
save_dir = 'dogpics'

# Create the directory if it does not exist
os.makedirs(save_dir, exist_ok=True)

# Function to download and save a dog image
def download_dog_image():
    response = requests.get(url)
    data = response.json()
    image_url = data['url']
    
    # Generate a filename based on the current date and time
    filename = datetime.now().strftime('%Y-%m-%d_%H-%M-%S') + '.' + image_url.split('.')[-1]
    
    # Save the image in the specified directory
    with open(os.path.join(save_dir, filename), 'wb') as file:
        image = requests.get(image_url)
        file.write(image.content)
    print(f'Image saved as {filename}')

# Download a random dog image
download_dog_image()
