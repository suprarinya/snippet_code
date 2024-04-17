import torch
from torch.utils.data import Dataset
from torch import nn
import numpy as np
from functions import *

class CustomDataset(Dataset):
    """
    create dataset from list 
    """
    def __init__(self, image_paths, labels) -> None:
        self.labels = torch.from_numpy(labels)
        self.image_paths = image_paths
        self.data = []
    
    def __len__(self):
        return len(self.image_paths)
    
    def __getitem__(self, idx):
        if not self.data:  # Preprocess images only on first access
            for image_path in self.image_paths:
                image = load_image(image_path=image_path)
                self.data.append(image)
        label = self.labels[idx]
        label_length = torch.tensor([len(label)])

        return self.data[idx], label, label_length
    
class CRNN(nn.Module):
    def __init__(self, vocab_size, hidden_size, num_layers):
        super(CRNN, self).__init__()
        # define CNN for feature extraction
        self.cnn = nn.Sequential(
            # 3 -> RGB, 1 -> greyscale
            nn.Conv2d(3, 32, kernel_size=3, padding=1),
            nn.ReLU(inplace=True),
            nn.MaxPool2d(2, 2)
            # more conv2d...
        )

        # define RNN for sequence prediction
        self.rnn = nn.LSTM(input_size=hidden_size, hidden_size=hidden_size, num_layers=num_layers, batch_first=True)
        # output layer for character probabilities
        self.fc = nn.Linear(hidden_size, vocab_size)
        # embedding layer (optional)
        # self.embedding = nn.Embedding(vocab_size, embedding_dim)
    
    def forward(self, x):
        # pass the image through CNN
        features = self.cnn(x)
        # reshape features for RNN input (reshape to (batch_size, seq_len, feature_dim))
        batch_size, channels, height, width = features.size()
        features = features.view(batch_size, width, -1)
        # optional, embed features before feeding to RNN
        # features = self.embedding(features)
        # pass features through RNN -> output : (batch_size, seq_len, hidden_size)
        outputs, (hidden, cell) = self.rnn(features)
        # use the last hidden state for prediction -> output from the last layer of RNN
        predictions = self.fc(hidden[-1])

        return predictions
    

