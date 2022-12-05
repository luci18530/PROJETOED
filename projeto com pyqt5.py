# A program to create visualizations of the data structures (linked lists, sequential lists, stacks, queues, binary search trees) 
# PROJETO DE ESTRUTURA DE DADOS
# Grupo: Guilherme Nogueira, Luciano Pereira, Pedro Lucas, Thais Melquiades, Vitoria Grisi
import PyQt5
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.Qt import *
import sys



# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
ORANGE = (255, 165, 0)
PURPLE = (128, 0, 128)

# LISTA ENCADEADA | LINKED LIST (USING PYTHON BUILD-IN LIST)
class LinkedList:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)

    def add(self, item):
        self.items.append(item)

    # def remove, if value is not in the list, do nothing
    def remove(self, item):
        if item in self.items:
            self.items.remove(item)

    def search(self, item):
        return item in self.items

    def index(self, item):
        return self.items.index(item)

    def pop(self, pos):
        return self.items.pop(pos)

    def insert(self, pos, item):
        self.items.insert(pos, item)

    def __str__(self):
        return str(self.items)
    
    def __repr__(self):
        return str(self.items)
    # get a value from the list by index
    def get(self, index):
        return self.items[index]

    def searchandmatch(self, item):
        if item in self.items:
            return self.items.index(item)
        else:
            return -1
    
    
# FILAS | QUEUES
class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        # if the queue is not empty, remove the first element
        if not self.isEmpty():
            return self.items.pop()

    def size(self):
        return len(self.items)

    def get(self, index):
        # if the queue is not empty, return the element at the index
        if not self.isEmpty():
            return self.items[index]

    def __str__(self):
        return str(self.items)
    
    def __repr__(self):
        return str(self.items)

# PILHAS | STACKS
class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        # if the stack is not empty, remove the last element
        if not self.isEmpty():
            return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)
    
    def __repr__(self):
        return str(self.items)

# ARVORE BINARIA DE BUSCA | BINARY SEARCH TREE
class Node(object):
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None

    def insert(self, data):
        ''' For inserting the node '''
        if self.data:
            if data < self.data:
                if self.leftChild is None:
                    self.leftChild = Node(data)
                else:
                    self.leftChild.insert(data)
            elif data > self.data:
                if self.rightChild is None:
                    self.rightChild = Node(data)
                else:
                    self.rightChild.insert(data)
        else:
            self.data = data

        

    def minValueNode(self, node):
        current = node

        # loop down to find the leftmost leaf
        while(current.leftChild is not None):
            current = current.leftChild

        return current

    def maxValueNode(self, node):
        current = node

        # loop down to find the leftmost leaf
        while(current.rightChild is not None):
            current = current.rightChild

        return current


    def delete(self, data,root):
        ''' For deleting the node '''
        if self is None:
            return None

        # if current node's data is less than that of root node, then only search in left subtree else right subtree
        if data < self.data:
            self.leftChild = self.leftChild.delete(data,root)
        elif data > self.data:
            self.rightChild = self.rightChild.delete(data,root)
        else:
            # deleting node with one child
            if self.leftChild is None:

                if self == root:
                    temp = self.minValueNode(self.rightChild)
                    self.data = temp.data
                    self.rightChild = self.rightChild.delete(temp.data,root) 

                temp = self.rightChild
                self = None
                return temp
            elif self.rightChild is None:

                if self == root:
                    temp = self.maxValueNode(self.leftChild)
                    self.data = temp.data
                    self.leftChild = self.leftChild.delete(temp.data,root) 

                temp = self.leftChild
                self = None
                return temp

            # deleting node with two children
            # first get the inorder successor
            temp = self.minValueNode(self.rightChild)
            self.data = temp.data
            self.rightChild = self.rightChild.delete(temp.data,root)

        return self

    def find(self, data):
        ''' This function checks whether the specified data is in tree or not '''
        if(data == self.data):
            return True
        elif(data < self.data):
            if self.leftChild:
                return self.leftChild.find(data)
            else:
                return False
        else:
            if self.rightChild:
                return self.rightChild.find(data)
            else:
                return False

    def preorder(self):
        '''For preorder traversal of the BST '''
        if self:
            print(str(self.data), end = ' ')
            if self.leftChild:
                self.leftChild.preorder()
            if self.rightChild:
                self.rightChild.preorder()

    def inorder(self):
        ''' For Inorder traversal of the BST '''
        if self:
            if self.leftChild:
                self.leftChild.inorder()
            print(str(self.data), end = ' ')
            if self.rightChild:
                self.rightChild.inorder()


    def postorder(self):
        ''' For postorder traversal of the BST '''
        if self:
            if self.leftChild:
                self.leftChild.postorder()
            if self.rightChild:
                self.rightChild.postorder()
            print(str(self.data), end = ' ')

    def size(self):
        ''' For finding the size of the BST '''
        if self is None:
            return 0
        else:
            return self.leftChild.size() + 1 + self.rightChild.size()

    # Recursive method used to draw the tree in the GUI

    def __str__(self) -> str:
        return str(self.data)

    def __repr__(self) -> str:
        return str(self.data)

        

