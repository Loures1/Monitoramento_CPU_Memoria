import PySimpleGUI as sg
import Monitoramento

GRAPH_SIZE = (600, 270)
DATA_SIZE = (600, 270)
DELAY = 1000


coluna1 =   [
            [sg.Button('CPU')],
            [sg.Button('Memória')]
]

coluna2 =   [       
            [sg.Text('', key = 'titulo')],                                                                                                                     
            [sg.Text('%utilização                                                                                                                                   100%')],
            [sg.Frame('', [[sg.Graph(GRAPH_SIZE, (0, 0), DATA_SIZE, key = 'graph')]])],
            [sg.Text('60 segudos                                                                                                                                       0')]
]          
layout =    [
            [sg.Column(coluna1, vertical_alignment = 't'), sg.Column(coluna2, vertical_alignment = 't')]
]

window = sg.Window('Monitoramento', layout)

step_size = 10
graph_cpu = False
graph_memoria = False
auto = 0

while True:
    event, values = window.read(timeout = DELAY, timeout_key= 1)

    if event == sg.WIN_CLOSED:
        break
    
    if type(event) == int:
        auto += event

    if event == 'CPU' or graph_cpu == True or auto == 1:
            
            if not graph_cpu:
                window['titulo'].update('CPU')
                window['graph'].Erase()
                x, y = GRAPH_SIZE[0], 0
                lastx, lasty = GRAPH_SIZE[0] - step_size, 0
                graph_cpu = True
                graph_memoria = False

            y = (Monitoramento.CPU()*270)/100
            window['graph'].Move(-step_size, 0)
            window['graph'].draw_line((lastx, lasty), (x, y), width=1)
            lasty = y

    if event == 'Memória' or graph_memoria == True:
        
        if not graph_memoria:
            window['titulo'].update(event)       
            window['graph'].Erase()
            x, y = GRAPH_SIZE[0], 0
            lastx, lasty = GRAPH_SIZE[0] - step_size, 0
            graph_memoria = True
            graph_cpu = False

        y = (Monitoramento.memoria()[2]*270)/100
        window['graph'].Move(-step_size, 0)
        window['graph'].draw_line((lastx, lasty), (x, y), width=1)
        lasty = y



window.close()