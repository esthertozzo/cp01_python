"""
Chatbot Temático - Matrix Terminal
Checkpoint 1 - Computational Thinking with Python
"""

from datetime import datetime
import time
from rich.console import Console

console = Console()


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
    console.print("[green]Inicializando sistema...[/green]")
    time.sleep(0.5)
    console.print("[green]Carregando dados...[/green]")
    time.sleep(0.5)
    console.print("[green]Conectando à Matrix...[/green]")
    time.sleep(0.8)

    console.print("\n[bold green]>>> ACESSO CONCEDIDO <<<[/bold green]\n")
    time.sleep(0.5)

    digitar("Você tomou a pílula vermelha...")
    time.sleep(0.5)
    digitar("Bem-vinda ao mundo real.")
    time.sleep(0.5)
    console.print()


# -------- FUNÇÕES -------- #

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
    item = input(">> Digite um item: ")

    if item == "":
        console.print("[yellow]Entrada vazia detectada.[/yellow]")
    else:
        lista_itens.append(item)
        console.print("[green]Item armazenado na memória.[/green]")


def listar_itens(lista_itens):
    console.print("\n[cyan]Acessando banco de dados...[/cyan]")
    time.sleep(0.5)

    if len(lista_itens) == 0:
        console.print("[yellow]Nenhum dado encontrado.[/yellow]")
    else:
        console.print("[green]Registros encontrados:[/green]")
        for i in range(len(lista_itens)):
            console.print(f"[green][{i+1}][/green] {lista_itens[i]}")


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

    import random
    frase = random.choice(frases)

    console.print("\n[bold cyan] TRANSMISSÃO DO ORÁCULO [/bold cyan]\n")
    digitar(f"{frase}", 0.04)



def submenu_lista(lista_itens, nome):
    while True:
        console.print(f"\n[cyan]Operador: {nome} | Banco de Dados[/cyan]")
        console.print("[1] Listar itens")
        console.print("[2] Contar itens")
        console.print("[3] Cadastrar item")
        console.print("[0] Voltar")

        opcao = input("Escolha: ")

        if opcao == "1":
            listar_itens(lista_itens)
        elif opcao == "2":
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

while True:
    console.print(f"\n[bold green]>> Bem-vindo (a), {nome}[/bold green]")
    console.print("[1] Ver data")
    console.print("[2] Ver hora")
    console.print("[3] Gerenciar dados")
    console.print("[4] Mensagem do Oráculo")
    console.print("[0] Sair da Matrix")

    opcao = console.input("Escolha: ")

    if opcao == "1":
        mostrar_data()

    elif opcao == "2":
        mostrar_hora()

    elif opcao == "3":
        submenu_lista(lista_itens, nome)

    elif opcao == "4":
        mensagem_matrix()

    elif opcao == "0":
        console.print("\n[bold green]Desconectando...[/bold green]")
        digitar("Até a próxima, operador.", 0.04)
        break

    else:
        console.print("[bold red]Opção inválida![/bold red]")

    console.input("\n[cyan]Pressione ENTER para continuar...[/cyan]")