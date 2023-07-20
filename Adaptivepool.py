import torch
import torch.nn as nn

x = torch.randn(5,3,512,512)
print(x.shape)

a = nn.AdaptiveAvgPool2d((10,10))
out = a(x)
print(out.shape)

a = nn.AdaptiveAvgPool2d((1007,1007))
out = a(x)
print(out.shape)

a = nn.AdaptiveAvgPool2d(1)
out = a(x)
print(out.shape)