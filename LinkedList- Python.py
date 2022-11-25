

class Node :
  def __init__(self, data):
    self.data = data
    self.next = None

class LinkedList:
  def __init__(self):
    self.head = None
    self._size = 0
    
  def append(self, elem):
    #Adiciona novos elementos a lista quando já há elementos
    if self.head:
      while(pointer.next):
        pointer = pointer.next
      pointer.next = Node(elem)
    
    
    else:
      self.head = Node(elem)
    self._size =self._size + 1
    
    #retorna o tamanho da lista utilizando a função (len)
  def __len__(self):
    return self._size
  #previsão de sobrecarga de operador
  def __getitem__(self, index):
    pointer = self.head
    for i in range(index):
      if pointer:
        pointer = pointer. next
      else:
        raise IndexError("List index error out of range")
