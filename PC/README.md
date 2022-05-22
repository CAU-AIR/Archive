# Archive - PC
 All experiments were conducted on PC

# (Key) Requirements
python 3.8.5

scikit-learn 1.0.2

# Hardware Specification

Hardware | Specification
:----: | :----:
Processor | Intel Core i7-12700 / 12 Core
Memory | 64GB
GPU | RTX 3070 Ti 8GB

# CIFAR-10
| Method | Train Size | Test Size | Feature Extraction Method | Feature Extraction Size | Epoch | Dimension Reduction Method | Reduced Feature | IID</br>(Accuracy / Forgetting) | CLS IID</br>(Accuracy / Forgetting) | INST</br>(Accuracy / Forgetting) | CLS INST</br>(Accuracy / Forgetting) |
|:------:|:----------:|:---------:|:-------------------------:|:-----------------------:|:-----:|:--------------------------:|:---------------:|:-------------------------------:|:-----------------------------------:|:--------------------------------:|:-------------------------------------:|
|   NCM  |   40,000   |   10,000  |           -               |           -             |   10  |             -              |        -        |            27.14 / -            |                   -                 |                -             |                   -                  |
|   CNN  |   50,000   |   10,000  |         ResNet-18         |           512           |  100  |              -             |        -        |             85.55 / -           |                 60 / -              |                70          |                   80                 |