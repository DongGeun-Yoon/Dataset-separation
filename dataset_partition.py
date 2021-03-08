import os
import math
import random

# set your directory
data_path = 'D:/dataset/'
out_path = 'D:/dataset/'
valid_ratio = 0.2


name_list = os.listdir(data_path)
data_len = len(name_list)
valid_len = math.floor(data_len * valid_ratio)

valid_name = random.sample(name_list, valid_len)
train_name = [name for name in name_list if name not in valid_name]

with open(out_path + 'train_name.txt', 'w') as file:
    file.write('\n'.join(train_name))

with open(out_path + 'valid_name.txt', 'w') as file:
    file.write('\n'.join(valid_name))

print('DataSet partition done!')