class Tree(object):
    def __init__(self):
        self.root = None
        self.size = 0

    def sort (self):
        if self.root is None:
            return []
        else:
            return self.root.recursive_sort([])

    def insert(self, data):
        if self.root:
            self.size = self.size + 1
            return self.root.insert(data)
        else:
            self.root = Node(data)
            self.size = self.size + 1
            return True

    def delete(self, data):
        if self.root is not None:
            return self.root.delete(data,self.root)

    def find(self, data):
        if self.root:
            return self.root.find(data)
        else:
            return False

    def preorder(self):
        if self.root is not None:
            print()
            print('Preorder: ')
            self.root.preorder()

    def inorder(self):
        print()
        if self.root is not None:
            print('Inorder: ')
            self.root.inorder()

    def postorder(self):
        print()
        if self.root is not None:
            print('Postorder: ')
            self.root.postorder()

    def __str__(self):
        return str(self.root)

    def __repr__(self):
        return str(self.root)

    def size (self):
        if self.root is not None:
            return self.root.size()

    # tree print function, get the widget
    def treeprint(self, widget):
        if self.root is not None:
            return self.printTree(self.root, widget)

    def printTree(self, currentnode, widget, level = 0, position = None):
        if currentnode is not None:
            
            self.printTree(currentnode.rightChild, widget, level + 1, 'R')
            if position == 'R':
                print('    ' * level, ' / ', currentnode.data)
                buttonarvore = QPushButton(currentnode.data, widget)
                buttonarvore.setStyleSheet("background-color: blue; color: white; font-size: 10px; font-weight: bold;")
                buttonarvore.move(10 + level*50,350 - 200/(level+1))
                buttonarvore.resize(50, 30)
                buttonarvore.show()
            elif position == 'L':
                print('    ' * level, ' \\ ', currentnode.data)
                buttonarvore = QPushButton (currentnode.data, widget)
                buttonarvore.setStyleSheet("background-color: blue; color: white; font-size: 10px; font-weight: bold;")
                buttonarvore.move(10 + level*50,350 + 200/(level+1))
                buttonarvore.resize(50, 30)
                buttonarvore.show()
            else:
                print(currentnode.data)
                buttonarvore = QPushButton (currentnode.data , widget)
                buttonarvore.setStyleSheet("background-color: blue; color: white; font-size: 10px; font-weight: bold;")
                buttonarvore.move(10,350)
                buttonarvore.resize(50, 30)
                buttonarvore.show()
            self.printTree(currentnode.leftChild, widget, level + 1, 'L')
            
            
        


    
    
        


