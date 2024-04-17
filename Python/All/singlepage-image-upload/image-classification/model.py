import os
import shutil
from sklearn.model_selection import train_test_split


def list_subfolders(dir):
    subfolders = [f.name for f in os.scandir(dir) if f.is_dir() and f.name not in ['test', 'train']]
    return subfolders

dataset_dir = "endo/kvasir-dataset/kvasir-dataset"
root_data_dir = "endo/kvasir-dataset/"
train_dir = os.path.join(root_data_dir, 'train')
test_dir = os.path.join(root_data_dir, 'test')

os.makedirs(train_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)

classes = list_subfolders(dataset_dir)
print(classes)
for class_name  in classes:
    os.makedirs(os.path.join(train_dir, class_name), exist_ok=True)
    os.makedirs(os.path.join(test_dir, class_name), exist_ok=True)

    class_dir = os.path.join(dataset_dir, class_name)
    images = [img for img in os.listdir(class_dir) if img.lower().endswith(('png','jpg','jpeg'))]
    train_imgs, test_imgs = train_test_split(images, test_size=0.2, random_state=42)
    
    # Copy training images to the training directory
    for img in train_imgs:
        src_path = os.path.join(class_dir, img)
        dst_path = os.path.join(train_dir, class_name, img)
        shutil.copy(src_path, dst_path)

    # Copy test images to the training directory
    for img in test_imgs:
        src_path = os.path.join(class_dir, img)
        dst_path = os.path.join(test_dir, class_name, img)
        shutil.copy(src_path, dst_path)

print("Dataset successfully split into training and test sets.")
