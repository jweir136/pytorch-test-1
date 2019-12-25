import torch

x = torch.tensor([1, 2, 3, 4, 5]).cuda().float()
print(x)
print("[+] CUDA is working!")
