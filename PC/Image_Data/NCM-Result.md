- [Experimental Results with NCM](#experimental-results-with-ncm)
  - [Comparison Results](#comparison-results)
  - [Time Comparison Results](#time-comparison-results)
# Experimental Results with NCM

<a title="By Josef Steppan [CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0)], from Wikimedia Commons" href="https://commons.wikimedia.org/wiki/File:MnistExamples.png"><img width="512" alt="MnistExamples" src="https://upload.wikimedia.org/wikipedia/commons/2/27/MnistExamples.png"/></a>
- MNIST Dataset
- Image size : 28 x 28
- Feature size : 784
- The number of classes : 10

---

<!-- Can use Cell Merge if we use Jekyll plugin -->
## Comparison Results
| Classification Method | Train Size | Test Size | Feature Extraction Method | Feature Extraction Size | Dimension Reduction Method | Dimension Reduction Size | Test Accuracy |
| :-------------------: | :--------: | :-------: | :-----------------------: | :---------------------: | :------------------------: | :----------------------: | :-----------: |
|          NCM          |   60,000   |  10,000   |          Flatten          |       784 (100%)        |             -              |            -             |     82.03     |
|          NCM          |   60,000   |  10,000   |          Flatten          |           784           |            PCA             |         2 (0.3%)         |     43.65     |
|          NCM          |   60,000   |  10,000   |          Flatten          |           784           |            PCA             |         3 (0.4%)         |     45.68     |
|          NCM          |   60,000   |  10,000   |          Flatten          |           784           |            PCA             |         5 (0.6%)         |     64.10     |
|          NCM          |   60,000   |  10,000   |          Flatten          |           784           |            PCA             |        26 (3.3%)         |     80.89     |
|          NCM          |   60,000   |  10,000   |          Flatten          |           784           |            PCA             |        43 (5.5%)         |     81.62     |
|          NCM          |   60,000   |  10,000   |          Flatten          |           784           |            LDA             |         2 (0.3%)         |     54.58     |
|          NCM          |   60,000   |  10,000   |          Flatten          |           784           |            LDA             |         3 (0.4%)         |     73.03     |
|          NCM          |   60,000   |  10,000   |          Flatten          |           784           |            LDA             |         5 (0.6%)         |     81.19     |
|          NCM          |   60,000   |  10,000   |          Flatten          |           784           |            LDA             |         9 (1.1%)         |     87.30     |
|          NCM          |   60,000   |  10,000   |        3 layer CNN        |        64 (8.2%)        |             -              |            -             |     95.39     |
|          NCM          |   60,000   |  10,000   |        3 layer CNN        |           64            |            PCA             |         2 (0.3%)         |     56.21     |
|          NCM          |   60,000   |  10,000   |        3 layer CNN        |           64            |            PCA             |         3 (0.4%)         |     72.16     |
|          NCM          |   60,000   |  10,000   |        3 layer CNN        |           64            |            PCA             |         5 (0.6%)         |     87.23     |
|          NCM          |   60,000   |  10,000   |        3 layer CNN        |           64            |            PCA             |        26 (3.3%)         |     95.35     |
|          NCM          |   60,000   |  10,000   |        3 layer CNN        |           64            |            PCA             |        43 (5.5%)         |     95.36     |
|          NCM          |   60,000   |  10,000   |        3 layer CNN        |           64            |            LDA             |         2 (0.3%)         |     81.45     |
|          NCM          |   60,000   |  10,000   |        3 layer CNN        |           64            |            LDA             |         3 (0.4%)         |     89.49     |
|          NCM          |   60,000   |  10,000   |        3 layer CNN        |           64            |            LDA             |         5 (0.6%)         |     95.59     |
|          NCM          |   60,000   |  10,000   |        3 layer CNN        |           64            |            LDA             |         9 (1.1%)         |     98.24     |

---
<br/><br/>

## Time Comparison Results
| Classification Method | Feature Extraction Time | Training Dimension Reduction Time | Model Training Time | Incremental Model Update Time | Inference Dimension Reduction Time | Inference Feature Extraction Time | Model Inference Time |
| :-------------------: | :---------------------: | :-------------------------------: | :-----------------: | :---------------------------: | :--------------------------------: | :-------------------------------: | :------------------: |
|          NCM          |            -            |                 -                 |          -          |               -               |                 -                  |                 -                 |          -           |
