from imgstitch.stitch_images import stitch_images, stitch_images_and_save
import matplotlib.pyplot as plt
import os
import cv2
import time

print('Stitching images...')


image_folder = 'test/'
image_filenames = ['scene1_a.jpeg', 'scene1_b.jpeg', 'scene1_c.jpeg']


#direction of stitching. Uses numpy convention. 
# Use 0 for stitching along image height or vertical stitching. 
# And use 1 for stitching along image width or horizontal stitching.
stitch_direction = 1

stitched_images = stitch_images(image_folder, image_filenames, stitch_direction)

# BGR to RGB
stitched_images = cv2.cvtColor(stitched_images, cv2.COLOR_BGR2RGB)

plt.imshow(stitched_images)
plt.show()


#Dataset is not working because of the confidence threshold
image_folder = 'isiqa_release/constituent_images/1/'
image_filenames = ['2.jpg', '3.jpg', '4.jpg']
stitch_direction = 1

stitched_images = stitch_images(image_folder, image_filenames, stitch_direction)

# BGR to RGB
stitched_images = cv2.cvtColor(stitched_images, cv2.COLOR_BGR2RGB)

plt.imshow(stitched_images)
plt.show()