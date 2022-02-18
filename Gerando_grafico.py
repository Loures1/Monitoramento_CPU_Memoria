import PySimpleGUI as sg

class Grafico:
    def __init__(self, nome = '', graph_size = [], origem = [], data_size = [], step_size = 0, cor = ''):
        self.nome = nome
        self.graph_size = graph_size
        self.origem = origem 
        self.data_size = data_size
        self.step_size = step_size
        self.cor = cor    
        self.graph = sg.Graph(self.graph_size, (0, 0), self.data_size, background_color = self.cor, key = self.nome)
        self.x = self.x = self.graph_size[0]
        self.lastx = self.graph_size[0] - self.step_size 
        self.lasty = [0]

    def escrevendo_Grafico(self, y):
        self.y = (y*self.graph_size[1])/100

        