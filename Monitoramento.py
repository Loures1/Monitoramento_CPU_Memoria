import psutil

def CPU():
    uso_da_CPU = psutil.cpu_percent(interval=0)
    return uso_da_CPU

def memoria():
    uso_da_memoria = psutil.virtual_memory()
    return uso_da_memoria


