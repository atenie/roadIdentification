import os
import cv2
import numpy as np

# filename lists
marking_masks = []
marking_images = []

# necessary counter
i = 0

# Mask input image with binary mask
# RGB, but order is BGR
marking_color = np.array([0, 0, 255])
road_color = np.array([32, 32, 64])
obstacle_color = np.array([102, 255, 0])
bg_color = np.array([96, 128, 128])
bonnet_color = np.array([255, 0, 204])

for (path, dirnames, filenames) in os.walk('imgs'):
    marking_images.extend(os.path.join(path, name) for name in filenames)

for (path, dirnames, filenames) in os.walk('masks'):
    marking_masks.extend(os.path.join(path, name) for name in filenames)

for name in marking_images:
    # Load image, create mask, and draw white circle on mask
    image_name = name
    mask_name = marking_masks[i]

    image = cv2.imread(image_name)
    mask = cv2.imread(mask_name)

    # mask, upper bound, lower bound

    marking_mask = cv2.inRange(mask, marking_color, marking_color)
    road_mask = cv2.inRange(mask, road_color, road_color)
    obstacle_mask = cv2.inRange(mask, obstacle_color, obstacle_color)
    bg_mask = cv2.inRange(mask, bg_color, bg_color)
    bonnet_mask = cv2.inRange(mask, bonnet_color, bonnet_color)

    # logical and on images
    marking_result = cv2.bitwise_and(image, image, mask=marking_mask)
    road_result = cv2.bitwise_and(image, image, mask=road_mask)
    obstacle_result = cv2.bitwise_and(image, image, mask=obstacle_mask)
    bg_result = cv2.bitwise_and(image, image, mask=bg_mask)
    bonnet_result = cv2.bitwise_and(image, image, mask=bonnet_mask)

    #save name
    marking_name = ".\\marking\\"+str(i)+".png"
    road_name = ".\\road\\"+str(i)+".png"
    obstacle_name = ".\\obstacle\\"+str(i)+".png"
    bg_name = ".\\bg\\"+str(i)+".png"
    bonnet_name = ".\\bonnet\\"+str(i)+".png"

    #write to file
    cv2.imwrite(marking_name, marking_result)
    cv2.imwrite(road_name, road_result)
    cv2.imwrite(obstacle_name, obstacle_result)
    cv2.imwrite(bg_name, bg_result)
    cv2.imwrite(bonnet_name, bonnet_result)

    #increment
    i=i+1
