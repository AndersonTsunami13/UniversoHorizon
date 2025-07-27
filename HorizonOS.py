from himport import *
#importações aqui encima!

# Variáveis globais
inicio_sistema = None # ?
 
# uma dessas mensagens serao exibidas no boot
mensagens_boot = [
    "Carregando inteligência artificial...",
    "Inicializando segurança...",
    "Verificando integridade do sistema...",
    "Otimizando desempenho...",
    "Sistema acordando do sono profundo..."
]

# opcao para limpar log
# somente o log3.txt por enquanto!
def limpar_log():
        print(Fore.RED + "\n\nVoce tem certeza que que limpa o log do sistema?")
        print(Fore.RED + "\n1. Limpar e voltar\n2. Limpar e Reiniciar\n3. Limpar e Desligar\n4. sair\n")
        Llog = input(">")
        if Llog == "1":
            with open("log3.txt", "w") as arquivo:
                print(Fore.GREEN + "Log limpo com sucesso!")
            time.sleep(0.6)
            os.system("cls" if os.name == "nt" else "clear")
        elif Llog == "2":
            with open("log3.txt", "w") as arquivo:
                print(Fore.GREEN + "Log limpo com sucesso!")
            time.sleep(0.6)
            print(Fore.YELLOW + "Reiniciando...")
            time.sleep(0.5)
            iniciar_terminal()
        elif Llog == "3":
            with open("log3.txt", "w") as arquivo:
                print(Fore.GREEN + "Log limpo com sucesso!")
            time.sleep(0.6)
            print(Fore.YELLOW + "Desligando...")
            time.sleep(0.5)
            sys.exit()
        elif Llog == "4":
            print(Fore.YELLOW + "saindo...")
            time.sleep(0.4)
        else:
            print(Fore.RED + "Opcao invalida! Tente novamente.")
            limpar_log()
            
# marcar tempo de inicializacao
escrever_log("Sistema Iniciado.", "log3.txt")

# verificacao de senha
def validar_senha(senha_digitada):
    return senha_digitada == senha_correta

# tela de login
def login():
    escrever_lento(Fore.GREEN + "\n== LOGIN ==")
    escrever_log("Senha Solicitada!", "log3.txt")
    tentativas = 0
    while True:
        usuario = input("Usuario: ")
        escrever_log(f"{usuario} foi registrado.", "log3.txt")
        senha = input("Senha: ")
        escrever_log("Senha inserida.", "log3.txt")
        if validar_senha(senha):
            escrever_lento(Fore.YELLOW + f"Acesso concedido! Bem-vindo, {usuario}.")
            escrever_log(f"Senha Inserida esta Correta! Bem-vindo {usuario}", "log3.txt")
            return usuario
        else: 
            tentativas += 1
            escrever_log("Senha inserida esta Incorreta! Tente novamente.", "log3.txt")
            escrever_lento(Fore.RED + f"Senha incorreta! Tentativas: {tentativas}")
            escrever_log(f"Tentativa {tentativas}", "log3.txt")
            if tentativas == 5:
                print(Fore.RED + "\nSuas tentativas acabaram!")
                escrever_log("Senha foi inserida 5 vezes erradas", "log3.txt")
                print(Fore.RED + "Seu sistema vai ser reiniciado!")
                escrever_log("Reiniciando sistema...", "log3.txt")
                time.sleep(2)
                escrever_log("Acao desconhecida acabou de ser feita!!!!!", "log3.txt")
                return
                
# funcao de hora para o comando tempo
def formatar_tempo(segundos):
    horas = segundos // 3600
    minutos = (segundos % 3600) // 60
    segundos_rest = segundos % 60
    return f"{horas:02d}:{minutos:02d}:{segundos_rest:02d}"

# opcao para mudar a senha
def alterar_senha():
    global senha_correta
    antiga = input("Digite a senha atual: ")
    if validar_senha(antiga):
        nova = input("Digite a nova senha: ")
        senha_correta = nova
        print(Fore.GREEN + "Senha alterada com sucesso!")
    else:
        print(Fore.RED + "Senha atual incorreta! Operação cancelada.")

boot_sequence()

def mostrar_ajuda():
    print(Fore.CYAN + Style.BRIGHT + "\nComandos disponíveis:")
    print(Fore.GREEN + "[Sistema]")
    print(Fore.WHITE + "- ajuda       → Mostra esta lista")
    print("- sobre       → Informações do sistema")
    print("- tempo       → Mostra hora atual + tempo ligado")
    print("- processos   → Simula processos em execução")
    print("- limpar      → Limpa a tela (fake)")
    print("- senha       → Alterar senha do sistema")
    print("- reiniciar   → Reinicia o sistema")
    print("- desligar    → Encerra o sistema")
    print("- terminalui  → Detalhes da interface atual")
    print("- creditos    → Mostra quem desenvolveu")
    print("- sugestao    → Envia sugestão fictícia")
    print("- config      → Menu de configurações")
    print("- historico")
    print("- limpar historico")
    print(Fore.YELLOW + "[Programas]")
    print("- meu_pc      → Simula acesso ao disco")
    print("- navegador   → Simula navegador fictício")
    print("- matrix      → Efeito hacker verde matrix\n")
    print(Fore.YELLOW + "/n===[DEV]===")
    print("| >enable devmode")
    print("| >status devmode")
    print("| >devmode")
    print("# Esta em desenvolvimento.")
        
