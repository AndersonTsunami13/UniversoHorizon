from himport import *

# simplificacao da animacao de escrevendo
def escrever_lento(texto, delay=0.03):
    for c in texto:
        print(c, end='', flush=True)
        time.sleep(delay)
    print()
    
# simplificacao de salva informacoes em logs
def escrever_log(texto, log):
    agora = datetime.now().strftime("%d/%m/%Y %H:%M:%S") # para salvar informacao junto com data e hora
    with open(log, "a") as arquivo:
        arquivo.write(f"[{agora}] {texto}\n")
        
# barra de carregamento simples
def barra_progresso_simples(tamanho=50, delay=0.05, cor=Fore.GREEN):
    for i in range(1, tamanho + 1):
        barra = "[" + "-" * i + "]"
        porcentagem = int((i / tamanho) * 100)
        print(cor + f"\r{porcentagem}% {barra}", end='', flush=True)
        time.sleep(delay)
    print()
  
# barra de carregamento simples
def barra_de_carregamento():
    print(Fore.GREEN + "\nAguarde!")
    barra_progresso_simples(75, 0.03, Fore.GREEN)