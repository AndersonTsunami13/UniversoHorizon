from himport import *
# importacoes gerais

from bios import bios_sequence

# simulacao de inicializacao de um sistema
def boot_sequence():
    global inicio_sistema
    inicio_sistema = time.time()
    bios_sequence()
    os.system("cls" if os.name == "nt" else "clear")
    escrever_lento(Fore.RED + "Starting HorizonOS SystemX 1...")
    escrever_log("Iniciando HorizonOS SystemX 1...", "log3.txt")
    barra_progresso_simples(50)
    time.sleep(0.4)
    escrever_lento(Fore.GREEN + Style.BRIGHT + f"\nHorizonOS System X - {versao}") 
    time.sleep(0.4)
    barra_progresso_simples(25)
    escrever_lento(Fore.YELLOW + random.choice(mensagens_boot))
    barra_progresso_simples(25)
    escrever_lento(Fore.YELLOW + "[OK] Núcleo carregado")
    barra_progresso_simples(50)
    escrever_lento(Fore.YELLOW + "[OK] Interface Terminal pronta")
    barra_progresso_simples(50)
    barra_de_carregamento()
    escrever_lento(Fore.CYAN + "\nDigite 'ajuda' para listar os comandos disponíveis\n")
    print("-" * 50)