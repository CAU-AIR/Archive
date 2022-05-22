# Experimental Results

<a title="By Josef Steppan [CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0)], from Wikimedia Commons" href="https://commons.wikimedia.org/wiki/File:MnistExamples.png"><img width="512" alt="MnistExamples" src="https://upload.wikimedia.org/wikipedia/commons/2/27/MnistExamples.png"/></a>
- MNIST Dataset
- Image size : 28 x 28
- Feature size : 784
- The number of classes : 10

---
## Method Experimental Results
  1. [KNN](KNN-Result.md)
  2. [NCM](NCM-Result.md)
  3. [LDA](LDA-Result.md)

---
<br/><br/>

## Sample Table for Standard Learning
| Classification Method | Train Size | Test Size | Feature Extraction Method | Feature Extraction Size | Dimension Reduction Method | Dimension Reduction Size | Test Accuracy |
| :-------------------: | :--------: | :-------: | :-----------------------: | :---------------------: | :------------------------: | :----------------------: | :-----------: |
|        3-NN(E)        |   60,000   |  10,000   |          Flatten          |       784 (100%)        |             -              |            -             |     97.2      |

---
<br/><br/>

## Sample Table for Incremental Learning
| Classification Method | Train Size | Incremental Size | Feature Extraction Method | Feature Extraction Size | Dimension Reduction Method | Dimension Reduction Size |  IID  | CLS IID | INST  | CLS INST |
| :-------------------: | :--------: | :--------------: | :-----------------------: | :---------------------: | :------------------------: | :----------------------: | :---: | :-----: | :---: | :------: |
|          NCM          |   60,000   |        10        |        3 layer CNN        |           64            |            LDA             |         9 (1.1%)         |   -   |    -    |   -   |    -     |

---
<br/><br/>

## Sample Time Comparison Table
| Classification Method | Feature Extraction Time | Training Dimension Reduction Time | Model Training Time | Incremental Model Update Time | Inference Dimension Reduction Time | Inference Feature Extraction Time | Model Inference Time |
| :-------------------: | :---------------------: | :-------------------------------: | :-----------------: | :---------------------------: | :--------------------------------: | :-------------------------------: | :------------------: |
|        3-NN(E)        |            -            |                 -                 |          -          |               -               |                 -                  |                 -                 |          -           |

---
<br/><br/>

## To-Do-List
* Fill Time Comparison Table
* Jetson Nano
* Visualize Tables using Graphs