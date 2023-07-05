from elevador import Elevador

def main():
    pisosTotal = 10
    elevador = Elevador(pisosTotal)


    while True:
        print("=== ELEVADOR MALUCO ===")
        print("1. Chamar elevador")
        print("2. Adicionar pessoa")
        print("3. Remover pessoa")
        print("0. Sair")

        escolha = input("Insira o que deseja fazer: ")

        if escolha == "1":
            pisos_input = input("Insira os pisos (separado por vírgulas) para chamar o elevador: ")
            pisos = [int(piso.strip()) for piso in pisos_input.split(",")]
            for piso in pisos:
                elevador.ordemChamada.append(piso)
                elevador.chamarElevador(piso)
                elevador.parado(piso, pisos)

        elif escolha == "2":
            elevador.adicionarPessoa()
        elif escolha == "3":
            elevador.removerPessoa()
        elif escolha == "0":
            print("Saindo...")
            break
        else:
            print("Escolha inválida, insira outro número.")

        print()

if __name__ == "__main__":
    main()