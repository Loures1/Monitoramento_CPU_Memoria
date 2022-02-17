import PySimpleGUI as sg
import Monitoramento

GRAPH_SIZE_CPU_AND_MEMORIA = (120, 54)
GRAPH_SIZE_MAIN = (GRAPH_SIZE_CPU_AND_MEMORIA[0]*5, GRAPH_SIZE_CPU_AND_MEMORIA[1]*5)
DATA_SIZE_CPU_AND_MEMORIA = (120, 54)
DATA_SIZE_MAIN = (DATA_SIZE_CPU_AND_MEMORIA[0]*5, DATA_SIZE_CPU_AND_MEMORIA[1]*5)
STEP_SIZE_CPU_MEMORIA = 2
STEP_SIZE_MAIN = STEP_SIZE_CPU_MEMORIA*5
DELAY = 1000
    

cpu_graph = [sg.Graph(GRAPH_SIZE_CPU_AND_MEMORIA, (0, 0), DATA_SIZE_CPU_AND_MEMORIA, background_color = 'white', key = 'cpu_graph')]
botao_cpu = [sg.Button('CPU')]
memoria_graph = [sg.Graph(GRAPH_SIZE_CPU_AND_MEMORIA, (0, 0), DATA_SIZE_CPU_AND_MEMORIA, background_color = 'white', key = 'memoria_graph')]
botao_memoria = [sg.Button('Memória')]

coluna1 =  [
            [sg.Column([cpu_graph], element_justification='c'), sg.Column([botao_cpu], element_justification='c')],
            [sg.Column([memoria_graph], element_justification='c'), sg.Column([botao_memoria], element_justification='c')]                
]

coluna2 =   [       
            [sg.Text('', key = 'titulo')],                                                                                                                     
            [sg.Text('%utilização                                                                                                                                   100%')],
            [sg.Frame('', [[sg.Graph(GRAPH_SIZE_MAIN, (0, 0), DATA_SIZE_MAIN, key = 'graph')]])],
            [sg.Text('60 segudos                                                                                                                                       0')]
]          
layout =    [
            [sg.Column(coluna1, vertical_alignment = 't'), sg.Column(coluna2, vertical_alignment = 't')]
]

window = sg.Window('Monitoramento', layout)

auto = False
lasty = [0]


while True:
    event, values = window.read(timeout = DELAY, timeout_key= 1)

    if event == sg.WIN_CLOSED:
        break

    x, y = GRAPH_SIZE_CPU_AND_MEMORIA[0], (Monitoramento.CPU()*GRAPH_SIZE_CPU_AND_MEMORIA[1])/100
    lastx = GRAPH_SIZE_CPU_AND_MEMORIA[0] - STEP_SIZE_CPU_MEMORIA
    window['cpu_graph'].Move(-STEP_SIZE_CPU_MEMORIA, 0)
    window['cpu_graph'].draw_line((lastx, lasty[-1]), (x, y), width=1)
    lasty.append(y)

    if event == 'CPU' or auto == True :

        if auto == True:
            x, y = GRAPH_SIZE_MAIN[0], y*5
            lastx = GRAPH_SIZE_MAIN[0] - STEP_SIZE_MAIN
            window['graph'].Move(-STEP_SIZE_MAIN, 0)
            window['graph'].draw_line((lastx, lasty[-2]*5), (x, y), width=1)
        
        
        if not auto:
            i = 0
            for y in lasty[1::]:
                x, y = GRAPH_SIZE_MAIN[0], y*5
                lastx = GRAPH_SIZE_MAIN[0] - STEP_SIZE_MAIN
                window['graph'].Move(-STEP_SIZE_MAIN, 0)
                window['graph'].draw_line((lastx, lasty[i]*5), (x, y), width=1)
                i += 1
            
            auto = True

        


window.close()