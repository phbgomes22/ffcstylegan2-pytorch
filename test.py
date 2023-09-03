import torch


# Example usage:
# Assuming you have a tensor with shape (batch_size, num_channels, height, width)
# and you want to split it along the channel dimension (num_channels)

tensor = torch.randn(4, 8, 32, 32)  # Example tensor

first_half, second_half = torch.split(tensor, tensor.size(1)// 2, dim=1)

print(first_half.shape)
print(second_half.shape)