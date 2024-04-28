import os
import numpy as np
from PIL import Image
from torchvision import transforms

def resize_images_in_directory(input_dir, output_file, target_size=(64, 148)):
    transform = transforms.Resize(target_size)
    for i, folder in enumerate(os.listdir(os.getcwd() + '/' + input_dir)):
        print(folder, i)
        country_images = []
        try:
            for i, filename in enumerate(os.listdir(os.getcwd()+'/' +input_dir + '/' + folder)):
                image_path = (os.getcwd() +'/'+ input_dir+'/'+ folder+'/'+ filename)
                with Image.open(image_path) as img:
                    img = img.convert("RGB")
                    img = transform(img)
                    data_transposed = np.transpose(np.array(img), (2, 0, 1))
                    country_images.append(data_transposed)

            output_path = os.path.join(output_file, folder + '.npy')
            # os.mkdir(output_path)
            np.save(output_path, country_images)
        except Exception as e:
            print(e)

    print(f"Resized images saved to {output_file}")

input_directory = "/geoguessr_filtered_data"
output_file = "resized_countries"
resize_images_in_directory(input_directory, output_file)
