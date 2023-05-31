from classes.FinancesManager import *

def main():
    finance_manager = FinancesManager()

    while True:
        try:
            print("----- Gerenciador de Finanças Pessoais -----")
            print("1. Exibir receitas planejadas")
            print("2. Adicionar receita planejada")
            print("3. Remover receita planejada")
            print("4. Exibir despesas planejadas")
            print("5. Adicionar despesa planejada")
            print("6. Remover despesa planejada")
            print("7. Exibir dinheiro economizado")
            print("8. Adicionar dinheiro guardado")
            print("9. Remover dinheiro guardado")
            print("10. Exibir histórico de transações")
            print("11. Adicionar transação ao histórico")
            print("12. Exibir dívidas e devedores")
            print("13. Adicionar devedor ou dívida")
            print("14. Remover devedor ou dívida")
            print("15. Atualizar valor pelo nome")
            print("16. Transferir valor de um arquivo")
            print("17. Sair")
            print("--------------------------------------------")

            choice = input("Digite o número da opção desejada: ")

            if choice == "1":
                print("Receitas Planejadas:")
                finance_manager.showPlannedRevenues()
                print()
            elif choice == "2":
                description = input("Digite a descrição da receita planejada: ")
                amount = float(input("Digite o valor da receita planejada: "))
                finance_manager.addPlannedRevenue(description, amount)
                print("Nova receita planejada adicionada!")
                print()
            elif choice == "3":
                description = input("Digite a descrição da receita planejada a ser removida: ")
                finance_manager.removePlannedRevenue(description)
                print("Receita planejada removida!")
                print()
            elif choice == "4":
                print("Despesas Planejadas:")
                finance_manager.showPlannedExpenses()
                print()
            elif choice == "5":
                description = input("Digite a descrição da despesa planejada: ")
                amount = float(input("Digite o valor da despesa planejada: "))
                ok = input("Aprovada? (Sim/Não): ")
                finance_manager.addPlannedExpense(description, amount, ok)
                print("Nova despesa planejada adicionada!")
                print()
            elif choice == "6":
                description = input("Digite a descrição da despesa planejada a ser removida: ")
                finance_manager.removePlannedExpense(description)
                print("Despesa planejada removida!")
                print()
            elif choice == "7":
                print("Dinheiro Economizado:")
                finance_manager.showSavedMoney()
                print()
            elif choice == "8":
                description = input("Digite a descrição do dinheiro guardado: ")
                amount = float(input("Digite o valor do dinheiro guardado: "))
                finance_manager.addSavedMoney(description, amount)
                print("Novo dinheiro guardado adicionado!")
                print()
            elif choice == "9":
                description = input("Digite a descrição do dinheiro guardado a ser removido: ")
                finance_manager.removeSavedMoney(description)
                print("Dinheiro guardado removido!")
                print()
            elif choice == "10":
                print("Histórico de Transações:")
                finance_manager.showHistoric()
                print()
            elif choice == "11":
                description = input("Digite a descrição da transação: ")
                amount = float(input("Digite o valor da transação: "))
                finance_manager.addHistoric(description, amount)
                print("Nova transação adicionada ao histórico!")
                print()
            elif choice == "12":
                print("Dívidas dos Devedores:")
                finance_manager.showDebtorsDebts()
                print()
            elif choice == "13":
                name = input("Digite o nome do devedor: ")
                debt = float(input("Digite o valor da dívida: "))
                finance_manager.addDebtorDebt(name, debt)
                print("Novo devedor ou dívida adicionado!")
                print()
            elif choice == "14":
                name = input("Digite o nome do devedor a ser removido: ")
                finance_manager.removeDebtorDebt(name)
                print("Devedor e dívida removidos!")
                print()
            elif choice == "15":
                description = input("Digite a descrição do valor a ser atualizado: ")
                new_amount = float(input("Digite o novo valor: "))
                finance_manager.updateAll(description, new_amount)
                print("Valor(es) atualizados!")
                print()
            elif choice == "16":
                source_file_path = input("Digite o caminho do arquivo de origem: ")
                destination_file_path = input("Digite o caminho do arquivo de destino: ")
                amount = float(input("Digite o valor a ser transferido: "))
                finance_manager.transferAmount(source_file_path, destination_file_path, amount)
                print("Transferência realizada com sucesso!")
                print()
            elif choice == "17":
                finance_manager.updateSummationFile()
                finance_manager.close_files()
                break
            else:
                print("Opção inválida. Por favor, tente novamente.")
                print()
        except Exception as e:
            print("Ocorreu um erro:", str(e))
            print()

if __name__ == "__main__":
    main()