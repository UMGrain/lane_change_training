import torch
from torch import nn
from .resnet import *

class multi_prediction(nn.Module):
    def __int__(self):
        self.backbone = resnet34(pretrained=True)

    def forward(self, img):
        feature_emb, _ = self.backbone(img)
        print(feature_emb.shape)



model = multi_prediction()
img = torch.randn(1, 3, 386, 800)
model(img)