liste = LinkedList()
# LISTA LISTA LISTA LISTA
class janelalista(QWidget):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("background-color: black;")
        labellista = QLabel(self)
        labellista.setText("Lista Encadeada")
        labellista.setStyleSheet("color: white; font-size: 20px; font-weight: bold;")
        labellista.move(10, 10)

        labelentrada = QLabel(self)
        labelentrada.setText("Adicionar elemento")
        labelentrada.setStyleSheet("color: white; font-size: 15px; font-weight: bold;")
        labelentrada.move(10, 40)

        labelremover = QLabel(self)
        labelremover.setText("Remover elemento")
        labelremover.setStyleSheet("color: white; font-size: 15px; font-weight: bold;")
        labelremover.move(460, 40)

        labelconsutar = QLabel(self)
        labelconsutar.setText("Consultar elemento")
        labelconsutar.setStyleSheet("color: white; font-size: 15px; font-weight: bold;")
        labelconsutar.move(10, 90)

        self.inputlista()
        self.consultarlista()
        #self.inputconsultar()   
        self.inputlistaposition()
        self.removedalistabutton()
        self.removedalista()
        self.removedalistaposicao()

        # add button
        addbutton = QPushButton('Adicionar', self)
        addbutton.setStyleSheet("background-color: #008A00; color: white; font-size: 15px; font-weight: bold;")
        addbutton.move(320, 50)
        addbutton.resize(100, 30)
        addbutton.clicked.connect(self.addbutton_clicked)

        self.initUI()
        
    def initUI(self):
        self.setGeometry(10, 30, 1050, 700)
        self.setWindowTitle('Lista Encadeada')
        self.show()

    def consultarlista(self):
        self.consultarlista = QLineEdit(self)
        self.consultarlista.move(10, 120)
        self.consultarlista.resize(200, 20)
        self.consultarlista.setObjectName("consultarlista")
        self.consultarlista.setStyleSheet("background-color: black; color: white; font-size: 15px; font-weight: bold;")
        self.consultarlista.setPlaceholderText("Digite o elemento a ser consultado")

        buttonconsultar = QPushButton('Consultar', self)
        buttonconsultar.setStyleSheet("background-color: #008A00; color: white; font-size: 15px; font-weight: bold;")
        buttonconsultar.move(220, 120)
        buttonconsultar.resize(100, 20)
        buttonconsultar.clicked.connect(self.buttonconsultar_clicked)

    def buttonconsultar_clicked(self):
        print('Consultar')
        self.consultarlista = self.findChild(QLineEdit, 'consultarlista')
        print(self.consultarlista.text())
        estalanista = liste.searchandmatch(self.consultarlista.text())
        print(estalanista)

        # if the element is in the list show a message in the screen
        if estalanista >= 0:
            msg = QMessageBox()
            msg.setWindowTitle("Elemento encontrado")
            msg.setText("O elemento está na lista, na posição: "+str(liste.searchandmatch(self.consultarlista.text())))
            msg.setIcon(QMessageBox.Information)
            msg.exec_()

        # if the element is not in the list show a message in the screen
        else:
            msg = QMessageBox()
            msg.setWindowTitle("Elemento não encontrado")
            msg.setText("O elemento não está na lista")
            msg.setIcon(QMessageBox.Information)
            msg.exec_()

    def inputlista(self):
        entrada = QLineEdit(self)
        entrada.move(10, 60)
        entrada.resize(200, 20)
        entrada.setObjectName("entrada")
        entrada.setStyleSheet("color: white;")
        entrada.setPlaceholderText("Digite um valor")
        entrada.textChanged.connect(self.onchanged) # Certifica que o texto foi alterado 

    def inputlistaposition(self):
        entradaposicao = QLineEdit(self)
        entradaposicao.move(220, 60)
        entradaposicao.resize(81, 20)
        entradaposicao.setObjectName("entradaposicao")
        entradaposicao.setStyleSheet("color: white;")
        entradaposicao.setPlaceholderText("Digite a posição")
        entradaposicao.textChanged.connect(self.onchanged)

    # now create a button for remotion (red color with white text)
    def removedalistabutton(self):
        removedalistabutton = QPushButton('Remover', self)
        removedalistabutton.setStyleSheet("background-color: #FF0000; color: white; font-size: 15px; font-weight: bold;")
        removedalistabutton.move(780, 50)
        removedalistabutton.resize(100, 30)
        removedalistabutton.clicked.connect(self.removedalistabutton_clicked)

    def removedalista(self):
        entradaremove = QLineEdit(self)
        entradaremove.move(460, 60)
        entradaremove.resize(200, 20)
        entradaremove.setObjectName("entradaremove")
        entradaremove.setStyleSheet("color: white;")
        entradaremove.setPlaceholderText("Digite o valor a remover")
        entradaremove.textChanged.connect(self.onchanged)

    def removedalistaposicao(self):
        entradaremoveposicao = QLineEdit(self)
        entradaremoveposicao.move(670, 60)
        entradaremoveposicao.resize(95, 20)
        entradaremoveposicao.setObjectName("entradaremoveposicao")
        entradaremoveposicao.setStyleSheet("color: white;")
        entradaremoveposicao.setPlaceholderText("Posição a remover")
        entradaremoveposicao.textChanged.connect(self.onchanged)

    def addbutton_clicked(self):
        print("add button clicked")

        textoparainput = self.findChild(QLineEdit, 'entrada').text()
        # if there is no text in the input, do nothing
        if textoparainput == "":
            return

        posicao = self.findChild(QLineEdit, 'entradaposicao').text()
        # if there is no text in the input, do nothing
        if posicao == "":
            return

        # if position is not a number, do nothing
        if not posicao.isnumeric():
            return

        liste.insert(int(posicao), textoparainput)

        button = []

        
        for i in range(liste.size()):       
            # create a list of buttons (SERVE PRA PILHA E FILA, LISTA É FEIO) SIMBORAAAAAAAA           
            button = QPushButton(str(liste.get(i)), self)
            button.setStyleSheet("background-color: #008A00; color: white; font-size: 15px; font-weight: bold;")
            button.move(10 + i * 50, 400)  
            button.resize(50, 30)
            button.show()

        print(liste)
        print("posicao =", posicao)

    def imageblackbmp(self):
        imageblack = QLabel(self)
        imageblack.setPixmap(QPixmap("black.bmp"))
        imageblack.move(10, 200)
        imageblack.resize(600, 600)
        imageblack.show()

    def removedalistabutton_clicked(self):
        print("remove button clicked")
        textoparainput = self.findChild(QLineEdit, 'entradaremove').text()
        posicaoremover = self.findChild(QLineEdit, 'entradaremoveposicao').text()
        # if there is no text in the input, do nothing
        if textoparainput == "" and posicaoremover == "":
            print("nenhum valor digitado")
            return
        if textoparainput != "" and posicaoremover != "":
            print("digite apenas um valor")
            return
        if textoparainput != "" and posicaoremover == "":
            print("removendo por valor")

            liste.remove(textoparainput)
            print("tam lista ",liste.size())
            self.imageblackbmp()

            for i in range(liste.size()):       
            # create a list of buttons (SERVE PRA PILHA E FILA, LISTA É FEIO) SIMBORAAAAAAAA
                
                
                button = QPushButton(str(liste.get(i)), self)
                # set id for each button
                button.setObjectName(str(i))
                button.setStyleSheet("background-color: #008A00; color: white; font-size: 15px; font-weight: bold;")
                button.move(10 + i * 50, 400)  
                button.resize(50, 30)
                button.show()

        if posicaoremover != "" and textoparainput == "":
            print("removendo por posição")
            print(liste.size())
            # if the position is not a number, do nothing
            if not posicaoremover.isnumeric():
                return
            # if the position is not in the list, do nothing
            if int(posicaoremover) >= liste.size():
                return
            print(posicaoremover)
            liste.pop(int(posicaoremover))

            self.imageblackbmp()

            for i in range(liste.size()):       
            # create a list of buttons (SERVE PRA PILHA E FILA, LISTA É FEIO) SIMBORAAAAAAAA
                # LOAD IMAGE
                print("i =", i)

                button = QPushButton(str(liste.get(i)), self)
                # set id for each button
                button.setObjectName(str(i))
                button.setStyleSheet("background-color: #008A00; color: white; font-size: 15px; font-weight: bold;")
                button.move(10 + i * 50, 400)  
                button.resize(50, 30)
                button.show()

            print(liste)
  
    def onchanged(self, text):
        print(text)

