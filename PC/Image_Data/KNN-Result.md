- [Experimental Results with KNN](#experimental-results-with-knn)
  - [Comparison Results with K = 3](#comparison-results-with-k--3)
  - [Time Comparison Results](#time-comparison-results)
  - [Comparison Results with K = {1,2,3,5}](#comparison-results-with-k--1235)
# Experimental Results with KNN

<a title="By Josef Steppan [CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0)], from Wikimedia Commons" href="https://commons.wikimedia.org/wiki/File:MnistExamples.png"><img width="512" alt="MnistExamples" src="https://upload.wikimedia.org/wikipedia/commons/2/27/MnistExamples.png"/></a>
- MNIST Dataset
- Image size : 28 x 28
- Feature size : 784
- The number of classes : 10
- E : Euclidian 
- PCA -Proportion of variance : 26-(70%), 43-(80%)

---

<!-- Can use Cell Merge if we use Jekyll plugin -->
## Comparison Results with K = 3
| Classification Method | Train Size | Test Size | Feature Extraction Method | Feature Extraction Size | Dimension Reduction Method | Dimension Reduction Size | Test Accuracy |
| :-------------------: | :--------: | :-------: | :-----------------------: | :---------------------: | :------------------------: | :----------------------: | :-----------: |
|        3-NN(E)        |   60,000   |  10,000   |          Flatten          |       784 (100%)        |             -              |            -             |     97.2      |
|        3-NN(E)        |   60,000   |  10,000   |          Flatten          |           784           |            PCA             |         2 (0.3%)         |     40.2      |
|        3-NN(E)        |   60,000   |  10,000   |          Flatten          |           784           |            PCA             |         3 (0.4%)         |     46.0      |
|        3-NN(E)        |   60,000   |  10,000   |          Flatten          |           784           |            PCA             |         5 (0.6%)         |     72.6      |
|        3-NN(E)        |   60,000   |  10,000   |          Flatten          |           784           |            PCA             |        26 (3.3%)         |     97.4      |
|        3-NN(E)        |   60,000   |  10,000   |          Flatten          |           784           |            PCA             |        43 (5.5%)         |     97.6      |
|        3-NN(E)        |   60,000   |  10,000   |          Flatten          |           784           |            LDA             |         2 (0.3%)         |     49.1      |
|        3-NN(E)        |   60,000   |  10,000   |          Flatten          |           784           |            LDA             |         3 (0.4%)         |     69.9      |
|        3-NN(E)        |   60,000   |  10,000   |          Flatten          |           784           |            LDA             |         5 (0.6%)         |     82.1      |
|        3-NN(E)        |   60,000   |  10,000   |          Flatten          |           784           |            LDA             |         9 (1.1%)         |     91.1      |
|        3-NN(E)        |   60,000   |  10,000   |        3 layer CNN        |        64 (8.2%)        |             -              |            -             |     98.8      |
|        3-NN(E)        |   60,000   |  10,000   |        3 layer CNN        |           64            |            PCA             |         2 (0.3%)         |     67.1      |
|        3-NN(E)        |   60,000   |  10,000   |        3 layer CNN        |           64            |            PCA             |         3 (0.4%)         |     87.6      |
|        3-NN(E)        |   60,000   |  10,000   |        3 layer CNN        |           64            |            PCA             |         5 (0.6%)         |     97.3      |
|        3-NN(E)        |   60,000   |  10,000   |        3 layer CNN        |           64            |            PCA             |        26 (3.3%)         |     98.7      |
|        3-NN(E)        |   60,000   |  10,000   |        3 layer CNN        |           64            |            PCA             |        43 (5.5%)         |     98.7      |
|        3-NN(E)        |   60,000   |  10,000   |        3 layer CNN        |           64            |            LDA             |         2 (0.3%)         |     78.7      |
|        3-NN(E)        |   60,000   |  10,000   |        3 layer CNN        |           64            |            LDA             |         3 (0.4%)         |     88.1      |
|        3-NN(E)        |   60,000   |  10,000   |        3 layer CNN        |           64            |            LDA             |         5 (0.6%)         |     96.1      |
|        3-NN(E)        |   60,000   |  10,000   |        3 layer CNN        |           64            |            LDA             |         9 (1.1%)         |     98.8      |

---
<br/><br/>

## Time Comparison Results
| Classification Method | Feature Extraction Time | Training Dimension Reduction Time | Model Training Time | Incremental Model Update Time | Inference Dimension Reduction Time | Inference Feature Extraction Time | Model Inference Time |
| :-------------------: | :---------------------: | :-------------------------------: | :-----------------: | :---------------------------: | :--------------------------------: | :-------------------------------: | :------------------: |
|        3-NN(E)        |            -            |                 -                 |          -          |               -               |                 -                  |                 -                 |          -           |


---

<br/><br/>
## Comparison Results with K = {1,2,3,5}

| Classification Method | Train Size | Test Size | Feature Extraction Method | Feature Extraction Size | Dimension Reduction Method | Dimension Reduction Size | Test Accuracy |
| :-------------------: | :--------: | :-------: | :-----------------------: | :---------------------: | :------------------------: | :----------------------: | :-----------: |
|        1-NN(E)        |   60,000   |  10,000   |          Flatten          |       784 (100%)        |             -              |            -             |     96.9      |
|        2-NN(E)        |   60,000   |  10,000   |          Flatten          |       784 (100%)        |             -              |            -             |     96.9      |
|        3-NN(E)        |   60,000   |  10,000   |          Flatten          |       784 (100%)        |             -              |            -             |     97.2      |
|        5-NN(E)        |   60,000   |  10,000   |          Flatten          |       784 (100%)        |             -              |            -             |     96.9      |
|        1-NN(E)        |   60,000   |  10,000   |          Flatten          |           784           |            PCA             |         2 (0.3%)         |     39.0      |
|        2-NN(E)        |   60,000   |  10,000   |          Flatten          |           784           |            PCA             |         2 (0.3%)         |     39.0      |
|        3-NN(E)        |   60,000   |  10,000   |          Flatten          |           784           |            PCA             |         2 (0.3%)         |     40.2      |
|        5-NN(E)        |   60,000   |  10,000   |          Flatten          |           784           |            PCA             |         2 (0.3%)         |     41.3      |
|        1-NN(E)        |   60,000   |  10,000   |          Flatten          |           784           |            PCA             |         3 (0.4%)         |     44.3      |
|        2-NN(E)        |   60,000   |  10,000   |          Flatten          |           784           |            PCA             |         3 (0.4%)         |     44.3      |
|        3-NN(E)        |   60,000   |  10,000   |          Flatten          |           784           |            PCA             |         3 (0.4%)         |     46.0      |
|        5-NN(E)        |   60,000   |  10,000   |          Flatten          |           784           |            PCA             |         3 (0.4%)         |     47.6      |
|        1-NN(E)        |   60,000   |  10,000   |          Flatten          |           784           |            PCA             |         5 (0.6%)         |     69.4      |
|        2-NN(E)        |   60,000   |  10,000   |          Flatten          |           784           |            PCA             |         5 (0.6%)         |     69.4      |
|        3-NN(E)        |   60,000   |  10,000   |          Flatten          |           784           |            PCA             |         5 (0.6%)         |     72.6      |
|        5-NN(E)        |   60,000   |  10,000   |          Flatten          |           784           |            PCA             |         5 (0.6%)         |     74.5      |
|        1-NN(E)        |   60,000   |  10,000   |          Flatten          |           784           |            PCA             |        26 (3.3%)         |     97.2      |
|        2-NN(E)        |   60,000   |  10,000   |          Flatten          |           784           |            PCA             |        26 (3.3%)         |     97.2      |
|        3-NN(E)        |   60,000   |  10,000   |          Flatten          |           784           |            PCA             |        26 (3.3%)         |     97.4      |
|        5-NN(E)        |   60,000   |  10,000   |          Flatten          |           784           |            PCA             |        26 (3.3%)         |     97.5      |
|        1-NN(E)        |   60,000   |  10,000   |          Flatten          |           784           |            PCA             |        43 (5.5%)         |     97.4      |
|        2-NN(E)        |   60,000   |  10,000   |          Flatten          |           784           |            PCA             |        43 (5.5%)         |     97.4      |
|        3-NN(E)        |   60,000   |  10,000   |          Flatten          |           784           |            PCA             |        43 (5.5%)         |     97.6      |
|        5-NN(E)        |   60,000   |  10,000   |          Flatten          |           784           |            PCA             |        43 (5.5%)         |     97.5      |
|        1-NN(E)        |   60,000   |  10,000   |          Flatten          |           784           |            LDA             |         2 (0.3%)         |     47.1      |
|        2-NN(E)        |   60,000   |  10,000   |          Flatten          |           784           |            LDA             |         2 (0.3%)         |     47.1      |
|        3-NN(E)        |   60,000   |  10,000   |          Flatten          |           784           |            LDA             |         2 (0.3%)         |     49.1      |
|        5-NN(E)        |   60,000   |  10,000   |          Flatten          |           784           |            LDA             |         2 (0.3%)         |     51.2      |
|        1-NN(E)        |   60,000   |  10,000   |          Flatten          |           784           |            LDA             |         3 (0.4%)         |     66.9      |
|        2-NN(E)        |   60,000   |  10,000   |          Flatten          |           784           |            LDA             |         3 (0.4%)         |     66.9      |
|        3-NN(E)        |   60,000   |  10,000   |          Flatten          |           784           |            LDA             |         3 (0.4%)         |     69.9      |
|        5-NN(E)        |   60,000   |  10,000   |          Flatten          |           784           |            LDA             |         3 (0.4%)         |     71.9      |
|        1-NN(E)        |   60,000   |  10,000   |          Flatten          |           784           |            LDA             |         5 (0.6%)         |     79.0      |
|        2-NN(E)        |   60,000   |  10,000   |          Flatten          |           784           |            LDA             |         5 (0.6%)         |     79.0      |
|        3-NN(E)        |   60,000   |  10,000   |          Flatten          |           784           |            LDA             |         5 (0.6%)         |     82.1      |
|        5-NN(E)        |   60,000   |  10,000   |          Flatten          |           784           |            LDA             |         5 (0.6%)         |     83.3      |
|        1-NN(E)        |   60,000   |  10,000   |          Flatten          |           784           |            LDA             |         9 (1.1%)         |     89.9      |
|        2-NN(E)        |   60,000   |  10,000   |          Flatten          |           784           |            LDA             |         9 (1.1%)         |     89.9      |
|        3-NN(E)        |   60,000   |  10,000   |          Flatten          |           784           |            LDA             |         9 (1.1%)         |     91.1      |
|        5-NN(E)        |   60,000   |  10,000   |          Flatten          |           784           |            LDA             |         9 (1.1%)         |     91.5      |
|        1-NN(E)        |   60,000   |  10,000   |        3 layer CNN        |        64 (8.2%)        |             -              |            -             |     98.6      |
|        2-NN(E)        |   60,000   |  10,000   |        3 layer CNN        |        64 (8.2%)        |             -              |            -             |     98.6      |
|        3-NN(E)        |   60,000   |  10,000   |        3 layer CNN        |        64 (8.2%)        |             -              |            -             |     98.8      |
|        5-NN(E)        |   60,000   |  10,000   |        3 layer CNN        |        64 (8.2%)        |             -              |            -             |     98.8      |
|        1-NN(E)        |   60,000   |  10,000   |        3 layer CNN        |           64            |            PCA             |         2 (0.3%)         |     63.8      |
|        2-NN(E)        |   60,000   |  10,000   |        3 layer CNN        |           64            |            PCA             |         2 (0.3%)         |     64.2      |
|        3-NN(E)        |   60,000   |  10,000   |        3 layer CNN        |           64            |            PCA             |         2 (0.3%)         |     67.1      |
|        5-NN(E)        |   60,000   |  10,000   |        3 layer CNN        |           64            |            PCA             |         2 (0.3%)         |     69.7      |
|        1-NN(E)        |   60,000   |  10,000   |        3 layer CNN        |           64            |            PCA             |         3 (0.4%)         |     85.0      |
|        2-NN(E)        |   60,000   |  10,000   |        3 layer CNN        |           64            |            PCA             |         3 (0.4%)         |     85.7      |
|        3-NN(E)        |   60,000   |  10,000   |        3 layer CNN        |           64            |            PCA             |         3 (0.4%)         |     87.6      |
|        5-NN(E)        |   60,000   |  10,000   |        3 layer CNN        |           64            |            PCA             |         3 (0.4%)         |     88.5      |
|        1-NN(E)        |   60,000   |  10,000   |        3 layer CNN        |           64            |            PCA             |         5 (0.6%)         |     96.7      |
|        2-NN(E)        |   60,000   |  10,000   |        3 layer CNN        |           64            |            PCA             |         5 (0.6%)         |     96.6      |
|        3-NN(E)        |   60,000   |  10,000   |        3 layer CNN        |           64            |            PCA             |         5 (0.6%)         |     97.3      |
|        5-NN(E)        |   60,000   |  10,000   |        3 layer CNN        |           64            |            PCA             |         5 (0.6%)         |     97.5      |
|        1-NN(E)        |   60,000   |  10,000   |        3 layer CNN        |           64            |            PCA             |        26 (3.3%)         |     98.5      |
|        2-NN(E)        |   60,000   |  10,000   |        3 layer CNN        |           64            |            PCA             |        26 (3.3%)         |     98.4      |
|        3-NN(E)        |   60,000   |  10,000   |        3 layer CNN        |           64            |            PCA             |        26 (3.3%)         |     98.7      |
|        5-NN(E)        |   60,000   |  10,000   |        3 layer CNN        |           64            |            PCA             |        26 (3.3%)         |     98.8      |
|        1-NN(E)        |   60,000   |  10,000   |        3 layer CNN        |           64            |            PCA             |        43 (5.5%)         |     98.6      |
|        2-NN(E)        |   60,000   |  10,000   |        3 layer CNN        |           64            |            PCA             |        43 (5.5%)         |     98.5      |
|        3-NN(E)        |   60,000   |  10,000   |        3 layer CNN        |           64            |            PCA             |        43 (5.5%)         |     98.7      |
|        5-NN(E)        |   60,000   |  10,000   |        3 layer CNN        |           64            |            PCA             |        43 (5.5%)         |     98.8      |
|        1-NN(E)        |   60,000   |  10,000   |        3 layer CNN        |           64            |            LDA             |         2 (0.3%)         |     75.7      |
|        2-NN(E)        |   60,000   |  10,000   |        3 layer CNN        |           64            |            LDA             |         2 (0.3%)         |     76.7      |
|        3-NN(E)        |   60,000   |  10,000   |        3 layer CNN        |           64            |            LDA             |         2 (0.3%)         |     78.7      |
|        5-NN(E)        |   60,000   |  10,000   |        3 layer CNN        |           64            |            LDA             |         2 (0.3%)         |     80.0      |
|        1-NN(E)        |   60,000   |  10,000   |        3 layer CNN        |           64            |            LDA             |         3 (0.4%)         |     86.2      |
|        2-NN(E)        |   60,000   |  10,000   |        3 layer CNN        |           64            |            LDA             |         3 (0.4%)         |     86.3      |
|        3-NN(E)        |   60,000   |  10,000   |        3 layer CNN        |           64            |            LDA             |         3 (0.4%)         |     88.1      |
|        5-NN(E)        |   60,000   |  10,000   |        3 layer CNN        |           64            |            LDA             |         3 (0.4%)         |     89.2      |
|        1-NN(E)        |   60,000   |  10,000   |        3 layer CNN        |           64            |            LDA             |         5 (0.6%)         |     95.2      |
|        2-NN(E)        |   60,000   |  10,000   |        3 layer CNN        |           64            |            LDA             |         5 (0.6%)         |     95.1      |
|        3-NN(E)        |   60,000   |  10,000   |        3 layer CNN        |           64            |            LDA             |         5 (0.6%)         |     96.1      |
|        5-NN(E)        |   60,000   |  10,000   |        3 layer CNN        |           64            |            LDA             |         5 (0.6%)         |     96.3      |
|        1-NN(E)        |   60,000   |  10,000   |        3 layer CNN        |           64            |            LDA             |         9 (1.1%)         |     98.5      |
|        2-NN(E)        |   60,000   |  10,000   |        3 layer CNN        |           64            |            LDA             |         9 (1.1%)         |     98.4      |
|        3-NN(E)        |   60,000   |  10,000   |        3 layer CNN        |           64            |            LDA             |         9 (1.1%)         |     98.8      |
|        5-NN(E)        |   60,000   |  10,000   |        3 layer CNN        |           64            |            LDA             |         9 (1.1%)         |     98.8      |
