import os
import math

import image_helpers


dir_path = input('Enter your directory path\n')
backup_path = os.path.join(dir_path, 'backup')

backup_path = os.path.join(dir_path, 'backup')

if not os.path.exists(backup_path):
    os.mkdir(backup_path)

has_images = True

while has_images:
    has_images = image_helpers.split_in_half(dir_path, backup_path)
