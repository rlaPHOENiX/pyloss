import torch


class Charbonnier(torch.nn.Module):
    def __init__(self, eps=1e-6):
        super(Charbonnier, self).__init__()
        self.eps = eps

    def forward(self, x, y):
        b, c, h, w = y.size()
        loss = torch.sum(torch.sqrt((x - y).pow(2) + self.eps ** 2))
        return loss / (c * b * h * w)
