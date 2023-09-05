import torch


# Example usage:
# Assuming you have a tensor with shape (batch_size, num_channels, height, width)
# and you want to split it along the channel dimension (num_channels)

def split_by_percentage(tensor, dimension, percentage):
    # Get the size of the dimension along which you want to split the tensor
    dim_size = tensor.size(dimension)

    # Calculate the split point based on the given percentage
    split_point = int(dim_size * percentage)
    print(split_point)

    # Use the split function to split the tensor into two parts
    first_part, second_part = torch.split(tensor, split_point, dim=dimension)

    return first_part, second_part


percentage = 0.75  # 60% of the channels

tensor = torch.randn(4, 8, 32, 32)  # Example tensor

first_half, second_half = split_by_percentage(tensor, dimension=1, percentage=percentage)

print(first_half.shape)
print(second_half.shape)