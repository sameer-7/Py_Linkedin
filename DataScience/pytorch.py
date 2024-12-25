# PyTorch is an open-source deep learning library developed by Facebook. It is known for its flexibility and ease of use, especially for dynamic computation graphs.
import torch
import torch.nn as nn
import torch.optim as optim

#creating a simple neural network model
class SimpleNN(nn.Module):
    def __init__(self):
        super(SimpleNN,self).__init__()
        #Input to Hidden
        self.fc1 = nn.Linear(4,10)
        #Hidden to Input
        self.fc2 = nn.Linear(10,3)
    def forward(self,x):
        x = torch.relu(self.fc1(x))
        x = self.fc2(x)
        return x
#Sample data (Iris dataset)
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
import numpy as np

iris = load_iris()
X_train, X_test, y_train, y_test = train_test_split(iris.data,iris.target,test_size=0.2,random_state=42)

#Convert data to PyTorch tensors
X_train_tensor = torch.FloatTensor(X_train)
y_train_tensor = torch.LongTensor(y_train)

#Training the model
model = SimpleNN()
criterian = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(),lr=0.01)

#train for 100 epochs
for epoch in range(100):
    optimizer.zero_grad()
    outputs = model(X_train_tensor)
    loss = criterion(outputs,y_train_tensor)
    loss.backward()
    optimizer.step()
print("Training complete.")