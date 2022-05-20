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
| Method | Train Size | Test Size | Feature Extraction Method | Feature Extraction Size | Dimension Reduction Method | Reduced Feature | IID (Acc/ Forgetting) | CLS IID (Acc/ Forgetting) | INST (Acc/ Forgetting) | CLS INST (Acc/ Forgetting) |
|:------:|:----------:|:---------:|:-------------------------:|:-----------------------:|:--------------------------:|:---------------:|:---------------------:|:-------------------------:|:----------------------:|:--------------------------:|
|   kNN  |    1000    |    100    |           ResNet          |           512           |             pca            |        2        |         90 / -        |             x             |            x           |              x             |
|   kNN  |    1000    |    100    |           ResNet          |           512           |             pca            |        2        |           x           |           60/()           |           70           |             80             |