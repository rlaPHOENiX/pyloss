import torch


class Overflow(torch.nn.Module):
    """
    Overflow loss. Only use if the image range is in [0,1].
    This solves the SPL brightness problem and can be useful in other cases as well.
    Source: https://git.io/JLhv7 (lj1995-computer-vision/Trident-Dehazing-Network)
    """

    def __init__(self):
        super(Overflow, self).__init__()

    @staticmethod
    def forward(img1):
        img_clamp = img1.clamp(0, 1)
        b, c, h, w = img1.shape
        return torch.log((img1 - img_clamp).abs() + 1).sum() / b / c / h / w
