import torch


class Charbonnier(torch.nn.Module):
    """
    Charbonnier (one variant of Robust L1Loss, a differentiable variant of L1 Loss).
    Described in "Deep Laplacian Pyramid Networks for Fast and Accurate Super-Resolution".
    Source: https://github.com/victorca25/BasicSR/blob/master/codes/models/modules/loss.py

    TODO: The code from upstream: https://github.com/xinntao/BasicSR/blob/master/basicsr/models/losses/losses.py
          Seems more efficient.

    Args:
        eps (float): A value used to control the curvature near zero.
    """
    def __init__(self, eps=1e-12):
        super(Charbonnier, self).__init__()
        self.eps = eps

    def forward(self, x, y):
        b, c, h, w = y.size()
        loss = torch.sum(torch.sqrt((x - y).pow(2) + self.eps ** 2))
        return loss / (c * b * h * w)
