from functions import *
from classes import *
from torch.utils.data import DataLoader
from collections import deque
import torch

# prepare data
test_data, test_labels = get_keydataframe(filepath="IIIT5K/testdata.mat", key="testdata") 
train_data, train_labels = get_keydataframe(filepath="IIIT5K/traindata.mat", key="traindata") 

combined_labels = deque(train_labels)
combined_labels.extend(test_labels)

test_encode_labels = [one_hot_encode(label, combined_labels) for label in test_labels]
train_encode_labels = [one_hot_encode(label, combined_labels) for label in train_labels]

# the list maybe containing object, so detach and get only tensor
test_numpy_array = np.array([tensor.detach().numpy() for tensor in test_encode_labels])
train_numpy_array = np.array([tensor.detach().numpy() for tensor in train_encode_labels])

# create dataset
test_dataset = CustomDataset(image_paths=test_data, labels=test_numpy_array)
train_dataset = CustomDataset(image_paths=train_data, labels=train_numpy_array)

# check_dataset(test_dataset, train_dataset)

# print(test_dataset)
# # create dataloader
test_loader = DataLoader(test_dataset, batch_size=32, shuffle=False)
train_loader = DataLoader(train_dataset, batch_size=32, shuffle=True)

images, labels = next(iter(test_loader))
print(images.shape)

# number of unique character of train dataset (not test dataset!)
# vocab_size = get_vocab_size(train_dataset)
vocab_size = len(train_dataset)
# no need to use embedding -> only for text, token or chracter for input
# embedding_dim = 16
hidden_size = 128
num_layers = 2
epochs = 5

test_losses, test_accs = [], []
train_losses, train_accs = [], []

model = CRNN(vocab_size, hidden_size, num_layers)

loss_fn = torch.nn.CTCLoss()
optimizer = torch.optim.Adam(model.parameters(), lr=0.001)



for epoch in range(epochs): 
    train_loss, train_acc = train(
        model=model, 
        optimizer=optimizer, 
        loss_fn=loss_fn, 
        dataloader=train_loader
    )
    train_losses.append(train_loss)
    train_accs.append(train_acc)
    print(f"For epoch:{epoch}, Loss is {train_loss}, Accuracy is {train_acc}")

    test_loss, test_acc = train(
        model=model, 
        dataloader=train_loader,
        optimizer=optimizer, 
    )
    test_losses.append(train_loss)
    test_accs.append(train_acc)
    print(f"For epoch:{epoch}, Loss is {test_loss}, Accuracy is {test_acc}")


plot_graph(test_losses, train_losses, epochs)
plot_graph(test_accs, train_accs, epochs)





