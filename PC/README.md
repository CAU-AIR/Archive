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
| Method | Train Size | Test Size | Feature Extraction |              | Dimension Reduction |                 | Task (Acc / forgetting) |         |      |          |
|:------:|:----------:|:---------:|:------------------:|:------------:|:-------------------:|:---------------:|:-----------------------:|:-------:|:----:|:--------:|
|        |            |           |       method       | feature size |        method       | reduced feature |           IID           | CLS IID | INST | CLS INST |
|   kNN  |    1000    |    100    |       ResNet       |      512     |         pca         |        2        |          90 / -         |    x    |   x  |     x    |
|        |            |           |                    |              |                     |                 |            x            |  60/()  |  70  |    80    |