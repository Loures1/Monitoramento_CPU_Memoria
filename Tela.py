import PySimpleGUI as sg
import Monitoramento

GRAPH_SIZE = (120, 54)
DATA_SIZE = (120, 54)
STEP_SIZE = 2
DELAY = 1000
    

cpu_graph = [sg.Graph(GRAPH_SIZE, (0, 0), DATA_SIZE, background_color = 'white', key = 'cpu_graph')]
botao_cpu = [sg.Button('CPU')]
memoria_graph = [sg.Graph(GRAPH_SIZE, (0, 0), DATA_SIZE, background_color = 'white', key = 'memoria_graph')]
botao_memoria = [sg.Button('Memória')]

coluna1 =  [
            [sg.Column([cpu_graph], element_justification='c'), sg.Column([botao_cpu], element_justification='c')],
            [sg.Column([memoria_graph], element_justification='c'), sg.Column([botao_memoria], element_justification='c')]                
]

coluna2 =   [       
            [sg.Text('', key = 'titulo')],                                                                                                                     
            [sg.Text('%utilização                                                                                                                                   100%')],
            [sg.Frame('', [[sg.Graph((GRAPH_SIZE[0]*5, GRAPH_SIZE[1]*5), (0, 0), (DATA_SIZE[0]*5, DATA_SIZE[1]*5), key = 'graph')]])],
            [sg.Text('60 segudos                                                                                                                                       0')]
]          
layout =    [
            [sg.Column(coluna1, vertical_alignment = 't'), sg.Column(coluna2, vertical_alignment = 't')]
]

window = sg.Window('Monitoramento', layout)

step_size = STEP_SIZE
graph_cpu = False
graph_memoria = False
auto = 0
lasty = 0

while True:
    event, values = window.read(timeout = DELAY, timeout_key= 1)

    if event == sg.WIN_CLOSED:
        break
    
    if type(event) == int:
        auto += event

    x, y = GRAPH_SIZE[0], (Monitoramento.CPU()*GRAPH_SIZE[1])/100
    lastx = GRAPH_SIZE[0] - step_size
    window['cpu_graph'].Move(-step_size, 0)
    window['cpu_graph'].draw_line((lastx, lasty), (x, y), width=1)
    lasty= y


window.close()