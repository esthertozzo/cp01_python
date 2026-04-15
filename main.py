"""
Chatbot Temático - Matrix Terminal
Checkpoint 1 - Computational Thinking with Python
"""
from datetime import datetime
import time
from rich.console import Console
from rich.panel import Panel
from rich.align import Align
from rich.rule import Rule
import random

console = Console(force_terminal=True, color_system="truecolor")


# Lista para guardar os itens
lista_itens = []


# -------- EFEITO DE DIGITAÇÃO -------- #
def digitar(texto, delay=0.03):
    for letra in texto:
        console.print(letra, style="green", end="")
        time.sleep(delay)
    console.print()  # quebra linha


# -------- TELA INICIAL MATRIX -------- #
def iniciar_matrix():
    console.print(Rule("[bold green]MATRIX SYSTEM BOOT[/bold green]"))
    chuva_matrix()

    console.print("\n")

    glitch("ACESSO CONCEDIDO")
    time.sleep(0.5)

    digitar("Você tomou a pílula vermelha...", 0.02)
    digitar("Bem-vinda ao mundo real.", 0.02)

    console.print(Rule("[green] SISTEMA PRONTO [/green]"))


# -------- FUNÇÕES -------- #

def processando(msg="Processando"):
    for i in range(3):
        console.print(f"[green]{msg}{'.' * (i+1)}[/green]", end="\r")
        time.sleep(0.4)
    console.print(" " * 50, end="\r")

def glitch(texto):
    for _ in range(3):
        console.print(f"[bright_black]{texto}[/bright_black]", end="\r")
        time.sleep(0.05)
        console.print(f"[green]{texto}[/green]", end="\r")
        time.sleep(0.05)
    console.print(f"[bold bright_green]{texto}[/bold bright_green]")

def chuva_matrix(linhas=12):
    chars = "01アイウエオカキクケコ"
    for _ in range(linhas):
        linha = "".join(random.choice(chars) for _ in range(80))
        console.print(f"[green]{linha}[/green]")
        time.sleep(0.03)

def mostrar_data():
    agora = datetime.now()
    data_formatada = agora.strftime('%d/%m/%Y')
    console.print(f"[green]> DATA DO SISTEMA:[/green] {data_formatada}")


def mostrar_hora():
    agora = datetime.now()
    hora_formatada = agora.strftime('%H:%M:%S')
    console.print(f"[green]> HORA DO SISTEMA:[/green] {hora_formatada}")


def mostrar_data_hora():
    agora = datetime.now()
    dt_formatado = agora.strftime("%d/%m/%Y às %H:%M:%S")
    console.print(f"[green]> TIMESTAMP:[/green] {dt_formatado}")


def cadastrar_item(lista_itens):
    console.print("\n[cyan]Modo de inserção ativado...[/cyan]")
    item = console.input(">> Digite um item: ")

    if item == "":
        console.print("[yellow]Entrada vazia detectada.[/yellow]")
    else:
        lista_itens.append(item)
        console.print(f"[green]Item '{item}' armazenado na memória.[/green]")


def listar_itens(lista_itens):
    processando("Acessando banco de dados")
    time.sleep(0.5)

    if len(lista_itens) == 0:
        console.print("[yellow]Nenhum dado encontrado.[/yellow]")
    else:
        console.print("[green]Registros encontrados:[/green]")
        for i, item in enumerate(lista_itens, start=1):
            console.print(f"[green][{i}][/green] {item}")


def contar_itens(lista_itens):
    quantidade = len(lista_itens)
    console.print(f"[green]> TOTAL DE REGISTROS:[/green] {quantidade}")


def mensagem_matrix():
    frases = [
        "Não existe colher.",
        "O problema é a escolha.",
        "Liberte sua mente.",
        "A Matrix é um sistema de controle.",
        "Você já teve a sensação de que não está no controle?",
    ]

    frase = random.choice(frases)
    chuva_matrix(6)
    console.print("\n[bold cyan] TRANSMISSÃO DO ORÁCULO [/bold cyan]\n")
    digitar(f"{frase}", 0.04)



def submenu_lista(lista_itens, nome):
    while True:
        console.print(Panel.fit(
            f"""
            [green]Operador:[/green] {nome}
            [green]Módulo:[/green] Banco de Dados
                        
            [1] Listar itens
            [2] Contar itens
            [3] Cadastrar item
            [0] Voltar
        """,
            border_style="green"
        ))

        opcao = console.input("[bold green]neo@matrix~# Escolha: [/bold green]")

        if opcao == "1":
            processando()
            listar_itens(lista_itens)
        elif opcao == "2":
            processando()
            contar_itens(lista_itens)
        elif opcao == "3":
            cadastrar_item(lista_itens)
        elif opcao == "0":
            console.print("[green]Retornando ao sistema principal...[/green]")
            break
        else:
            console.print("[red]Código inválido.[/red]")


# -------- INÍCIO DO PROGRAMA -------- #

iniciar_matrix()

nome = console.input("[cyan]Identifique-se, operador: [/cyan]")

console.print(f"\n[green]Validando identidade de {nome}...[/green]")
processando()

console.print(f"[bold green]Acesso autoridado, {nome}.[/bold green]")

def menu_principal(nome):
    console.print(Panel.fit(
        f"""
    [bold green]>> Bem-vindo(a), {nome}[/bold green]
    
    [1] Ver data
    [2] Ver hora
    [3] Gerenciar dados
    [4] Mensagem do Oráculo
    [0] Sair da Matrix
    """,
        title="[bold green] TERMINAL MATRIX [/bold green]",
        border_style="green"
    ))

while True:
    menu_principal(nome)

    opcao = console.input("[bold green]neo@matrix~# Escolha: [/bold green]")

    if opcao == "1":
        mostrar_data()

    elif opcao == "2":
        mostrar_hora()

    elif opcao == "3":
        submenu_lista(lista_itens, nome)

    elif opcao == "4":
        mensagem_matrix()

    elif opcao == "0":

        console.print(Panel.fit("[bold green]ENCERRANDO CONEXÃO COM A MATRIX...[/bold green]", border_style="green"))
        chuva_matrix(6)
        digitar("Você nunca steve realmente desconectado...", 0.04)
        break

    else:
        console.print("[bold red]Opção inválida![/bold red]")

    console.input("\n[cyan]Pressione ENTER para continuar...[/cyan]")