import os
import random
import shutil
import math

def is_image_file(dir_path, file):
    if os.path.isfile(os.path.join(dir_path, file)):
        splitted = file.split('.')
        if splitted[-1].lower() in ['jpg', 'png', 'svg', 'gif']:
            return True
        return False
    return False



def split_in_half(dir_path, backup_path):
    images = [f for f in os.listdir(dir_path) if is_image_file(dir_path, f)]
    
    random_indeces = random.sample(range(0, len(images) - 1), math.floor(len(images) / 2))
    
    if len(images) == 0:
        return False
    else:
        if len(images) == 1:
            random_indeces = [0]
        
        for index in random_indeces:
            if not os.path.isfile(os.path.join(backup_path, images[index])):
                shutil.move(os.path.join(dir_path, images[index]), os.path.join(backup_path, images[index]))
        return True
