
import PySimpleGUI as sg
import Monitoramento
import Gerando_grafico

GRAPH_SIZE_CPU_AND_MEMORIA = (120, 54)
GRAPH_SIZE_MAIN = (GRAPH_SIZE_CPU_AND_MEMORIA[0]*5, GRAPH_SIZE_CPU_AND_MEMORIA[1]*5)
DATA_SIZE_CPU_AND_MEMORIA = (120, 54)
DATA_SIZE_MAIN = (DATA_SIZE_CPU_AND_MEMORIA[0]*5, DATA_SIZE_CPU_AND_MEMORIA[1]*5)
STEP_SIZE_CPU_MEMORIA = 2
STEP_SIZE_MAIN = STEP_SIZE_CPU_MEMORIA*5
DELAY = 1000
    
cpu = Gerando_grafico.Grafico('cpu_graph', GRAPH_SIZE_CPU_AND_MEMORIA, (0,0), DATA_SIZE_CPU_AND_MEMORIA,STEP_SIZE_CPU_MEMORIA, 'white')
memoria = Gerando_grafico.Grafico('memoria_graph', GRAPH_SIZE_CPU_AND_MEMORIA, (0,0), DATA_SIZE_CPU_AND_MEMORIA, STEP_SIZE_CPU_MEMORIA, 'white')
principal = Gerando_grafico.Grafico('principal_graph', GRAPH_SIZE_MAIN, (0,0), DATA_SIZE_MAIN, STEP_SIZE_MAIN, None)
botao_cpu = [
            [sg.Button('CPU')],
            [sg.Text('', key = 'percent_cpu')]
]
botao_memoria = [
                [sg.Button('Memória')],
                [sg.Text('',size = (15,1), key = 'percent_memoria')]
]

coluna1 =  [
            [sg.Column([[cpu.graph]], element_justification='c'), sg.Column(botao_cpu, element_justification='l')],
            [sg.Column([[memoria.graph]], element_justification='c'), sg.Column(botao_memoria, element_justification='l')]                
]

coluna2 =   [       
            [sg.Text('', key = 'titulo')],                                                                                                                     
            [sg.Text('%utilização                                                                                                                                   100%')],
            [sg.Frame('', [[principal.graph]])],
            [sg.Text('60 segudos                                                                                                                                       0')]
]          
layout =    [
            [sg.Column(coluna1, vertical_alignment = 't'), sg.Column(coluna2, vertical_alignment = 't')]
]

window = sg.Window('Monitoramento', layout)

auto = 0
auto_cpu = False
auto_memoria = False
principal.lasty = []

while True:
    event, values = window.read(timeout = DELAY, timeout_key= 1)

    if event == sg.WIN_CLOSED:
        break
    

    if event == 1:
        auto += 1

    y = Monitoramento.CPU()
    window['percent_cpu'].update(str(y) + ' %')
    cpu.escrevendo_Grafico(y)
    window['cpu_graph'].move(-cpu.step_size, 0 )
    window['cpu_graph'].draw_line((cpu.lastx, cpu.lasty[-1]), (cpu.x, cpu.y), width = 1)
    cpu.lasty.append(cpu.y)

    memoria_total_GB = float(round(Monitoramento.memoria()[0] * 9.31 * 10**-10))
    memoria_usada_GB = float(round(Monitoramento.memoria()[3] * 9.31 * 10**-10, 2))
    memoria_percent = Monitoramento.memoria()[2]
    window['percent_memoria'].update(f'{memoria_total_GB}/ {memoria_usada_GB} GB ({memoria_percent}%)')
    memoria.escrevendo_Grafico(memoria_percent)
    window['memoria_graph'].move(-memoria.step_size, 0)
    window['memoria_graph'].draw_line((memoria.lastx, memoria.lasty[-1]), (memoria.x, memoria.y), width = 1)
    memoria.lasty.append(memoria.y)

    if event == 'CPU' or auto_cpu == True or auto == 1:
        
        window['titulo'].update('CPU')

        if auto_cpu == True:
            principal.y = cpu.lasty[-1]
            window['principal_graph'].move(-principal.step_size, 0)
            window['principal_graph'].draw_line((principal.lastx, principal.lasty[-2]*5), (principal.x, principal.y*5))       
            principal.lasty = cpu.lasty

        if  not auto_cpu:
            window['principal_graph'].erase() 
            principal.lasty = cpu.lasty
            i = 0
            for principal.y in principal.lasty[1::]:
                window['principal_graph'].move(-principal.step_size, 0)
                window['principal_graph'].draw_line((principal.lastx, principal.lasty[i]*5), (principal.x, principal.y*5))
                i += 1
            auto_memoria = False
            auto_cpu = True
        
    if event == 'Memória' or auto_memoria == True:
        
        window['titulo'].update('Memória')

        if auto_memoria == True:
            principal.y = memoria.lasty[-1]
            window['principal_graph'].move(-principal.step_size, 0)
            window['principal_graph'].draw_line((principal.lastx, principal.lasty[-1]*5), (principal.x, principal.y*5))       
            principal.lasty = memoria.lasty

        if not auto_memoria:
            window['principal_graph'].erase()
            principal.lasty = memoria.lasty
            i = 0 
            for principal.y in principal.lasty[1::]:
                window['principal_graph'].move(-principal.step_size, 0)
                window['principal_graph'].draw_line((principal.lastx, principal.lasty[i]*5), (principal.x, principal.y*5))
                i += 1
            auto_memoria = True
            auto_cpu = False

window.close()