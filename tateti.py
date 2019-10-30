
class TaTeTi():

    def __init__(self, iniciar = None):
        self.board_i= iniciar
        self.board = [' ' for _ in range(9)]

    def full(self):
        contador=0
        for i in self.board_i:
            if i != ' ':
                contador = contador +1
        if contador == 9:
            return True
        else:
            return False

    def win(self):
        contador_x = 0
        contador_o = 0
        cadena = ''.join(self.board_i)
        fila = 3
        self.board_i = [ [  cadena[j+(i*3)]  for j in range(fila) ] for i in range(fila)]
        j=0
        for i in range(3):
            if self.board_i[0][i] == 'x':
                contador_x= contador_x +1
            if self.board_i[0][i] == 'o':
                contador_o = contador_o +1
            if self.board_i[1][i] == 'x':
                contador_x= contador_x +1
            if self.board_i[1][i] == 'o':
                contador_o = contador_o +1
            if self.board_i[2][i] == 'x':
                contador_x= contador_x +1
            if self.board_i[2][i] == 'o':
                contador_o = contador_o +1
        if contador_x == 3 or contador_o == 3:
            j=j+1

        for i in range(3):
            if self.board_i[i][0] == 'x':
                contador_x = contador_x + 1
            if self.board_i[i][0] == 'o':
                contador_o = contador_o + 1
            if self.board_i[i][1] == 'x':
                contador_x = contador_x + 1
            if self.board_i[i][1] == 'o':
                contador_o = contador_o + 1
            if self.board_i[i][2] == 'x':
                contador_x = contador_x + 1
            if self.board_i[i][2] == 'o':
                contador_o = contador_o + 1

        if contador_x == 3 or contador_o == 3:
            j=j+1
        if j == 1:
            return True
        else:
            return False


