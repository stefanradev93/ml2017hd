'''
This script creates a validation split of maxNum instances per class (min. minNum if class is rare) using the image filepath and rating filepath.
'''

from shutil import copyfile
import os
import numpy as np

img_path = '../project/all_females_combined'
rating_path = './ratings_s_combined.txt'
save_path_val = '../project/eval_data/all_females_combined_val_s'
save_path_train = '../project/eval_data/all_females_combined_train_s'
maxNum = 7
minNum = 1

if not os.path.isdir(save_path_val):
    os.makedirs(save_path_val)

if not os.path.isdir(save_path_train):
    os.makedirs(save_path_train)

orig_ratings = np.genfromtxt(rating_path)
rounded_ratings = np.round(orig_ratings, 0).astype(np.int8)

# Move all images according to ratings
orig_images = sorted(os.listdir(img_path))
assert len(rounded_ratings) == len(orig_images)

perm_ratings = np.random.permutation(len(rounded_ratings))

images = np.array(orig_images)[perm_ratings]
ratings = rounded_ratings[perm_ratings]

np.unique(ratings)

selected_img = [[] for i in np.unique(ratings)]
train_img = [[] for i in np.unique(ratings)]

unique, count = np.unique(ratings, return_counts=True)

for i,r in zip(images,ratings):
    if len(selected_img[r]) < maxNum and count[r] >= 10*maxNum:
        selected_img[r].append(i)
    elif len(selected_img[r]) < maxNum and count[r] < 10*maxNum:
        #use fewer images for this class
        classMaxNum = count[r] // 10
        if classMaxNum < minNum:
            classMaxNum = minNum #we want at least minNum images per class
        if len(selected_img[r]) < classMaxNum:
            selected_img[r].append(i)
        else:
            #put image in train set
            train_img[r].append(i)
    else:
        #put image in train set
        train_img[r].append(i)

text_file = open(save_path_val + "/val_ratings.txt", "w")
#make sure all selected ratings are correct
save_ratings = []
for r,sub in enumerate(selected_img):
    for img in sub:
        idx = orig_images.index(img)
        assert(rounded_ratings[idx] == r)
        #move selected_img to separate folder & create corresponding val_ratings.txt
        copyfile(img_path + "/" + img,save_path_val + "/" + str(orig_ratings[idx]) + "_" + img) #copy rating into filename to ensure correct order
        save_ratings.append(str(orig_ratings[idx]))
save_ratings.sort()
for r in save_ratings:
    text_file.write(r + "\n")
text_file.close()

#do the same for train set
text_file = open(save_path_train + "/train_ratings.txt", "w")
#make sure all selected ratings are correct
save_ratings = []
for r,sub in enumerate(train_img):
    for img in sub:
        idx = orig_images.index(img)
        assert(rounded_ratings[idx] == r)
        #move selected_img to separate folder & create corresponding train_ratings.txt
        copyfile(img_path + "/" + img,save_path_train + "/"+ str(orig_ratings[idx]) + "_" + img)
        save_ratings.append(str(orig_ratings[idx]))
save_ratings.sort()
for r in save_ratings:
    text_file.write(r + "\n")
text_file.close()
