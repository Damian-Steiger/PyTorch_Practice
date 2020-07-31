import torch

x = torch.Tensor([5,3])
y = torch.rand([2,5])

y = y.view([1, 10])


print(y)