# JANELA FILA FILA FILA FILA FILA
class janelafila(QWidget):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("background-color: black;")
        labelfila = QLabel(self)
        labelfila.setText("Fila")
        labelfila.setStyleSheet("color: white; font-size: 20px; font-weight: bold;")
        labelfila.move(10, 10)

        labelenfileirar = QLabel(self)
        labelenfileirar.setText("Enfileirar elemento")
        labelenfileirar.setStyleSheet("color: white; font-size: 15px; font-weight: bold;")
        labelenfileirar.move(10, 40)

        labelprimeirofila = QLabel(self)
        labelprimeirofila.setText("Primeiro da fila")
        labelprimeirofila.setStyleSheet("color: white; font-size: 15px; font-weight: bold;")
        labelprimeirofila.move(10, 500)

        enqueuebutton = QPushButton('Enfileirar', self)
        enqueuebutton.setStyleSheet("background-color: #008A00; color: white; font-size: 15px; font-weight: bold;")
        enqueuebutton.move(320, 50)
        enqueuebutton.resize(100, 30)
        enqueuebutton.clicked.connect(self.enqueuebutton_clicked)

        dequeuebutton = QPushButton('Desenfileirar', self)
        dequeuebutton.setStyleSheet("background-color: red; color: white; font-size: 15px; font-weight: bold;")
        dequeuebutton.move(320, 90)
        dequeuebutton.resize(100, 30)
        dequeuebutton.clicked.connect(self.dequeuebutton_clicked)

        self.inputfila()
        self.initUI()
        
    def initUI(self):
        self.setGeometry(10, 30, 1050, 700)
        self.setWindowTitle('Fila')
        self.show()

    def inputfila(self):
        entradafila = QLineEdit(self)
        entradafila.move(10, 60)
        entradafila.resize(300, 20)
        entradafila.setObjectName("entradafila")
        entradafila.setStyleSheet("color: white;")
        entradafila.setPlaceholderText("Digite o valor")
        
    def enqueuebutton_clicked(self):
        print("enqueue button clicked")
        textoparainputfila = self.findChild(QLineEdit, 'entradafila').text()
        # if there is no text in the input, do nothing
        if textoparainputfila == "":
            return

        fila.enqueue(textoparainputfila)
        lastelement = fila.get(fila.size() - 1)
        print(fila)
        for i in range (fila.size()):
            button = QPushButton(str(fila.get(i)), self)
            # set id for each button
            button.setObjectName(str(i))
            button.setStyleSheet("background-color: #008A00; color: white; font-size: 15px; font-weight: bold;")
            button.move(10 + i * 50, 400)  
            button.resize(50, 30)
            button.show()

        # show a button that shows the first element of the queue 
        button = QPushButton(str(lastelement), self)
        button.setObjectName("primeirofila")
        button.setStyleSheet("background-color: orange; color: white; font-size: 15px; font-weight: bold;")
        button.move(10, 530)
        button.resize(50, 30)
        button.show()


    def dequeuebutton_clicked(self):
        print("dequeue button clicked")
        fila.dequeue()
        print(fila)
        self.imageblackbmp()
        for i in range (fila.size()):
            button = QPushButton(str(fila.get(i)), self)
            # set id for each button
            button.setObjectName(str(i))
            button.setStyleSheet("background-color: #008A00; color: white; font-size: 15px; font-weight: bold;")
            button.move(10 + i * 50, 400)  
            button.resize(50, 30)
            button.show()

        lastelement = fila.get(fila.size() - 1)
        print("checgou aqui")
        labelprimeirofila = QLabel(self)
        labelprimeirofila.setText("Primeiro da fila")
        labelprimeirofila.setStyleSheet("color: white; font-size: 15px; font-weight: bold;")
        labelprimeirofila.move(10, 500)
        labelprimeirofila.show()

        button = QPushButton(str(lastelement), self)
        button.setObjectName("primeirofila")
        button.setStyleSheet("background-color: orange; color: white; font-size: 15px; font-weight: bold;")
        button.move(10, 530)
        button.resize(50, 30)
        button.show()

    def imageblackbmp(self):
        imageblack = QLabel(self)
        imageblack.setPixmap(QPixmap("black.bmp"))
        imageblack.move(10, 200)
        imageblack.resize(600, 600)
        imageblack.show()

