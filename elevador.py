import time
import sys
class Elevador: 
    def __init__(elevador, pisosTotal):
        elevador.pisoAtual = 0
        elevador.capacidadeMaxima = 10
        elevador.capacidadeAtual = 0
        elevador.direcao = "parado"
        elevador.ordemChamada = []
        elevador.totalPisos = 10
        elevador.porta = "fechada"

    def adicionarPessoa(elevador):
        if elevador.capacidadeAtual < elevador.capacidadeMaxima:
            pessoasEntrando = int(input('Digite quantas pessoas vão entrar no elevador: '))
            if elevador.capacidadeAtual + pessoasEntrando > elevador.capacidadeMaxima:
                print(f"Não é possível adicionar esse número de pessoas no elevador. Ele está lotado.")
            else:
                elevador.capacidadeAtual += pessoasEntrando
                print(f"Há agora {elevador.capacidadeAtual} pessoas no elevador")
        else:
            print("O elevador está cheio no momento.")

    
    def removerPessoa(elevador):
        if elevador.capacidadeAtual > 0:
            pessoasSaindo = int(input('Digite a quantas pessoas vão sair do elevador: '))
            if elevador.capacidadeAtual - pessoasSaindo < 0:
                print(f"Não é possível remover esse número de pessoas no elevador. Este sistema não aceita valores negativos.")
            else:
                elevador.capacidadeAtual = elevador.capacidadeAtual - pessoasSaindo
                print(f"Há agora {elevador.capacidadeAtual} pessoas no elevador")
        else:
            print("O elevador está vazio. Não há pessoas para sair.")
    
    def mover(elevador, piso):
        if elevador.porta == "fechada":
            elevador.abrirPorta()
            elevador.fecharPorta()
            if piso < elevador.pisoAtual:
                elevador.direcao = "descendo"
                print(f"O elevador está descendo para o andar {piso}.")
            elif piso > elevador.pisoAtual:
                elevador.direcao = "subindo"
                print(f"O elevador está subindo para o andar {piso}.")
            else:
                print("O elevador já está no andar solicitado.")
        else:
            print("A porta do elevador está aberta. Feche a porta antes de se mover.")
        
        chegando = "O elevador está chegando\n"
        for l in chegando:
            sys.stdout.write(l)
            sys.stdout.flush()
            time.sleep(0.3)
        
        elevador.ordenarOrdem()
        elevador.pisoAtual = piso
        elevador.fecharPorta()
        print(f"O elevador está no {elevador.pisoAtual} andar")

    def chamarElevador(elevador, piso):
        if elevador.porta == "fechada":
                while elevador.ordemChamada:
                    if piso > elevador.pisoAtual and elevador.direcao == "descendo":
                        print("O elevador está descendo. Espere até chegar. ")
                    elif piso < elevador.pisoAtual and elevador.direcao == "subindo":
                        print("O elevador está subindo. Espere até pegar as pessoas de todos os andares superiores.")
                    else:
                        print("O piso chamado foi adicionado à fila.")
                    elevador.ordenarOrdem()
                    if not elevador.ordemChamada:
                        break
        else:
            print("A porta do elevador está aberta. Feche a porta antes de chamar o elevador.")
    

    def ordenarOrdem(elevador):
        if elevador.porta == "fechada":
            if elevador.ordemChamada:
                proximoPiso = elevador.ordemChamada.pop(0)
                elevador.mover(proximoPiso)
        else:
            print("A porta está aberta.")
    
    def abrirPorta(elevador):
        if elevador.porta == "fechada":
            elevador.porta = "aberta"
            print("A porta do elevador está aberta")
        else:
            print("A porta do elevador já está aberta")
    
    def fecharPorta(elevador):
        if elevador.porta =="aberta":
            elevador.porta = "fechada"
            print("A porta do elevador está fechada")
        else:
            print("A porta já está fechada")

    def parado(elevador, piso, pisos):
        escolha2 = int
        while True or escolha2 != 4 and 0:
            print("=== ELEVADOR MALUCO ===")
            print(f"O elevador chegou em um de seus destinos. O andar {elevador.pisoAtual}. Agora informe:")
            print("1. Adicionar pessoa ao elevador")
            print("2. Remover pessoa do elevador")
            print("3. Adicionar e remover pessoas do elevador")
            print("4. Seguir viagem")
            print("0. Sair (voltar a tela inicial)")
            print("======================")
            print()
            
            escolha2 = input("Insira o que irá fazer: ")
            if escolha2 == "1":
                elevador.adicionarPessoa()
                print("As pessoas que foram adicionadas ao elevador, gostariam de ir para quais andares? ")
                pisosAdicionado_input = input("Insira os pisos (separado por vírgulas) para chamar o elevador: ")
                pisosAdicionado = [int(pisoAdicionado.strip()) for pisoAdicionado in pisosAdicionado_input.split(",")]
                pisos.extend(pisosAdicionado)
            elif escolha2 == "2":
                elevador.removerPessoa()
            elif escolha2 == "3":
                elevador.adicionarPessoa()
                print("As pessoas que foram adicionadas ao elevador, gostariam de ir para quais andares? ")
                pisosAdicionado_input = input("Insira os pisos (separado por vírgulas) para chamar o elevador: ")
                pisosAdicionado = [int(pisoAdicionado.strip()) for pisoAdicionado in pisosAdicionado_input.split(",")]
                pisos.extend(pisosAdicionado)
                elevador.removerPessoa()
            elif escolha2 == "4":
                print("Seguindo viagem...")
                elevador.chamarElevador(piso)
                print()
                break
            elif escolha2 == "0":
                print("Saindo...")
                break
            else:
                print("Escolha inválida, insira outro número.")


