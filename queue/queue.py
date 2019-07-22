class Queue:
  def __init__(self):
    self.size = 0
    # what data structure should we
    # use to store queue elements?
    self.storage = []


  def enqueue(self, item):
    self.item = item
    return self.storage.append(item)
  
  def dequeue(self):
    if len(self.storage) > 0:
      return self.storage.pop(0)
    elif len(self.storage) == 0 :
      return None
    else:
      return self.storage
    

  def len(self):
    return len(self.storage)
