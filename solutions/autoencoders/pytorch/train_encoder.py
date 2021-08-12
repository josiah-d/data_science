import torch, sys, os, argparse, time
from torch import nn
import numpy as np
from torchvision import datasets
import torchvision.transforms as transforms
# import our class
sys.path.append("./src")
from autoencoder import Embedding

def create_data_itterators(num_workers, batch_size):
    # convert data to torch.FloatTensor
    transform = transforms.ToTensor()

    # choose the training and test datasets
    train_data = datasets.MNIST(
        root='data', 
        train=True,
        download=True, 
        transform=transform)

    test_data = datasets.MNIST(
        root='data', 
        train=False,
        download=True, 
        transform=transform)

    # prepare data loaders
    train_loader = torch.utils.data.DataLoader(
        train_data, 
        batch_size=batch_size,
        num_workers=num_workers)

    test_loader = torch.utils.data.DataLoader(
        test_data, 
        batch_size=batch_size, 
        num_workers=num_workers)
    
    return train_loader, test_loader

def model_settup(embedding_dim, learning_rate):
    # initialize the NN
    model = Embedding(embedding_dim=embedding_dim)
    print(model)

    ## Specify loss and optimization functions
    # specify loss function
    criterion = nn.L1Loss()

    # specify optimizer
    optimizer = torch.optim.SGD(model.parameters(), lr=learning_rate, momentum=0.01)    
    return model, criterion, optimizer

def train_model(model, optimizer, criterion, n_epochs, train_loader):
    model.train() # prep model for training
    for epoch in range(n_epochs):
        epoch_start = time.time()
        # monitor training loss
        train_loss = 0.0
        
        ###################
        # train the model #
        ###################    
        for data, target in train_loader:
            # clear the gradients of all optimized variables
            optimizer.zero_grad()
            # forward pass: compute predicted outputs by passing inputs to the model
            output = model(data)
            target_unfolded = data.view(-1, 28 * 28)
            # calculate the loss
            loss = criterion(output, target_unfolded)
            # backward pass: compute gradient of the loss with respect to model parameters
            loss.backward()
            # perform a single optimization step (parameter update)
            optimizer.step()
            # update running training loss
            train_loss += loss.item()*data.size(0)
            
        # print training statistics 
        # calculate average loss over an epoch
        train_loss = train_loss/len(train_loader.dataset)

        print('Epoch: {} \tTraining Loss: {:.6f}'.format(
            epoch+1, 
            train_loss
            ))
        print("\ttime for epoch: {}".format(epoch_start-time.time()))

def test_model(model, criterion, test_loader):
    # initialize lists to monitor test loss and accuracy
    test_loss = 0.0
    class_correct = list(0. for i in range(10))
    class_total = list(0. for i in range(10))

    model.eval() # prep model for *evaluation*

    for data, target in test_loader:
        # forward pass: compute predicted outputs by passing inputs to the model
        output = model(data)
        target_unfolded = data.view(-1, 28 * 28)
        # calculate the loss
        loss = criterion(output, target_unfolded)
        # update test loss 
        test_loss += loss.item()*data.size(0)

    # calculate and print avg test loss
    test_loss = test_loss/len(test_loader.dataset)
    print('Test Loss: {:.6f}\n'.format(test_loss))

def save_model(model, model_path, embedding_dim, n_epochs, learning_rate):
    directory = os.path.dirname(model_path)
    if not os.path.exists(directory):
        os.mkdir(directory)

    model_name = "encoder_dim{}_epochs{}_lr{}".format(embedding_dim, n_epochs, learning_rate)
    if model_path[-1] != "/":
        model_path = model_path + "/"
    torch.save(model.state_dict(), model_path + model_name)

def main(num_workers, batch_size, n_epochs, learning_rate, embedding_dim, model_path):
    print("Training a nework with the following parameters:")
    print("\tNumber of epochs: {}".format(n_epochs))
    print("\tLearning rate: {}".format(learning_rate))
    print("\tEmbedding dimension: {}".format(embedding_dim))
    start_time = time.time()
    
    # Get data
    train_loader, test_loader = create_data_itterators(num_workers, batch_size)

    # Specify the model
    model, criterion, optimizer = model_settup(embedding_dim, learning_rate)
    
    # Train your model
    train_model(model, optimizer, criterion, n_epochs, train_loader)

    # Test your model
    test_model(model, criterion, test_loader)

    # Save your model
    save_model(model, model_path, embedding_dim, n_epochs, learning_rate)

    print("Total run time: {}".format(start_time-time.time()))

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-num_workers", type=int, help="Number of workers to parse data, default =0)", default=0)
    parser.add_argument("-batch_size", type=int, help="Number of batches during trainging/testing", default=20)
    parser.add_argument("-n_epochs", type=int, help="Number of epochs for training", default=30)
    parser.add_argument("-learning_rate", type=float, help="Learning rate during training", default=0.05) 
    parser.add_argument("-embedding_dim", type=int, help="Embedding dimention for training", default=300)
    parser.add_argument("-model_path", help="Path to save your model", default="/home/ec2-user/projects/models/")    
    args = parser.parse_args()

    main(args.num_workers, args.batch_size, args.n_epochs, args.learning_rate, args.embedding_dim, args.model_path)