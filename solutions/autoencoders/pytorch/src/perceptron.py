import torch.nn as nn
import torch.nn.functional as F

## Define the NN architecture
class MLP(nn.Module):
    def __init__(self, embedding_dim = 300):
        super(MLP, self).__init__()
        self.fc1 = nn.Linear(28 * 28, embedding_dim)
        # linear layer (n_hidden -> hidden_2)
        self.fc2 = nn.Linear(embedding_dim, embedding_dim)
        # linear layer (n_hidden -> 10)
        self.fc3 = nn.Linear(embedding_dim, 10)
        # dropout layer (p=0.2)
        # dropout prevents overfitting of data
        self.dropout = nn.Dropout(0.2)

    def forward(self, x):
        # flatten image input
        x = x.view(-1, 28 * 28)
        # add hidden layer, with relu activation function
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = F.log_softmax(self.fc3(x), dim=1)
        return x