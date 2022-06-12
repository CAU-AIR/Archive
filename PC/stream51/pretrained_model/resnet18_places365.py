import torch
from torch import nn
from torchvision import models 

from pathlib import Path
import sys
import os

FILE = Path(__file__).resolve()
ROOT = FILE.parents[0]  

#if str(ROOT) not in sys.path:
#    sys.path.append(str(ROOT))  # add ROOT to PATH
ROOT = Path(os.path.relpath(ROOT, Path.cwd()))  # relative
#print(ROOT)

def build_resnet18(fe=False):
    resnet = models.resnet18(pretrained=False)
    resnet.fc = nn.Linear(resnet.fc.in_features, 51)
    resumed = torch.load(ROOT / "resnet18_places365.pth.tar", map_location='cuda:0')
    safe_load_dict(resnet, resumed['state_dict'])
    
    if fe:
        print('Using model as feature extractor')
        for params in resnet.model.parameters():
            params.requires_grad = False
        for params in resnet.model.fc.parameters():
            params.requires_grad = True
    return resnet

def safe_load_dict(model, new_model_state):
    old_model_state = model.state_dict()
    c = 0
    for name, param in new_model_state.items():
        name = '.'.join(name.split('.')[1:])
        if name not in old_model_state:
            print('%s not found in old model.' % name)
            continue
        if isinstance(param, nn.Parameter):
            # backwards compatibility for serialized parameters
            param = param.data
        c += 1
        if old_model_state[name].shape != param.shape:
            print('Shape mismatch...ignoring %s' % name)
            continue
        else:
            old_model_state[name].copy_(param)
    if c == 0:
        raise AssertionError('No previous ckpt names matched and the ckpt was not loaded properly.')

if __name__ == "__main__":
    model = build_resnet18()
    model_state = model.state_dict()
    for name, _ in model_state.items():
        print(name)

