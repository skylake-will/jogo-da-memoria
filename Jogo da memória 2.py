import tkinter as tk
from random import shuffle

# inicialização da janela

janela = tk.Tk()
canvas = tk.Canvas(janela, width=500, height=500)
canvas.pack()


class Tile(object):
    def __init__(self, x, y, color):
        self.y = y
        self.x = x
        self.color = color

    def drawFaceDown(self):
        print(self.x, self.y, self.x + 70, self.y + 70)
        canvas.create_rectangle(self.x, self.y, self.x + 70, self.y + 70, fill="grey")
        self.isFaceUp = False

    def drawFaceUp(self):
        canvas.create_rectangle(self.x, self.y, self.x + 70, self.y + 70, fill=self.color)
        canvas.create_text(self.x + 35, self.y + 35, text=self.color, width=70)
        self.isFaceUp = True

    def isUnderMouse(self, event):
        if self.x < event.x < self.x + 70:
            if self.y < event.y < self.y + 70:
                return True


def mouseClicked(self):
    global flippedTiles
    acertou = False
    for i in range(len(tiles)):
        if tiles[i].isUnderMouse(self):
            if len(flippedTiles) < 3 and not tiles[i].isFaceUp:
                tiles[i].drawFaceUp()
                print("vira pra cima")
                flippedTiles.append(tiles[i])
            if len(flippedTiles) == 2:
                if not (flippedTiles[0].color == flippedTiles[1].color):
                    print('não acertou')
                else:
                    print('acertou')
                    acertou = True
            if len(flippedTiles) == 3:
                if acertou or flippedTiles[0].color == flippedTiles[1].color:
                    last = flippedTiles[2]
                    flippedTiles = [last]
                    acertou = False
                    print("continua para cima")

                else:
                    print("vira pra baixo")
                    flippedTiles[0].drawFaceDown()
                    flippedTiles[1].drawFaceDown()
                    last = flippedTiles[2]
                    flippedTiles = []
                    flippedTiles.append(last)


tiles = []
colors = [
    "Red", "Orange", "Yellow", "Green", "Blue", "Purple", "Pink", "Brown", "Magenta", "White",
    "Red", "Orange", "Yellow", "Green", "Blue", "Purple", "Pink", "Brown", "Magenta", "White"
]
shuffle(colors)
flippedTiles = []
NUM_COLS = 5
NUM_ROWS = 4

for x in range(0, NUM_COLS):
    for y in range(0, NUM_ROWS):
        tiles.append(Tile(x * 78 + 10, y * 78 + 40, colors.pop()))

for i in range(len(tiles)):
    tiles[i].drawFaceDown()

janela.bind("<Button-1>", mouseClicked)

janela.mainloop()