listadaarvore = []

# ARVORE ARVORE ARVORE ARVORE ARVORE
class janelaarvore(QWidget):
    def __init__(self):
        super().__init__()
        arvore = Tree()
        self.setStyleSheet("background-color: black;")
        labelarvore = QLabel(self)
        labelarvore.setText("Árvore")
        labelarvore.setStyleSheet("color: white; font-size: 20px; font-weight: bold;")
        labelarvore.move(10, 10)

        labelinserir = QLabel(self)
        labelinserir.setText("Inserir elemento")
        labelinserir.setStyleSheet("color: white; font-size: 15px; font-weight: bold;")
        labelinserir.move(10, 40)

        self.inputarvore()

        buttoninserir = QPushButton('Inserir', self)
        buttoninserir.setStyleSheet("background-color: #008A00; color: white; font-size: 15px; font-weight: bold;")
        buttoninserir.move(320, 50)
        buttoninserir.resize(100, 30)
        buttoninserir.clicked.connect(self.buttoninserir_clicked)

        labelremover = QLabel(self)
        labelremover.setText("Remover elemento")
        labelremover.setStyleSheet("color: white; font-size: 15px; font-weight: bold;")
        labelremover.move(450, 40)

        self.removedaarvore()

        buttonremover = QPushButton('Remover', self)
        buttonremover.setStyleSheet("background-color: red; color: white; font-size: 15px; font-weight: bold;")
        buttonremover.move(730, 50)
        buttonremover.resize(100, 30)

        buttoninordem = QPushButton('In-ordem', self)
        buttoninordem.setStyleSheet("background-color: #008A00; color: white; font-size: 15px; font-weight: bold;")
        buttoninordem.move(10, 90)
        buttoninordem.resize(100, 30)

        labelpesquisa = QLabel(self)
        labelpesquisa.setText("Pesquisar elemento")
        labelpesquisa.setStyleSheet("color: white; font-size: 15px; font-weight: bold;")
        labelpesquisa.move(10, 130)

        self.inputpesquisa()

        buttonpesquisa = QPushButton('Pesquisar', self)
        buttonpesquisa.setStyleSheet("background-color: #008A00; color: white; font-size: 15px; font-weight: bold;")
        buttonpesquisa.move(320, 140)
        buttonpesquisa.resize(100, 30)

        self.initUI()
    
    def initUI(self):
        self.setGeometry(10, 30, 1050, 700)
        self.setWindowTitle('Árvore')
        self.show()

    def inputarvore(self):
        entradaarvore = QLineEdit(self)
        entradaarvore.move(10, 60)
        entradaarvore.resize(300, 20)
        entradaarvore.setObjectName("entradaarvore")
        entradaarvore.setStyleSheet("color: white;")
        entradaarvore.setPlaceholderText("Digite o valor")

    def inputpesquisa(self):
        entradaarvore = QLineEdit(self)
        entradaarvore.move(10, 150)
        entradaarvore.resize(300, 20)
        entradaarvore.setObjectName("entradaarvore")
        entradaarvore.setStyleSheet("color: white;")
        entradaarvore.setPlaceholderText("Digite o valor")

    def removedaarvore(self):
        removedaarvore = QLineEdit(self)
        removedaarvore.move(450, 60)
        removedaarvore.resize(270, 20)
        removedaarvore.setObjectName("removedaarvore")
        removedaarvore.setStyleSheet("color: white;")
        removedaarvore.setPlaceholderText("Digite o valor")

    def imageblackbmp(self):
        imageblack = QLabel(self)
        imageblack.setPixmap(QPixmap("black.bmp"))
        imageblack.move(10, 200)
        imageblack.resize(600, 600)
        imageblack.show()

    def buttoninserir_clicked(self):
        entradaarvore = self.findChild(QLineEdit, "entradaarvore")
        valor = entradaarvore.text()
        listadaarvore.append(valor)
        arvore.insert(valor)
        # SORT LISTADAARVORE
        #listadaarvore.sort()
        print(listadaarvore)
        # print the value of arvore in text
        print(str(arvore.root))
        # print size
        print("size: ",arvore.size)
        # TREE PRINTER
        print("Tree:")
        self.imageblackbmp()

        for i in range (0, len(listadaarvore)):
            button = QPushButton(str(listadaarvore[i]), self)
            button.setObjectName("arvore")
            button.setStyleSheet("background-color: orange; color: white; font-size: 15px; font-weight: bold;")
            # if value of i is 0, the button will be in the top of the tree
            if i == 0:
                button.move(500, 200)
            # if value of i is 1, the button will be in the left of the tree
            elif listadaarvore[i] < listadaarvore[i-1]:
                button.move(300, 300)
            # if value of i is 2, the button will be in the right of the tree
            elif listadaarvore[i] > listadaarvore[i-1]:
                button.move(700, 300)
            # if value of i is 3, the button will be in the left of the left of the tree
            elif listadaarvore[i] < listadaarvore[i-2]:
                button.move(300, 400)
            # if value of i is 4, the button will be in the right of the left of the tree
            elif listadaarvore[i] > listadaarvore[i-2]:
                button.move(600, 400)
            # if value of i is 5, the button will be in the left of the right of the tree
            elif i == 5:
                button.move(700, 280)
            # if value of i is 6, the button will be in the right of the right of the tree
            elif i == 6:
                button.move(900, 280)
            # if value of i is 7, the button will be in the left of the left of the left of the tree
            elif i == 7:
                button.move(200, 320)
            # if value of i is 8, the button will be in the right of the left of the left of the tree
            elif i == 8:
                button.move(400, 320)
            # if value of i is 9, the button will be in the left of the right of the left of the tree
            elif i == 9:
                button.move(600, 320)
            # if value of i is 10, the button will be in the right of the right of the left of the tree
            elif i == 10:
                button.move(800, 320)
            # if value of i is 11, the button will be in the left of the left of the right of the tree
            elif i == 11:
                button.move(1000, 320)
            # if value of i is 12, the button will be in the right of the left of the right of the tree
            elif i == 12:
                button.move(1200, 320)
            # if value of i is 13, the button will be in the left of the right of the right of the tree
            elif i == 13:
                button.move(1400, 320)
            # if value of i is 14, the button will be in the right of the right of the right of the tree
            elif i == 14:
                button.move(1600, 320)
            # if value of i is 15, the button will be in the left of the left of the left of the left of the tree
            elif i == 15:
                button.move(100, 360)
            # if value of i is 16, the button will be in the right of the left of the left of the left of the tree
            elif i == 16:
                button.move(300, 360)

            button.resize(50, 30)
            button.show()
        #|arvore.treeprint(self)
        
        





        

    def printTreeinButton(self, level = 0):
        # print all the elements in the arvore
        gfg = 1


        
