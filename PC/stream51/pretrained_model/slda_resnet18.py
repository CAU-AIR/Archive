import torch
import torch.nn as nn
from avalanche.models.utils import FeatureExtractorBackbone
from pretrained_model.resnet18_places365 import build_resnet18

from pathlib import Path
import os

FILE = Path(__file__).resolve()
ROOT = FILE.parents[0]  

ROOT = Path(os.path.relpath(ROOT, Path.cwd()))  # relative

class SLDAResNetModel(nn.Module):
    """
    This is a model wrapper to reproduce experiments from the original
    paper of Deep Streaming Linear Discriminant Analysis by using
    a pretrained ResNet model.
    """

    def __init__(
        self,
        device="cpu",
    ):
        """Init.

        :param arch: backbone architecture. Default is resnet-18, but others
            can be used by modifying layer for
            feature extraction in ``self.feature_extraction_wrapper``.
        :param imagenet_pretrained: True if initializing backbone with imagenet
            pre-trained weights else False
        :param output_layer_name: name of the layer from feature extractor
        :param device: cpu, gpu or other device
        """

        super(SLDAResNetModel, self).__init__()

        #model = build_resnet18()

        #feat_extractor = (
        #    models.__dict__[arch](pretrained=imagenet_pretrained)
        #    .to(device)
        #    .eval()
        #)
        feat_extractor = build_resnet18().to(device).eval()
        output_layer_name="layer4.1"

        self.feature_extraction_wrapper = FeatureExtractorBackbone(
            feat_extractor, output_layer_name
        ).eval()

    @staticmethod
    def pool_feat(features):
        feat_size = features.shape[-1]
        num_channels = features.shape[1]
        features2 = features.permute(0, 2, 3, 1)  # 1 x feat_size x feat_size x
        # num_channels
        features3 = torch.reshape(
            features2, (features.shape[0], feat_size * feat_size, num_channels)
        )
        feat = features3.mean(1)  # mb x num_channels
        return feat

    def forward(self, x):
        """
        :param x: raw x data
        """
        feat = self.feature_extraction_wrapper(x)
        feat = SLDAResNetModel.pool_feat(feat)
        return feat
