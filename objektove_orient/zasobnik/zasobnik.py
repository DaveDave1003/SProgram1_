class Node:
    def __init__(self, value):
        self.value = value
        self.next = None





class Stack:
    def __init__(self):
        self.top = None
    
    
    def push(self, prvek):
        # Přidá prvek na vrchol zásobníku
        if self.isEmpty():
            novy_top = Node(prvek)
            self.top = novy_top
        
        else:
            novy_top = Node(prvek)
            novy_top.next = self.top
            self.top = novy_top
        

    def isEmpty(self):
        # Vrátí True pokud je prázdný, jinak False
        if self.top is None:
            return True

        else:
            return False
        
   
    def pop(self):
        if self.isEmpty():
            return None
        elif self.top.next is None:
            value = self.top.value
            self.top = None
            return None
        else:
            value = self.top.value
            self.top = self.top.next
            return value
        # Odebere a vrátí prvek z vrcholu
        # Nezapomeň zkontrolovat, jestli není prázdný!
    
    def peek(self):
        if(self.isEmpty()):
            return  None
        return self.top.value
    
    def size(self):
        return self.top.size()

    def __str__(self):
        pass
    
    def clear(self):
        self.top = None




    def size(self):
        if(self.next):
            return self.next.size() + 1
        return 1
    



