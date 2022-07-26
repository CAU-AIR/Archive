import os
import cv2
from cv2 import transform
from numpy import imag
import torch
from sklearn import preprocessing
from torch.utils.data import Dataset
from avalanche.benchmarks.utils import (
    AvalancheDataset,
    PathsDataset,
    common_paths_root,
)
from avalanche.benchmarks.utils.dataset_definitions import IDataset
from tqdm import trange

def get_image_list(data_path):
    image = []
    label = []

    data_list = os.listdir(data_path)
    le = preprocessing.LabelEncoder()
    target = le.fit_transform(data_list)

    for idx, folder in enumerate(data_list):
        folder_name = os.path.join(data_path, folder)
        folder_list = os.listdir(folder_name)
        for image_name in folder_list:
            img_name = os.path.join(folder_name, image_name)
            image.append(img_name)
            label.append(target[idx])

    return image, label

def dataset_list(x_data, y_data):
    dataset = []
    file_list = []

    for idx, data in enumerate(x_data):
        instance_tuple = (data, y_data[idx])
        file_list.append(instance_tuple)

    dataset.append(file_list)

    return dataset

class ImageDataset(IDataset):
    def __init__(self, image_list, label_list):
        self.image_list = image_list
        self.lable_list = label_list

    def __len__(self):
        return len(self.lable_list)

    def __getitem__(self, idx):
        image = cv2.imread(self.image_list[idx], cv2.IMREAD_COLOR)
        image = torch.tensor(image).float()

        target = self.lable_list[idx]
        target = torch.tensor(target).float()

        return image, target

def PathDataset(dataset, transfrom, mode):
    for exp_id, list_of_files in enumerate(dataset):
        common_root, exp_paths_list = common_paths_root(list_of_files)
        paths_dataset = PathsDataset(common_root, exp_paths_list)
        stream_datasets = AvalancheDataset(paths_dataset, transform_groups=transfrom, initial_transform_group=mode)

    return stream_datasets
    
