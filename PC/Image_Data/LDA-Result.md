- [Experimental Results with LDA](#experimental-results-with-lda)
  - [Comparison Results](#comparison-results)
  - [Time Comparison Results](#time-comparison-results)
# Experimental Results with LDA

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
|          LDA          |   60,000   |  10,000   |          Flatten          |       784 (100%)        |             -              |            -             |     87.30     |
|          LDA          |   60,000   |  10,000   |          Flatten          |           784           |            PCA             |         2 (0.3%)         |     44.29     |
|          LDA          |   60,000   |  10,000   |          Flatten          |           784           |            PCA             |         3 (0.4%)         |     46.60     |
|          LDA          |   60,000   |  10,000   |          Flatten          |           784           |            PCA             |         5 (0.6%)         |     66.49     |
|          LDA          |   60,000   |  10,000   |          Flatten          |           784           |            PCA             |        26 (3.3%)         |     85.73     |
|          LDA          |   60,000   |  10,000   |          Flatten          |           784           |            PCA             |        43 (5.5%)         |     87.20     |
|          LDA          |   60,000   |  10,000   |          Flatten          |           784           |            LDA             |         2 (0.3%)         |     54.13     |
|          LDA          |   60,000   |  10,000   |          Flatten          |           784           |            LDA             |         3 (0.4%)         |     72.73     |
|          LDA          |   60,000   |  10,000   |          Flatten          |           784           |            LDA             |         5 (0.6%)         |     81.35     |
|          LDA          |   60,000   |  10,000   |          Flatten          |           784           |            LDA             |         9 (1.1%)         |     87.30     |
|          LDA          |   60,000   |  10,000   |        3 layer CNN        |        64 (8.2%)        |             -              |            -             |     98.25     |
|          LDA          |   60,000   |  10,000   |        3 layer CNN        |           64            |            PCA             |         2 (0.3%)         |     57.73     |
|          LDA          |   60,000   |  10,000   |        3 layer CNN        |           64            |            PCA             |         3 (0.4%)         |     74.01     |
|          LDA          |   60,000   |  10,000   |        3 layer CNN        |           64            |            PCA             |         5 (0.6%)         |     90.70     |
|          LDA          |   60,000   |  10,000   |        3 layer CNN        |           64            |            PCA             |        26 (3.3%)         |     98.01     |
|          LDA          |   60,000   |  10,000   |        3 layer CNN        |           64            |            PCA             |        43 (5.5%)         |     98.28     |
|          LDA          |   60,000   |  10,000   |        3 layer CNN        |           64            |            LDA             |         2 (0.3%)         |     81.60     |
|          LDA          |   60,000   |  10,000   |        3 layer CNN        |           64            |            LDA             |         3 (0.4%)         |     89.46     |
|          LDA          |   60,000   |  10,000   |        3 layer CNN        |           64            |            LDA             |         5 (0.6%)         |     95.56     |
|          LDA          |   60,000   |  10,000   |        3 layer CNN        |           64            |            LDA             |         9 (1.1%)         |     98.25     |

---
<br/><br/>

## Time Comparison Results
| Classification Method | Feature Extraction Time | Training Dimension Reduction Time | Model Training Time | Incremental Model Update Time | Inference Dimension Reduction Time | Inference Feature Extraction Time | Model Inference Time |
| :-------------------: | :---------------------: | :-------------------------------: | :-----------------: | :---------------------------: | :--------------------------------: | :-------------------------------: | :------------------: |
|          LDA          |            -            |                 -                 |          -          |               -               |                 -                  |                 -                 |          -           |
