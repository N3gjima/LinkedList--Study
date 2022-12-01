# LinkedList--Study
Este é apenas um estudo de listas encadeadas. 
O estudo foi feito a partir de um vídeo do youtube, o código feito aqui também é do video então todos os créditos são para este video:
https://youtu.be/jIM87UqOq3g
e deste vídeo também:
https://youtu.be/EUUlB4Rmhf0

Então para começar precisamos saber o que são listas, são uma estrutura de dados onde o armazenamento se dá de forma sequencial e assim ocupando o mesmo espaço na memoria. Já as listas encadeadas fogem dessa regra pois o lugar que estão armazenados os dados não necessariamente precisam estar juntos, porque graças a um aritifico, uma parte muito importante da lista encadeada, os nós, o dados não precisam ser sequenciais e nem utilizar o mesmo espaço na memoria.
O que são os nós ?
Eles a parte mais importante da lista encadeada, eles guardam o dado que precisa ser guardado e a localização do próximo nó, graças a isso a lista encadeada normalmente só poderá fazer sua busca sempre para o próximo dado, assim não conseguindo voltar para trás.

Primeiramente para construirmos uma lista encadeada precisaremos do nó e sua classe, ele que guardará o dado e a localização do próximo dado.

class Node:
  def __init__(self,data):
    self.data = data
    self.next = next 

Agora criaremos a classe que criará a lista e depois disso criaremos também uma função nela para introduzirmos o primeiro elemento da lista.
O head será o dado e o size o tamanho da lista, está com os valores, None e 0 sucessivamente porque não há dentro da lista, ainda.

class LinkedList:
  def __init__(self):
    self.head = None
    self.size = 0
    
  def append(self, elem):
    if self.head:
      while(pointer.next):
				  pointer = pointer.next
			 pointer.next = Node(elem)
       
O pointe será uma variavel auxiliar que utilizaremos para não perder os dados que estarão no HEAD.
    
    class LinkedList:
  def __init__(self):
    self.head = None
    self.size = 0
    
  def append(self, elem):
    if self.head:
      while(pointer.next):
				  pointer = pointer.next
			 pointer.next = Node(elem)
    else:
      self.head = Node(elem)
    self.size = self.size + 1
    
O else será para o caso do HEAD estar vázio então um elemento será adicionado nele.
e o size sempre adicionará mais um elemento a sua variavél, para sabermos o tamanho sempre que precisarmos.
Agora que entramos nessa parte de tamanho da lista precisaremos resolver o caso quando for utilizada a função len, é muita facil, dentro da classe LinkedList:

  def __len__(self):
    return self.size
    
criaremos também uma função para que o usuario possa pesquisar um elemento na lista obtenha sua localização na lista,como a linguagem utilizada foi python, ele possibilita uma sobrecarga de operador, que no caso seria o []

  def __getitem__(self,index):
    pointer = self.head                 Com a utilização da variavel auxiliar poderemos assim ir para o próximo nó sem perder o dado do head quando ocorrer essa busca
    for i in range(index):
      if pointer:
        pointer = pointer.next
      else:
        raise IndexError ("List index error out of range")
     if pointer:
      return pointer.data
     else:
      raise IndexError ("list index error out of range")
      
Agora precisaremos de uma função para o caso do usuario querer editar um elemento em um espaço da memoria do nó que não está vazio.

   def __setitem__(self, index, elem):
    pointer = self.head
    for i in range(index):
      if pointer:
        pointer = pointer.next
      else:
        raise IndexError ("List index error out of range")
      if pointer:
        pointer.data = elem             Note que como só queremos qual dado está localizado na posição mudaremos somente a saida.
      else:
        raise IndexError ("List index error out of range")

Como a lista encadeada não é uma lista sequencial precisaremos adaptar uma busca linear nela, para que o usuario consigo fazer sua busca por indexação.

  def index (self,elem):
    pointer = self.head
    i = o
    while (pointer):
      if pointer.data == elem:
        return
        
        
