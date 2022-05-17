'''
    Description ouput for experimental settings
'''

class Info:
    def __init__(self):
        pass

    def info(self):
        if self.reduction_method[1] is not None:
            self.reduction_ratio = round(self.reduction_method[1]/self.feature_size, 3)

        config_list = {
            0 : ['Dataset', self.dataset, "Train size " + str(int((1-self.test_size)*100))+"%", 'Feature size: ' + str(self.feature_size), 1],
            1 : ['Method', self.method, 2],
            2 : ['Dimension reduction', 
                 'Method: ' + str(self.reduction_method[0]),
                 'Component size: ' + str(self.reduction_method[1]),
                 'Feature Reduction Ratio: ' + str(self.reduction_ratio*100)+"%" if self.reduction_ratio is not None else 'Feature Reduction Ratio: ' + str(None), 3],
            3 : ['Iteration', str(self.iter), -1]
        }

        print("Device " + "─" * 2 + " " + self.device)
        print("│")

        parent = 1
        for child in range(len(config_list)):
            for idx, contents in enumerate(config_list[child][:-1]):
                if idx == 0 and child == len(config_list)-1:
                    print("└" + "─" * 2 + contents)
                elif idx == 0:
                    print("├" + "─" * 2 + contents)
                elif child == len(config_list)-1:
                    print(" " * 4 + "└" + "─" * 4 + contents)
                else:
                    print("│" + " " * 4 + "└" + "─" * 4 + contents)
            parent = config_list[child][-1]
            if parent == -1: break
            print("│")
        
    def print_rutin(self):
        if self.reduction_method[0] is None:
            rutin = str(self.device) + " - " + str(self.dataset) + "(" + str(int((1-self.test_size)*100)) + "%) - " + str(self.method) + " - " + str(self.iter) + " iteration"
            print(rutin)
        else:
            rutin = str(self.device) + " - " + str(self.dataset) + "(" + str(int((1-self.test_size)*100)) + "%) - " + str(self.method) + " - " + str(self.iter) + " iteration - " + str(self.reduction_method[0]) + "(reduction : " + str(self.reduction_method[1]) + "%)"
            print(rutin)