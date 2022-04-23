from argparse import ArgumentParser


class Parser(ArgumentParser):
    
    def __init__(self):
        super().__init__()
    
    def giveArg(self):
        self.add_argument("-c", "--config", help="Config file", required=True)
        self.add_argument("-l", "--logged", help="Config file", required=True)       
        return self.parse_args()



