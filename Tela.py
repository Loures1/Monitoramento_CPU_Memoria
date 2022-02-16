import PySimpleGUI as sg
import Monitoramento

GRAPH_SIZE = (120, 54)
DATA_SIZE = (120, 54)
STEP_SIZE = 2
DELAY = 1000


graph_cpu = [sg.Graph(GRAPH_SIZE, (0, 0), DATA_SIZE, background_color = 'white', key = 'cpu_graph')]
botao_cpu = [sg.Button('CPU')]
graph_memoria = [sg.Graph(GRAPH_SIZE, (0, 0), DATA_SIZE, background_color = 'white', key = 'memoria_graph')]
botao_memoria = [sg.Button('Memória')]

coluna1 =  [
            [sg.Column([graph_cpu], element_justification='c'), sg.Column([botao_cpu], element_justification='c')],
            [sg.Column([graph_memoria], element_justification='c'), sg.Column([botao_memoria], element_justification='c')]                
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
                x, y = GRAPH_SIZE[0]*5, 0
                lastx, lasty = GRAPH_SIZE[0]*5 - step_size, 0
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
            x, y = GRAPH_SIZE[0]*5, 0
            lastx, lasty = GRAPH_SIZE[0]*5 - step_size, 0
            graph_memoria = True
            graph_cpu = False

        y = (Monitoramento.memoria()[2]*270)/100
        window['graph'].Move(-step_size, 0)
        window['graph'].draw_line((lastx, lasty), (x, y), width=1)
        lasty = y



window.close()