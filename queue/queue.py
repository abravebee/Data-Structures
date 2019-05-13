class Queue:
  def __init__(self):
    self.size = 0
    # what data structure should we
    # use to store queue elements?
    self.storage = []

  def enqueue(self, item):
    self.storage.append(item)
    print(f"Enqueued")
    pass
  
  def dequeue(self):
    if self.storage:
        item = self.storage.pop(0)
        print(f"Dequeued")
        return item
    pass

  def len(self):
    return len(self.storage)
    pass
