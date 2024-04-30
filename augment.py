import os
from PIL import Image
import random
import re
import sys

data_path = 'data/archive/compressed_dataset/' # change this according to where you put your data

def random_crop(image):
    width, height = image.size
    left = random.randint(0, width // 2)
    top = random.randint(0, height // 2)
    right = random.randint(width // 2 + 300, width)
    bottom = random.randint(height // 2 + 300, height)
    return image.crop((left, top, right, bottom))

def augment_images():
    new_data_count = 0
    for country in os.listdir(data_path):
        country_path = os.path.join(data_path, country)
        if len(os.listdir(country_path)) < 20:
            images = []
            for img in os.listdir(country_path):
                img_path = os.path.join(country_path, img)
                base = Image.open(img_path)
                images.append(base)
            
            for base in images:
                flipped = base.transpose(Image.FLIP_LEFT_RIGHT)
                flipped.save(country_path + '/' + str(new_data_count) + '.jpg')
                new_data_count += 1

                for i in range(4):
                    cropped = random_crop(base)
                    cropped_flipped = random_crop(flipped)
                    cropped.save(country_path + '/' + str(new_data_count) + '.jpg')
                    new_data_count += 1
                    cropped_flipped.save(country_path + '/' + str(new_data_count) + '.jpg')
                    new_data_count += 1

    print('finished augmenting data. Generated', new_data_count, 'new images')

def deaugment_images():
    pattern = re.compile(r"^\d+\.jpg$")
    count = 0
    for country in os.listdir(data_path):
        country_path = os.path.join(data_path, country)
        for img in os.listdir(country_path):
            if pattern.match(img):
                file_path = os.path.join(country_path, img)
                if os.path.isfile(file_path):
                    # print(file_path)
                    os.remove(file_path)
                    count += 1
    print('finished deaugmenting data. Deleted', count, 'files')

def main():
    args = sys.argv[1:]
    if len(args) == 0:
         print('NO ARGUMENTS GIVEN. GIVE ARG \'augment\' TO AUGMENT THE DATASET AND \'deaugment\' TO DE-AUGMENT THE DATASET')
         return
    
    if args[0] == 'augment':
        print('augmenting the dataset... (this may take a few seconds)')
        augment_images()
    elif args[0] == 'deaugment':
        print('de-augmenting the dataset... (this may take a few seconds)')
        deaugment_images()
    else:
        print('INCORRECT ARGUMENTS GIVEN. GIVE ARG \'augment\' TO AUGMENT THE DATASET AND \'deaugment\' TO DE-AUGMENT THE DATASET')

main()