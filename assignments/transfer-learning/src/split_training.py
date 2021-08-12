from numpy.random import choice
import cv2
import os


def train_val_holdout_split_images(root_path,
                                   n_images=350,
                                   train_ratio=0.7,
                                   validation_ratio=0.2,
                                   holdout_ratio=0.1,
                                   resize_size=(299, 299)):
    """
    Utility to split categorical training files organized by folder into
        training and testing, with resizing and max_images
    Args:
        root_path (str): folder containing category folders
        n_images (int): max number of images to copy
        train_ratio (float): ratio of images to copy to train folder
        validation_ratio(float): ratio of images to copy to validation folder
        holdout_ratio (float): ratio of images to copy to holdout folder
        resize_size (tuple(int, int)): size in pixels to resize copied images

    Returns:
        None
        """

    train_folder = root_path + '/data/train'
    validation_folder = root_path + '/data/validation'
    holdout_folder = root_path + '/data/holdout'

    for root, dirs, files in os.walk(root_path, topdown=False):
        i = 0
        for name in files:
            ext = name.split('.')[-1]
            if i < n_images and ext in ['jpg', 'png']:
                current_path = os.path.join(root, name)
                root_dir, category = os.path.split(root)
                val_split_dir = choice([train_folder,
                                        validation_folder,
                                        holdout_folder],
                                       1,
                                       p=[train_ratio,
                                           validation_ratio,
                                           holdout_ratio])[0]
                new_dir = os.path.join(val_split_dir, category)
                if not os.path.exists(new_dir):
                    os.makedirs(new_dir)
                new_path = os.path.join(new_dir, name)
                o_img = cv2.imread(current_path)
                new_img = cv2.resize(o_img, resize_size)
                cv2.imwrite(new_path, new_img)
                print(new_path, i)
                i += 1


train_val_holdout_split_images('/home/michael/g80/transfer-learning/food_data')