class janelamain(QMainWindow):
    def __init__(self):
        super().__init__()
        # set background color to black
        self.setStyleSheet("background-color: black;")
        self.left = 10
        self.top = 30
        self.width = 1050
        self.height = 700
        self.title = 'Estrutura de Dados'
        exit_button = QPushButton('SAIR', self)
        exit_button.move(1000, 660)
        exit_button.resize(50, 40)
        exit_button.setStyleSheet("background-color: red; color: white; font-weight: bold; font-size: 15px; font-family: Lucida Sans Unicode")
        exit_button.clicked.connect(self.close)

        self.label1()
        self.lista()
        self.pilha()
        self.fila()
        self.arvore()      
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.show()

    def label1(self):
        label1 = QLabel('Visualizador de Estrutura de Dados', self)
        # move to the center top of the window
        label1.setAlignment(Qt.AlignCenter | Qt.AlignVCenter)
        label1.resize(600, 40)
        label1.setStyleSheet("background-color: black; color: white; font-weight: bold; font-size: 32px; font-family: Lucida Sans Unicode; font-style: italic")
        label1.show()

    def lista(self):
        lista_button = QPushButton('Lista Encadeada', self)
        lista_button.move(10, 60)
        lista_button.resize(200, 40)
        lista_button.setStyleSheet("background-color: blue; color: white; font-weight: bold; font-size: 15px; font-family: Lucida Sans Unicode")
        lista_button.clicked.connect(self.listaclick)

    def listaclick(self):
        print('Lista Encadeada')
        self.lista = janelalista()

    def pilha(self):
        pilha_button = QPushButton('Pilha', self)
        pilha_button.move(10, 110)
        pilha_button.resize(200, 40)
        pilha_button.setStyleSheet("background-color: blue; color: white; font-weight: bold; font-size: 15px; font-family: Lucida Sans Unicode")
        pilha_button.clicked.connect(self.pilhaclick)
    
    def pilhaclick(self):
        print('Pilha')

    def fila(self):
        fila_button = QPushButton('Fila', self)
        fila_button.move(10, 160)
        fila_button.resize(200, 40)
        fila_button.setStyleSheet("background-color: blue; color: white; font-weight: bold; font-size: 15px; font-family: Lucida Sans Unicode")
        fila_button.clicked.connect(self.filaclick)

    def filaclick(self):
        print('Fila')
        print(self.objectName())
        self.fila = janelafila()

    def arvore(self):
        arvore_button = QPushButton('Arvore', self)
        arvore_button.move(10, 210)
        arvore_button.resize(200, 40)
        arvore_button.setStyleSheet("background-color: blue; color: white; font-weight: bold; font-size: 15px; font-family: Lucida Sans Unicode")
        arvore_button.clicked.connect(self.arvoreclick)
    
    def arvoreclick(self):
        self.arvore = janelaarvore()
        print('Arvore')

textoparainput = ''
posicao = 0

fila = Queue()
pilha = Stack()
arvore = Tree()
application = PyQt5.QtWidgets.QApplication(sys.argv)
janela = janelamain()
sys.exit(application.exec_())