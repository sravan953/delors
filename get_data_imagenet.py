#!/usr/bin/env python
__author__ = "Vineet Bhombore, Keerthi Sravan Ravi"

import urllib.request
import cv2
import numpy as np
import os


def get_images():
    # URLs of ImageNet categories of interest
    all_categories = {'animals':'http://image-net.org/api/text/imagenet.synset.geturls?wnid=n02512053',
        'artefact':'http://image-net.org/api/text/imagenet.synset.geturls?wnid=n00021939',
        'flora':'http://image-net.org/api/text/imagenet.synset.geturls?wnid=n00017222',
        'fungus':'http://image-net.org/api/text/imagenet.synset.geturls?wnid=n12992868',
        'geo':'http://image-net.org/api/text/imagenet.synset.geturls?wnid=n09287968',
        'people':'http://image-net.org/api/text/imagenet.synset.geturls?wnid=n00007846',
        'sports':'http://image-net.org/api/text/imagenet.synset.geturls?wnid=n00523513'}

    for cat in all_categories.keys():
        cat_url = all_categories[cat]
        all_image_urls = urllib.request.urlopen(cat_url).read().decode()

        # Create directory if it does not already exist
        if not os.path.exists(cat):
            os.makedirs(cat)

        num_of_pics = len(all_image_urls.split())
        print("Downloading {} pictures from \'{}\' category...".format(num_of_pics, cat))
        for pic_index, _image_url in enumerate(all_image_urls.split('\n')):
            try:
                urllib.request.urlretrieve(_image_url, cat + "/" + str(pic_index) + ".jpg")
                img = cv2.imread(cat + "/" + str(pic_index) + ".jpg", cv2.IMREAD_GRAYSCALE)
                resized_image = cv2.resize(img, (128, 128)) # should be larger than samples / pos pic (so we can place our image on it)
                cv2.imwrite(cat + "/" + str(pic_index) + ".jpg", resized_image)

            except Exception as e:
                print(str(e))

# Run the function
get_images()
