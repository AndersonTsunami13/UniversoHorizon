from himport import *
from funcoes import *

# Inicializa o colorama
init(autoreset=True)

enable_segure_bios = "false"

def bios_sequence():
    os.system("cls" if os.name == "nt" else "clear")
    escrever_log("Carregando bios...", "log3.txt")
    escrever_lento(Fore.GREEN + "| Horizon Megatrends")
    escrever_lento(Fore.GREEN + "| BIOS v2")
    escrever_lento(Fore.GREEN + "| Copyright (C) 2024-2025\n")
    print(Fore.YELLOW + "Deseja entra no Setup? S ou N")
    resposta = input("> ")
    if resposta == "s":
        print("Entrando no setup...")
        time.sleep(3)
        bios_system()
    elif resposta == "n":
        print(Fore.GREEN + "Certo! Aguarde...\n")
    else:
        print(Fore.RED + "Comando nao reconhecido! tente novamente.")
        time.sleep(1)
        return
    escrever_lento(Fore.GREEN + "Initializing hardware...")
    escrever_log("Iniciando hardware...", "log3.txt")
    time.sleep(0.4)
    escrever_log("Hardware iniciado!", "log3.txt")
    escrever_lento(Fore.GREEN + "Detecting drives...")
    escrever_log("Detectando drivers...", "log3.txt")
    time.sleep(0.5)
    escrever_lento(Fore.GREEN + "C: Fixed Disk Drive")
    escrever_log("(C: Fixed Disk Drive) Detectado.", "log3.txt")
    time.sleep(0.3)
    escrever_lento(Fore.GREEN + "D: CD-ROM Drive")
    escrever_log("(D: CD-ROM Drive) Detectado.", "log3.txt")
    time.sleep(0.3)
    escrever_lento(Fore.GREEN + "Memory Test: 65536K OK")
    escrever_log("Memory> 65536K Ok", "log3.txt")
    escrever_lento(Fore.GREEN + "Loading Operating System...")
    escrever_log("Carregando Sistema Operacional...", "log3.txt")
    barra_progresso_simples(50, 0.2)
    time.sleep(0.4)
    
def bios_system():
    os.system("cls" if os.name == "nt" else "clear")
    escrever_lento(Fore.GREEN + "Carregando informações...")
    time.sleep(0.8)
    escrever_log("Carregando informações...", "log_bios1.txt")
    escrever_lento(Fore.BLUE + "Verificando informacoes de seguranca...")
    escrever_log("BIOS esta sendo acessada!", "log_bios1.txt")
    if enable_segure_bios == "false":
        escrever_lento(Fore.RED + "Voce nao tem permissao.")
        time.sleep(0.4)
    elif enable_segure_bios == "true":
        escrever_lento(Fore.GREEN + "Permissao ativada!")
        escrever_lento(Fore.GREEN + "Aguarde...")
        time.sleep(0.3)
        escrever_lento(Fore.RED + "\nNao foi possivel acessar.")
        time.sleep(0.4)
    else:
        escrever_lento(Fore.RED + "\nfuncao indisponivel!")