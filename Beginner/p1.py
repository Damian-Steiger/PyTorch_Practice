import torch 
import torchvision
import matplotlib.pyplot as plt
from torchvision import transforms, datasets

train = datasets.MNIST("", train = True, download = True, transform= transforms.Compose([transforms.ToTensor()])) 

test = datasets.MNIST("", train = True, download = True, transform= transforms.Compose([transforms.ToTensor()]))

trainset = torch.utils.data.DataLoader(train, batch_size = 10, shuffle = True)

testset = torch.utils.data.DataLoader(train, batch_size = 10, shuffle = True)

for data in trainset:
    break

x, y = data[0][0], data[0][0]

plt.imshow(data[0][0].view(28, 28))
#plt.show()







