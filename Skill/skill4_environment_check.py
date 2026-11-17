
import torch
import sys

print("Deep Learning - Skill 4")

print("Python Version:", sys.version)
print("PyTorch Version:", torch.__version__)
print("CUDA Available:", torch.cuda.is_available())
print("CUDA Version:", torch.version.cuda)

if torch.cuda.is_available():
    print("GPU Name:", torch.cuda.get_device_name(0))

print("Environment Setup Completed!")
