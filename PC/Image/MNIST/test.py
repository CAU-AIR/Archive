import numpy as np
import avalanche as avl
from torch.nn import CrossEntropyLoss
from torch.optim import SGD
from avalanche.evaluation import metrics as metrics
import torchvision

def main():
    
    benchmark = avl.benchmarks.SplitCIFAR100(n_experiences=10, seed=1, return_task_id=True)

    model = torchvision.models.resnet18(num_classes=100)

    criterion = CrossEntropyLoss()
    optimizer = SGD(model.parameters(), lr=0.0001)

    interactive_logger = avl.logging.InteractiveLogger()
    evaluation_plugin = avl.training.plugins.EvaluationPlugin(
        metrics.accuracy_metrics(epoch=True, experience=True, stream=True),
        metrics.loss_metrics(epoch=True, experience=True, stream=True),
        loggers=[interactive_logger])
    
    cl_strategy = avl.training.JointTraining(
        model, optimizer, criterion,
        train_mb_size=128, train_epochs=2, eval_mb_size=128,
        evaluator=evaluation_plugin)
    
    cl_strategy.train(benchmark.train_stream)
    res = cl_strategy.eval(benchmark.test_stream)


if __name__ == '__main__':
    main()
