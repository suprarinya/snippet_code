from scipy.io import loadmat
import numpy as np
import pandas as pd
import cv2
from collections import deque, Counter
import matplotlib.pyplot as plt
import torch
from PIL import Image
from torchvision import transforms


def get_keydataframe(filepath:str, key:str):
    """
        prepare data and label from .mat file
        Returns: list of image paths and words
    """
    mat = loadmat(filepath)
    data = np.array(mat[key])
    totalcount = len(data[0])
    images, labels = [], []
    for i in range(totalcount):
        groundtruth, imgname = data['GroundTruth'][0][i][0], 'IIIT5K/'+data['ImgName'][0][i][0]
        if groundtruth: labels.append(groundtruth)
        if imgname: images.append(imgname)
    return images, labels

def get_vocab_size(labels):
    """
        Calculates the number of unique characters in the labels.
        Args: labels: A list of strings representing character sequences.
        Returns: int: The number of unique characters in the labels.
    """
    unique_chars = set()
    for label in labels:
        for char in label:
            unique_chars.add(char)
    return len(unique_chars)

def load_image(image_path):
    """
        Loads an image from a given path and converts it to a NumPy array.
        Args: image_path: String representing the path to the image file.
        Returns: numpy.ndarray: The image data as a NumPy array.
    """
    # image = cv2.imread(image_path)
    # new_size = (256, 256)
    # if image is None:
    #     raise ValueError(f"Failed to load image: {image_path}")
    # image = cv2.resize(image, new_size)
    # image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    # return image.astype(np.float32)

    image = Image.open(image_path).convert('RGB')
    transform = transforms.Compose([
        transforms.Resize((256, 256)),
        transforms.ToTensor()
    ])
    image = transform(image)
    return image


def one_hot_encode(label, all_labels):
    vocab_size = len(all_labels)
    word_to_index = {word:i for i, word in enumerate(all_labels)} # map word to index
    index_to_word = {i:word for i, word in enumerate(all_labels)} # map index to word
    # Convert a word label to a one-hot encoded vector
    one_hot = torch.zeros(vocab_size)
    one_hot[word_to_index[label]] = 1.0
    return one_hot

def check_dataset(train_dataset, test_dataset):
    test_sample, test_label = test_dataset[0]
    train_sample, train_label = train_dataset[0]
    # check dataset length && sample
    print(f"Number of training samples: {len(train_dataset)}, Sample type: {type(test_sample)}, label type: {type(test_label)}")
    print(f"Number of testing samples: {len(test_dataset)}, Sample type: {type(train_sample)}, label type: {type(train_label)}")
    # visualize samples from the dataset
    visualize_sample(train_dataset, 0)
    visualize_sample(test_dataset, 0)
    # check saple data type


def visualize_sample(dataset, index):
    sample, label = dataset[index]
    print("Data type:", sample.dtype)
    print("Min value:", np.min(sample))
    print("Max value:", np.max(sample))

    # Normalize if needed
    # if sample.dtype == np.float32 or sample.dtype == np.float64:
    #     sample = sample - np.min(sample)  # Shift to 0
    #     sample = sample / np.max(sample)  # Normalize to 1

    plt.imshow(sample.astype(np.uint8))  
    plt.title(f"Label: {label}")
    plt.show()

def train(model, optimizer, loss_fn, dataloader, device="cpu"):
    """
        Train CRNN model
        Args:
            model: CRNN model instance
            optimizer: optimizer 
            loss: Loss function 
            dataloader: dataloader
            num_epochs: number of training epochs
            device: cpu or gpu
    """
    model.train()
    train_loss, train_acc = 0, 0
    for images, labels, label_lengths in dataloader:

        images, labels = images.to(device), labels.to(device)

        optimizer.zero_grad()

        outputs = model(images)
        output_lengths = torch.full((outputs.size(1),), outputs.size(0), dtype=torch.long, device=device)

        loss = loss_fn(outputs, labels, output_lengths, label_lengths)
        loss.backward()
        optimizer.step()

        train_loss += loss.item()

        # # forward pass
        # y_pred = model(X)
        # # calc loss
        # loss = loss_fn(y_pred, y)
        # train_loss += loss.item()
        # # optimize zero grad
        # optimizer.zero_grad()
        # # loss backward
        # loss.backward()
        # # optimizer step
        # optimizer.step()

        # # calc accuracy across all batches
        # y_pred_class = torch.argmax(torch.softmax(y_pred, dim=1), dim=1)
        # train_acc += (y_pred_class == y).sum().item() / len(y_pred)
    
    # get train_loss and train_acc per batch
    train_loss = train_loss / len(dataloader)
    train_acc = train_acc / len(dataloader)
    return train_loss, train_acc

def test(model, dataloader, loss_fn, device='cpu'):
    """
    test model
    Args:
        model: CRNN model instance
        loss: Loss function 
        dataloader: dataloader
    """
    model.eval()
    test_loss = 0
    test_acc = 0
    with torch.inference_mode():
        for images, labels, label_lengths in dataloader:
            images, labels = images.to(device), labels.to(device)

            outputs = model(images)
            output_lengths = torch.full((outputs.size(1),), outputs.size(0), dtype=torch.long, device=device)

            loss = loss_fn(outputs, labels, output_lengths)
            test_loss += loss.item()
            # calc accuracy across all batches
            y_pred_class = torch.argmax(torch.softmax(outputs, dim=1), dim=1)
            test_acc += (y_pred_class == labels).sum().item() / len(outputs)

        # get train_loss and train_acc per batch
        test_loss = test_loss / len(dataloader)
        test_acc  = test_acc / len(dataloader)
    return test_loss, test_acc

def plot_graph(test_data, train_data, epochs):
    plt.plot(range(epochs), train_data, label="Train loss")
    plt.plot(range(epochs), test_data, label="Test loss")
    plt.xlabel('Epochs')
    plt.ylabel('Loss')
    plt.title('Training and Test Loss Over Epochs')
    plt.legend()
    plt.show()





    # for images, labels in dataloader:
    #     images, labels = images.to(device), labels.to(device)
    #     outputs = model(images)
    #     loss = loss_fn(outputs, labels)
    #     optimizer.zero_grad()
    #     loss.backward()
    #     optimizer.step()
    #     running_loss += loss.item()
        











# img = load_image('IIIT5K/test/1_1.png')
# img_uint8 = img.astype(np.uint8)
# print(img_uint8, img_uint8.dtype)
# plt.imshow(img_uint8)  
# plt.show()
