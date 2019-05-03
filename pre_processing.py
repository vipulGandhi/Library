import os
import numpy as np

from tqdm import tqdm_notebook as tqdm

from keras.preprocessing import image
from keras.applications.vgg16 import preprocess_input as vgg16_preprocess_input
from keras.applications.vgg19 import preprocess_input as vgg19_preprocess_input
from keras.applications.xception import preprocess_input as xception_preprocess_input
from keras.applications.resnet50 import preprocess_input as resnet50_preprocess_input
from keras.applications.inception_resnet_v2 import preprocess_input as inception_resnet_v2_preprocess_input
from keras.applications.mobilenet import preprocess_input as mobilenet_preprocess_input
from keras.applications.inception_v3 import preprocess_input as inception_v3_preprocess_input



'''
The function takes image as input. It resize and preprocess(wrt. given model) the image. It generates keras redable numpy array of images and their corresponding class.

Input = Single folder containing images from different class/labels. The name of the image(s) is their class/label.

Output = numpy array from image file(s) - X_data
         Class/label of every element of image array - y_data
         
Note: I found creating empty numpy array and appending new image array to it - "np.concatenate((X_data, temp_image))" is computationally heavy. Instead I created an empty list, appended data to it- "X_data.append(temp_image)", later converted the list to np.array - "X_data = np.asarray(X_data)".

Condition: All images are contained in a single class. All image names are there respective class names.
'''
def generate_data(files, model_name, seperator = "_" , image_size = 224, image_name_contain_digits = False):
    
    # Create empty list
    X_data = []
    y_data = []
    
    for myFile in tqdm(files):
        # Load and resize image
        img = image.load_img(myFile, target_size=(image_size, image_size))
        # adds channels: x.shape = (image_size, image_size, 3) for RGB and (image_size, image_size, 1) for gray image
        temp_image = image.img_to_array(img)
        # Preprocess image wrt. given model
        temp_image = model_preprocesing(model_name, temp_image)
        # Append image tensor to list
        X_data.append(temp_image)
        
        # Get full file name
        filename_w_ext = os.path.basename(myFile)
        # remove extention from(eg. jpg/ png etc)
        filename, _ = os.path.splitext(filename_w_ext)
        # Replace seperators with ' '
        res_image = filename.replace(seperator, " ")
        # If name contains digits, remove them
        if(image_name_contain_digits):
            res_image = ''.join([i for i in res_image if not i.isdigit()])
        # Append name to list
        y_data.append(res_image)
    
    # Convert to array
    X_data = np.asarray(X_data)
    y_data = np.asarray(y_data)
    
    return X_data, y_data

""
def vgg16_preprocess_image(resized_image):
    preprocessed_image = vgg16_preprocess_input(resized_image)
    return preprocessed_image
    
def vgg19_preprocess_image(resized_image):
    preprocessed_image = vgg19_preprocess_input(resized_image)
    return preprocessed_image

def resnet50_preprocess_image(resized_image):
    preprocessed_image = resnet50_preprocess_input(resized_image)
    return preprocessed_image
    
def inception_v3_preprocess_image(resized_image):
    preprocessed_image = inception_v3_preprocess_input(resized_image)
    return preprocessed_image
    
def inception_resnet_v2_preprocess_image(resized_image):
    preprocessed_image = inception_resnet_v2_preprocess_input(resized_image)
    return preprocessed_image
    
def mobilenet_preprocess_image(resized_image):
    preprocessed_image = mobilenet_preprocess_input(resized_image)
    return preprocessed_image
    
def xception_preprocess_image(resized_image):
    preprocessed_image = xception_preprocess_input(resized_image)
    return preprocessed_image
    

my_model_preprocessing = {
    'vgg16_preprocess_image' : vgg16_preprocess_image,
    'vgg19_preprocess_image' : vgg19_preprocess_image,
    'resnet50_preprocess_image' : resnet50_preprocess_image,
    'inception_v3_preprocess_image' : inception_v3_preprocess_image,
    'inception_resnet_v2_preprocess_image' : inception_resnet_v2_preprocess_image,
    'mobilenet_preprocess_image' : mobilenet_preprocess_image,
    'xception_preprocess_image' : xception_preprocess_image
}

def model_preprocesing(model_name, input_image):
    selected_model = model_name + str("_preprocess_image")
    result = my_model_preprocessing[selected_model](input_image)
    return result