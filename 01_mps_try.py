import torch
# 创建conda env：YOLOv9
# 从pytorch官网下载torchhttps://pytorch.org
# !conda install pytorch::pytorch torchvision torchaudio -c pytorch
print(torch.backends.mps.is_available())
# 输出为True说明有mps
