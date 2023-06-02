from datetime import date
import os
from classes.fileMethods import *

def get_current_date():
    current_date = date.today()
    return current_date

class FinancesManagerException(Exception):
    def __init__(self,msg):
        super(FinancesManagerException, self).__init__(msg)

class FinancesManager:
    def __init__(self) -> None:
        try:
            if not os.path.exists("data"): os.makedirs("data")
            
            if not os.path.exists("data/planned_revenues.csv"):
                with open("data/planned_revenues.csv", "w") as file:
                    file.write("")
            if not os.path.exists("data/planned_expenses.csv"):
                with open("data/planned_expenses.csv", "w") as file:
                    file.write("")
            if not os.path.exists("data/saved_money.csv"):
                with open("data/saved_money.csv", "w") as file:
                    file.write("")
            if not os.path.exists("data/historic.csv"):
                with open("data/historic.csv", "w") as file:
                    file.write("")
            if not os.path.exists("data/debtors-debts.csv"):
                with open("data/debtors-debts.csv", "w") as file:
                    file.write("")
            if not os.path.exists("data/summation.csv"):
                with open("data/summation.csv", "w") as file:
                    file.write("")

            self.__FILE_PLANNED_REVENUES = open("./data/planned_revenues.csv", "r")
            self.__FILE_PLANNED_EXPENSES = open("./data/planned_expenses.csv", "r")
            self.__FILE_HISTORIC = open("./data/historic.csv", "r")
            self.__FILE_SAVED_MONEY = open("./data/saved_money.csv", "r")
            self.__FILE_DEBTORS_DEBTS = open("./data/debtors-debts.csv", "r")
            self.__FILE_SUMMATION = open("./data/summation.csv", "r")
            self.__total_expenses = 727.00
            self.__total_revenues = 650.00
        except FileNotFoundError:
            raise FinancesManagerException("Error: arquivo não encontrado!")
    
    def addPlannedRevenue(self, description: str, amount: float) -> None:
        try:
            planned_revenue = f"{description};{str(amount)}"
            file_path = "./data/planned_revenues.csv"
            if has_line(file_path):
                planned_revenue = "\n" + planned_revenue
            with open(file_path, "a") as file:
                file.write(planned_revenue + "\n")
            self.addHistoric("Adição de categoria de dinheiro guardado: "+description, amount)
        except IOError:
            raise FinancesManagerException("Erro ao adicionar receita planejada. Verifique o arquivo ou permissões de leitura/escrita.")

    def addPlannedExpense(self, description: str, amount: float, ok: any) -> None:
        try:
            planned_expense = f"{description};{str(amount)};{str(ok)}"
            file_path = "./data/planned_expenses.csv"
            if has_line(file_path):
                planned_expense = "\n" + planned_expense
            with open(file_path, "a") as file:
                file.write(planned_expense + "\n")
            self.addHistoric("Adição de gasto: "+description, amount)
        except IOError:
            raise FinancesManagerException("Erro ao adicionar despesa planejada. Verifique o arquivo ou permissões de leitura/escrita.")
    
    def addSavedMoney(self, description: str, amount: float) -> None:
        try:
            money = f"{description};{str(amount)}"
            file_path = "./data/saved_money.csv"
            if has_line(file_path):
                money = "\n" + money
            with open(file_path, "a") as file:
                file.write(money + "\n")
            self.addHistoric("Dinheiro guardado adicionado: "+description, amount)
        except IOError:
            raise FinancesManagerException("Erro ao adicionar dinheiro guardado. Verifique o arquivo ou permissões de leitura/escrita.")
    
    def addDebtorDebt(self, name: str, amount: float) -> None:
        try:
            debt = f"{name};{str(amount)}"
            file_path = "./data/debtors_debts.csv"
            if has_line(file_path):
                debt = "\n" + debt
            with open(file_path, "a") as file:
                file.write(debt + "\n")
            self.addHistoric("Adição de devedor ou dívida: " + name, amount)
        except IOError:
            raise FinancesManagerException("Erro ao adicionar devedor ou dívida. Verifique o arquivo ou permissões de leitura/escrita.")


    def removeSavedMoney(self, description: str, amount: float) -> None:
        try:
            money = f"{description};{str(amount)}"
            file_path = "./data/saved_money.csv"
            with open(file_path, "r") as file:
                lines = file.readlines()
            with open(file_path, "w") as file:
                for line in lines:
                    if money not in line:
                        file.write(line)
            self.addHistoric("Remoção de categoria de dinheiro guardado: "+description, amount * -1)
        except IOError:
            raise FinancesManagerException("Erro ao remover dinheiro guardado. Verifique o arquivo ou permissões de leitura/escrita.")

    def removePlannedRevenue(self, description: str, amount: float) -> None:
        try:
            revenue = f"{description};{str(amount)}"
            file_path = "./data/planned_revenues.csv"
            with open(file_path, "r") as file:
                lines = file.readlines()
            with open(file_path, "w") as file:
                for line in lines:
                    if revenue not in line:
                        file.write(line)
            self.addHistoric("Remoção de receita planejada: " + description, amount * -1)
        except IOError:
            raise FinancesManagerException("Erro ao remover receita planejada. Verifique o arquivo ou permissões de leitura/escrita.")

    def removePlannedExpense(self, description: str, amount: float) -> None:
        try:
            expense = f"{description};{str(amount)}"
            file_path = "./data/planned_expenses.csv"
            with open(file_path, "r") as file:
                lines = file.readlines()
            with open(file_path, "w") as file:
                for line in lines:
                    if expense not in line:
                        file.write(line)
            self.addHistoric("Remoção de despesa planejada: " + description, amount * -1)
        except IOError:
            raise FinancesManagerException("Erro ao remover despesa planejada. Verifique o arquivo ou permissões de leitura/escrita.")

    def removeDebtorDebt(self, description: str, amount: float) -> None:
        try:
            debt = f"{description};{str(amount)}"
            file_path = "./data/debtors-debts.csv"
            with open(file_path, "r") as file:
                lines = file.readlines()
            with open(file_path, "w") as file:
                for line in lines:
                    if debt not in line:
                        file.write(line)
            self.addHistoric("Remoção de dívida: " + description, amount * -1)
        except IOError:
            raise FinancesManagerException("Erro ao remover dívida. Verifique o arquivo ou permissões de leitura/escrita.")

    def transferAmount(self, source_file_path: str, destination_file_path: str, amount: float) -> None:
        try:
            with open(source_file_path, "r") as source_file:
                lines = source_file.readlines()

            with open(source_file_path, "w") as source_file:
                with open(destination_file_path, "a") as destination_file:
                    for line in lines:
                        description, line_amount = line.strip().split(";")
                        line_amount = float(line_amount)
                        if line_amount >= amount:
                            new_amount = line_amount - amount
                            line = f"{description};{new_amount}\n"
                            source_file.write(line)
                            destination_file.write(f"{description};{amount}\n")
                            break
                        else:
                            source_file.write(line)
                            destination_file.write(line)
                            amount -= line_amount
            self.addHistoric(f"Tranferência de {source_file_path} para {destination_file_path}", amount)
        except IOError:
            raise FinancesManagerException("Erro ao transferir o valor. Verifique os arquivos ou permissões de leitura/escrita.")

    def addHistoric(self, description: str, amount: float):
        try:
            current_date = get_current_date()
            expense = f"{str(amount)};{description};{current_date}"
            with open("./data/historic.csv", "a") as file:
                file.write(expense + "\n")
        except IOError:
            raise FinancesManagerException("Erro ao adicionar histórico. Verifique o arquivo ou permissões de leitura/escrita.")

    def showPlannedExpenses(self):
        try:
            with open("./data/planned_expenses.csv", "r") as file:
                for linha in file:
                    print(linha.strip())
        except IOError:
            raise FinancesManagerException("Erro ao exibir despesas planejadas. Verifique o arquivo ou permissões de leitura.")

    def showHistoric(self):
        try:
            with open("./data/historic.csv", "r") as file:
                for linha in file:
                    print(linha.strip())
        except IOError:
            raise FinancesManagerException("Erro ao exibir histórico. Verifique o arquivo ou permissões de leitura.")

    def showSavedMoney(self):
        try:
            with open("./data/saved_money.csv", "r") as file:
                for linha in file:
                    print(linha.strip())
        except IOError:
            raise FinancesManagerException("Erro ao exibir dinheiro guardado. Verifique o arquivo ou permissões de leitura.")

    def showDebtorsDebts(self):
        try:
            with open("./data/debtors-debts.csv", "r") as file:
                for linha in file:
                    print(linha.strip())
        except IOError:
            raise FinancesManagerException("Erro ao exibir dívidas de devedores. Verifique o arquivo ou permissões de leitura.")

    def showPlannedRevenues(self):
        try:
            with open("./data/planned_revenues.csv", "r") as file:
                for linha in file:
                    print(linha.strip())
        except IOError:
            raise FinancesManagerException("Erro ao exibir receitas planejadas. Verifique o arquivo ou permissões de leitura.")

    def update(self, file_path: str, description: str, new_amount: float) -> None:
        try:
            lines = []
            with open(file_path, "r") as file:
                lines = file.readlines()

            updated_lines = []
            for line in lines:
                line_data = line.strip().split(";")
                line_description = line_data[0]
                line_amount = float(line_data[1])

                if line_description == description:
                    if file_path == "./data/planned_expenses.csv" or file_path == "./data/debtors-debts.csv":
                        if line_amount > 0 and new_amount == 0:
                            updated_line = f"{line_description};{new_amount};check\n"
                    else:
                        updated_line = f"{line_description};{new_amount}\n"
                else:
                    updated_line = line
                updated_lines.append(updated_line)

            with open(file_path, "w") as file:
                file.writelines(updated_lines)
        except IOError:
            raise FinancesManagerException("Erro ao atualizar o arquivo. Verifique o arquivo ou permissões de leitura/escrita.")

    def updateAll(self, description: str, new_amount: float) -> None:
        try:
            self.update("./data/planned_revenues.csv", description, new_amount)
            self.update("./data/planned_expenses.csv", description, new_amount)
            self.update("./data/saved_money.csv", description, new_amount)
            self.update("./data/debtors-debts.csv", description, new_amount)
        except IOError:
            raise FinancesManagerException("Erro ao atualizar os arquivos. Verifique os arquivos ou permissões de leitura/escrita.")

    def updateSummationFile(self):
        accountsImportants = ["Reserva de Emergencia", "Nubank"]
        reserve = ["Reserva de Emergencia"]
        total_saved_money_not_expense = sum_values_in_file("./data/saved_money.csv", accountsImportants)
        total_saved_money_for_reserve = sum_values_in_file("./data/saved_money.csv", reserve)
        total_saved_money = sum_values_in_file("./data/saved_money.csv")
        total_debtors_debts = sum_values_in_file("./data/debtors-debts.csv")
        total_planned_expenses = sum_values_in_file("./data/planned_expenses.csv")
        total_planned_revenues = sum_values_in_file("./data/planned_revenues.csv")

        summation_content = f"Total: {total_saved_money:.2f}\nTotal em receitas: {self.__total_revenues:.2f}\nDevedores: {total_debtors_debts:.2f}\nPara gastar: {total_saved_money - total_saved_money_not_expense:.2f}\nTotal em maos - reserva: {total_saved_money - total_saved_money_for_reserve:.2f}\nTotal em despesas: {self.__total_expenses:.2f}\nQuanto falta em despesas: {total_planned_expenses:.2f}"

        with open("./data/summation.csv", "w") as file:
            file.write(summation_content)
    
    def close_files(self):
        self.__FILE_PLANNED_REVENUES.close()
        self.__FILE_PLANNED_EXPENSES.close()
        self.__FILE_HISTORIC.close()
        self.__FILE_SAVED_MONEY.close()
        self.__FILE_DEBTORS_DEBTS.close()
        self.__FILE_SUMMATION.close()