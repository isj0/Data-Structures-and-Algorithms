import queue


class PrintManager:

    def __init__(self):
        self.queue = queue.Queue()

    def queue_print_job(self, document):
        self.queue.enqueue(document)

    def run(self):
        while self.queue.read():
            self.print_document(self.queue.dequeue())

    def print_document(self, document):
        # Code to run the actual printer goes here.
        # For demo purposes, we'll print to the terminal:
        print(document)
