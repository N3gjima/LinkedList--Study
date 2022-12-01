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
    
