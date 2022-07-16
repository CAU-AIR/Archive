import os
from torch.utils.data import Dataset
from sklearn import preprocessing

def get_image_list(data_path):
    data_list = os.listdir(data_path)

    le = preprocessing.LabelEncoder()
    target = le.fit_transform(data_list)

    # return data_list
    return data_list, target
    