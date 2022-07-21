import time
import numpy as np
import torch
import shutil
from enum import Enum

feature_layers = {'8': 'AdaptiveAvgPool2d'}

def get_features(x, model, layers):
    for name, layer in enumerate(model.children()): # 0, conv
        x = layer(x)
        if str(name) in layers:
            features = x
            break
    return features

def train(train_loader, model, device):
    model.eval()
    features = np.empty((0, 512), float)
    targets = np.empty(0, float)

    for images, target in train_loader:
        if torch.cuda.is_available():
            images = images.to(device)
            target = target.cuda(device)

        # compute output
        feature = get_features(images, model, feature_layers)
        feature = torch.flatten(feature, 1)

        features = np.append(features, feature.detach().cpu().numpy(), axis=0)
        targets = np.append(targets, target.detach().cpu().numpy(), axis=0)

    return features, targets


def validate(val_loader, model, device):
    features = np.empty((0, 512), float)
    targets = np.empty(0, float)

    # switch to evaluate mode
    model.eval()

    with torch.no_grad():
        for images, target in val_loader:
            if torch.cuda.is_available():
                images = images.to(device)
                target = target.cuda(device)

            # compute output
            feature = get_features(images, model, feature_layers)
            feature = torch.flatten(feature, 1)

            features = np.append(features, feature.detach().cpu().numpy(), axis=0)
            targets = np.append(targets, target.detach().cpu().numpy(), axis=0)

    return features, targets


def save_checkpoint(state, is_best, filename='checkpoint/checkpoint.pth.tar'):
    torch.save(state, filename)
    if is_best:
        shutil.copyfile(filename, 'checkpoint/model_best.pth.tar')


class Summary(Enum):
    NONE = 0
    AVERAGE = 1
    SUM = 2
    COUNT = 3


class AverageMeter(object):
    """Computes and stores the average and current value"""
    def __init__(self, name, fmt=':f', summary_type=Summary.AVERAGE):
        self.name = name
        self.fmt = fmt
        self.summary_type = summary_type
        self.reset()

    def reset(self):
        self.val = 0
        self.avg = 0
        self.sum = 0
        self.count = 0

    def update(self, val, n=1):
        self.val = val
        self.sum += val * n
        self.count += n
        self.avg = self.sum / self.count

    def __str__(self):
        fmtstr = '{name} {avg' + self.fmt + '}'
        return fmtstr.format(**self.__dict__)
    
    def summary(self):
        fmtstr = ''
        if self.summary_type is Summary.NONE:
            fmtstr = ''
        elif self.summary_type is Summary.AVERAGE:
            fmtstr = '{name} {avg:.4f}'
        elif self.summary_type is Summary.SUM:
            fmtstr = '{name} {sum:.4f}'
        elif self.summary_type is Summary.COUNT:
            fmtstr = '{name} {count:.4f}'
        else:
            raise ValueError('invalid summary type %r' % self.summary_type)
        
        return fmtstr.format(**self.__dict__)


class ProgressMeter(object):
    def __init__(self, num_batches, meters, prefix=""):
        self.batch_fmtstr = self._get_batch_fmtstr(num_batches)
        self.meters = meters
        self.prefix = prefix

    def display(self, batch):
        entries = [self.prefix + self.batch_fmtstr.format(batch)]
        entries += [str(meter) for meter in self.meters]
        print('\t'.join(entries))
        
    def display_summary(self):
        entries = [" *"]
        entries += [meter.summary() for meter in self.meters]
        print(' '.join(entries))

    def _get_batch_fmtstr(self, num_batches):
        num_digits = len(str(num_batches // 1))
        fmt = '{:' + str(num_digits) + 'd}'
        return '[' + fmt + '/' + fmt.format(num_batches) + ']'


def accuracy(output, target):
    """Computes the accuracy over the k top predictions for the specified values"""
    with torch.no_grad():
        batch_size = target.size(0)

        _, pred = output.topk(1, 1, True, True)  # k, dim, largest, sorted
        pred = pred.t()
        correct = pred.eq(target.view(1, -1).expand_as(pred))

        correct = correct[0].reshape(-1).float().sum(0, keepdim=True)
        correct = correct.mul_(100.0 / batch_size)

        return correct