import threading


class Worker(threading.Thread):

    def __init__(self, target, args=()):

        super().__init__()

        self.target = target

        self.args = args

        self.daemon = True

    def run(self):

        self.target(*self.args)