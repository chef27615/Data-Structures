import heapq

class Heap:
  def __init__(self):
    self.storage = []

  def insert(self, value):
    # if len(self.storage) is None:
    #   self.storage.append(value)
    self.storage.append(value)
    self._bubble_up(len(self.storage)-1)

  def delete(self):
    if self.storage is None:
      return
    elif len(self.storage) == 1:
      return self.storage.pop()
    top_value = self.storage[-1]
    length = len(self.storage)
    if top_value:
      self.storage.pop()
      if length == 1:
        top_value=self.storage[0]
      else:
        pass

  def get_max(self):
    if len(self.storage) == 0:
      return
    elif len(self.storage) == 1:
      return self.storage[0]
    else:
      heapq.nlargest(1, self.storage)

  def get_size(self):
      return len(self.storage)

  def _bubble_up(self, index):
    length = self.get_size()
    if index<0 or index>length-1:
      return
    heapq.heapify(self.storage)[::-1]



  def _sift_down(self, index):
    pass
