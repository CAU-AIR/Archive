import time
from matplotlib import image
from numpy import imag
import torch
import shutil
from enum import Enum

def train(train_loader, model, criterion, optimizer, epoch, device):
    print("Epoch: [{}]".format(epoch))

    batch_time = AverageMeter('Time', ':.4f')
    data_time = AverageMeter('Data', ':.4f')
    losses = AverageMeter('Loss', ':.4f')
    train_acc = AverageMeter('Acc', ':.2f')
    progress = ProgressMeter(
        len(train_loader),
        [batch_time, data_time, losses, train_acc],
        prefix='Train: ')

    # switch to train mode
    model.train()

    end = time.time()

    for i, (images, target) in enumerate(train_loader):
        # measure data loading time
        data_time.update(time.time() - end)

        if torch.cuda.is_available():
            images = images.to(device)
            target = target.cuda(device)

        # compute output
        output = model(images)
        loss = criterion(output, target)

        # measure accuracy and record loss
        acc = accuracy(output, target)
        losses.update(loss.item(), images.size(0))
        train_acc.update(acc[0], images.size(0))

        # compute gradient and do SGD step
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        # measure elapsed time
        batch_time.update(time.time() - end)
        end = time.time()

        # if i % 1000 == 0:
        #     progress.display(i)
        if i+1 == len(train_loader):
            progress.display(i+1)


def validate(val_loader, model, criterion, device):
    batch_time = AverageMeter('Time', ':.4f', Summary.NONE)
    data_time = AverageMeter('Data', ':.4f', Summary.NONE)
    losses = AverageMeter('Loss', ':.4f', Summary.NONE)
    val_acc = AverageMeter('Acc', ':.2f', Summary.AVERAGE)
    progress = ProgressMeter(
        len(val_loader),
        [batch_time, data_time, losses, val_acc],
        prefix='Test: ')

    # switch to evaluate mode
    model.eval()

    with torch.no_grad():
        end = time.time()
        for i, (images, target) in enumerate(val_loader):
            data_time.update(time.time() - end)

            if torch.cuda.is_available():
                images = images.to(device)
                target = target.cuda(device)

            # compute output
            output = model(images)
            loss = criterion(output, target)

            # measure accuracy and record loss
            acc = accuracy(output, target)
            losses.update(loss.item(), images.size(0))
            val_acc.update(acc[0], images.size(0))

            # measure elapsed time
            batch_time.update(time.time() - end)
            end = time.time()

            # if i % 10 == 0:
            #     progress.display(i)
            if i+1 == len(val_loader):
                progress.display(i+1)

        # progress.display_summary()

    return val_acc.avg


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