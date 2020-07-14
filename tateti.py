class TaTeTi():
    def __init__(self,valor=None):
        self.board=[' ' for _ in range(9)]
        self.inicio=valor

    def full(self):
        contador=0
        for i in self.inicio:
            if i != ' ':
                contador += 1
        if contador == 9:
            return True
        else:
            return False

    def win(self):
        cont=0
        cont1=0
        for i in self.inicio:
            if i == 'x':
                cont+=1
    
            if i == 'o':
                cont1+=1
            
        if cont == 0 or cont1 == 0:
            return True
        
        else:
            return False
            
    def validate(self,position):
        if 'x' in self.inicio[position-1] or 'o' in self.inicio[position-1]:
            return False
        else:
            return True
            
    def assign(self,position,piece):
        self.board=self.inicio
        if self.validate(position):
            cont=1
            for i in self.board:
                if cont == position:
                    self.board[cont-1]=piece
                cont=cont+1
            return self.board
            
        else:
            raise Exception

    def draw_board(self):
        self.board=self.inicio
        cont=1
        for i in self.board:
            if i == ' ':
              self.board[cont-1]=str(cont)
            cont=cont+1

        printing = "\n"
        for num in range(9):
            if self.board[num] != " ":
                printing += " " + self.board[num] + " "
            else:
                printing += " " + str(1+num) + " "
            if num == 2 or num == 5:
                printing += "\n---+---+---\n"
            elif num == 8:
                printing += "\n"
            else:
                printing += "|"
        return printing