# efeito matrix brabo
def efeito_matrix():
    chars = "01"
    try:
        for _ in range(40):
            linha = "".join(random.choice(chars) for _ in range(80))
            print(Fore.GREEN + linha)
            time.sleep(0.05)
    except KeyboardInterrupt:
        pass

# bloco para execultar as acoes dos comandos
def executar_comando(comando):
    if comando == "ajuda":
        mostrar_ajuda()
    elif comando == "meu_pc":
        print(Fore.GREEN + "[Discos disponíveis:]")
        print("- C:/ (Sistema)")
        print("- D:/ (Arquivos)")
        print("- E:/ (Backup)")
        print(Fore.RED + "(Sistema Beta!)")
    elif comando == "historico":
        print(Fore.YELLOW + "Histórico de comandos:")
        with open("log3.txt", "r") as arquivo:
            conteudo = arquivo.read()
            print(Fore.BLUE + "\nConteúdo de log3.txt:")
            print(conteudo)
    elif comando =="limpar historico":
        limpar_log()
    elif comando == "navegador":
        escrever_lento(Fore.YELLOW + "Abrindo GalaxyNet...")
        time.sleep(1)
        print(Fore.CYAN + "https://galaxy.net - Conectado com sucesso!")
    elif comando == "limpar":
        os.system("cls" if os.name == "nt" else "clear")
    elif comando == "tempo":
        hora = time.strftime("%H:%M:%S")
        data = time.strftime("%d/%m/%Y")
        uptime_segundos = int(time.time() - inicio_sistema)
        print(Fore.CYAN + f"Hora atual: {hora}")
        print(Fore.CYAN + f"Data atual: {data}")
        print(Fore.CYAN + f"Iniciado às: {time.strftime('%H:%M:%S', time.localtime(inicio_sistema))}")
        print(Fore.CYAN + f"Tempo ligado: {formatar_tempo(uptime_segundos)}")
    elif comando == "processos":
        print(Fore.GREEN + "processos em execução...")
        time.sleep(1)
        print("- kernel.sys  | em execução")
        print("- terminal.py | aguardando entrada")
        print("- 007.exe     | finalizado")
    elif comando == "senha":
        alterar_senha()
    elif comando == "sobre":
        print(Fore.MAGENTA + "== HorizonOS System X ==")
        print(f"- Versão: {versao}")
        print("- Edição: System X")
        print(f"- Interface: {versaoUI}")
        print(f"- Desenvolvido por: {DEV}")
        print(Fore.CYAN + "feito usando o ChatGPT")
    elif comando == "terminalui":
        print(Fore.GREEN + f"Interface atual: {versaoUI}")
    elif comando == "creditos":
        print(Fore.YELLOW + f"Desenvolvido por {DEV} usando Python e Colorama")
    elif comando == "sugestao":
        sugestao = input("Digite sua sugestão: ")
        print(Fore.GREEN + "Obrigado pela sugestão! (ela será ignorada na versão beta 😅)")
    elif comando == "config":
        print(Fore.CYAN + "Menu de configurações ainda em desenvolvimento...")
    elif comando == "matrix":
        print(Fore.GREEN + "Entrando no modo Matrix... (Ctrl+C para sair)")
        efeito_matrix()
    elif comando == "status devmode":
        escrever_log(f"{usuario} tentou usarno devmode!", "log3.txt")
        print(Fore.RED + "Voce nao tem permissao para usar esse modo!")
    elif comando == "enable devmode":
        escrever_log(f"{usuario} tentou usarno devmode!", "log3.txt")
        print(Fore.RED + "Voce nao tem permissao para usar esse modo!")
    elif comando == "devmode":
        escrever_log(f"{usuario} tentou usarno devmode!", "log3.txt")
        print(Fore.RED + "Voce nao tem permissao para usar esse modo!")
    elif comando == "reiniciar":
        print(Fore.YELLOW + "Reiniciando sistema...")
        time.sleep(1.5)
        iniciar_terminal()
    elif comando in ["desligar", "sair"]:
        print(Fore.GREEN + "Desligando... até a próxima!")
        escrever_log("Sistema Desligado.", "log3.txt")
        sys.exit()
    else:
        print(Fore.RED + f"Comando desconhecido: '{comando}' (digite 'ajuda')")

# aonde a magia acontece
def iniciar_terminal():
    os.system("cls" if os.name == "nt" else "clear")
    boot_sequence()
    print(Fore.GREEN + "\nO Modo Dev ja esta disponivel!")
    print(Fore.GREEN + "\nDigite: (devmode) para entrar.\n")
    usuario = login()
    while True:
        try:
            comando = input(Fore.CYAN + f"{usuario}@systemX> ").strip().lower()
            if comando:           
                escrever_log(f"comando: {comando} Inserido.", "log3.txt")
                executar_comando(comando)
        except KeyboardInterrupt:
            print(Fore.RED + "\nSistema interrompido pelo usuário.")
            break

# Corrigindo o nome do módulo principal
if __name__ == "__main__":
    iniciar_terminal()