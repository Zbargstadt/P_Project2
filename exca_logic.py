from PyQt6.QtWidgets import *
from exca_input import *
from exca_list import *
from exca_sum import *
import csv
import os.path

class Logic_Input(QMainWindow, Ui_InputWindow):
    '''
    Class that applies the Login GUI
    Also houses functions login and create
    '''
    def __init__(self) -> None:
        '''
        Initializes Login Gui
        '''
        super().__init__()
        self.setupUi(self)
        self.button_login.clicked.connect(lambda: self.login())
        self.button_create.clicked.connect(lambda: self.create())

    def login(self) -> None:
        '''
        Allows user to login into saved account
        :return: Access Bank GUI
        '''
        Logic_Input.login_list = [self.input_username.text(), self.input_password.text()]
        if os.path.isfile(f'files\\names.csv'):
            with open('files\\names.csv', 'r', newline='') as csv_file:
                csv_reader = csv.reader(csv_file)
                for line in csv_reader:
                    if self.input_username.text() == line[0]:
                        if self.input_password.text() == line[1]:
                            self.application = QApplication([])
                            self.window = Logic_List()
                            self.window.show()
                            self.application.exec()
                        else:
                            self.label_error.setText('ERROR: Incorrect Password')
                            break
                    else:
                        self.label_error.setText('ERROR: User Doesnt Exist')
        else:
            self.label_error.setText('No Users Exist Yet')
    def create(self) -> None:
        '''
        Allows user to create new account
        :return: Access Bank GUI
        '''
        Logic_Input.login_list = [self.input_username.text(), self.input_password.text()]
        repeat = False
        if os.path.isfile(f'files\\names.csv'):
            #Create New Login
            with open('files\\names.csv', 'r', newline='') as csv_file:
                csv_reader = csv.reader(csv_file)
                for line in csv_reader:
                    if self.input_username.text() == line[0]:
                        self.label_error.setText('ERROR: User Already Exists')
                        repeat = True
                if repeat is False:
                    with open('files\\names.csv', 'a', newline='') as c_file:
                        csv_writer = csv.writer(c_file)
                        csv_writer.writerow(Logic_Input.login_list)
                    self.application = QApplication([])
                    self.window = Logic_List()
                    self.window.show()
                    self.application.exec()

        else:
            #Create CSV File
            with open('files\\names.csv', 'w', newline='') as csv_file:
                csv_writer = csv.writer(csv_file)
                header = ['Username', 'Password']
                csv_writer.writerow(header)
                csv_writer.writerow(Logic_Input.login_list)
            self.application = QApplication([])
            self.window = Logic_List()
            self.window.show()
            self.application.exec()

class Logic_List(QMainWindow, Ui_ListWindow):
    '''
    Class that applies the List GUI
    Also houses functions create2, add_expense, removw_expense, and save
    '''
    def __init__(self) -> None:
        '''
        Initializes List GUI
        '''

        #Initializes GUI
        super().__init__()
        self.setupUi(self)
        Logic_List.expense_list = []

        #Checks For Previous Data
        if os.path.isfile(f'files\\{Logic_Input.login_list[0]}.csv'):
            with open(f'files\\{Logic_Input.login_list[0]}.csv', 'r', newline='') as csv_file:
                csv_reader = csv.reader(csv_file)
                next(csv_reader)
                for line in csv_reader:
                    Logic_List.expense_list.append(line)
                row = 0
                self.table_expenses.setRowCount(len(Logic_List.expense_list))
                for exp in Logic_List.expense_list:
                    print(exp[0])
                    self.table_expenses.setItem(row, 0, QtWidgets.QTableWidgetItem(exp[0]))
                    self.table_expenses.setItem(row, 1, QtWidgets.QTableWidgetItem(f'{str(exp[1])}$'))
                    self.table_expenses.setItem(row, 2, QtWidgets.QTableWidgetItem(str(exp[2])))
                    self.table_expenses.setItem(row, 3, QtWidgets.QTableWidgetItem(f'{str(exp[3])}$'))
                    self.table_expenses.setItem(row, 4, QtWidgets.QTableWidgetItem(f'{str(exp[4])}$'))
                    row += 1

        #Buttons Clicks
        self.button_sum.clicked.connect(lambda: self.create2())
        self.button_ent.clicked.connect(lambda: self.add_expense())
        self.button_rem.clicked.connect(lambda: self.remove_expense())
        self.button_save.clicked.connect(lambda: self.save())

    def create2(self) -> None:
        '''
        :return: Access Summary GUI
        '''
        self.application = QApplication([])
        self.window = Logic_Sum()
        self.window.show()
        self.application.exec()

    def add_expense(self) -> None:
        '''
        Adds a new expense to the table
        :return:
        '''
        try:
            #Establish Variables / Calculations
            expense_name = self.input_name.text()
            expense_cost = float(self.input_cost.text())
            expense_freq = float(self.input_freq.text())
            expense_monthly_cost = expense_cost * expense_freq
            expense_yearly_cost = expense_monthly_cost * 12
            expense = [expense_name , expense_cost, expense_freq, expense_monthly_cost, expense_yearly_cost]
            Logic_List.expense_list.append(expense)

            #Update Table
            row = 0
            self.table_expenses.setRowCount(len(Logic_List.expense_list))
            for exp in Logic_List.expense_list:
                self.table_expenses.setItem(row, 0, QtWidgets.QTableWidgetItem(exp[0]))
                self.table_expenses.setItem(row, 1, QtWidgets.QTableWidgetItem(f'{str(exp[1])}$'))
                self.table_expenses.setItem(row, 2, QtWidgets.QTableWidgetItem(str(exp[2])))
                self.table_expenses.setItem(row, 3, QtWidgets.QTableWidgetItem(f'{str(exp[3])}$'))
                self.table_expenses.setItem(row, 4, QtWidgets.QTableWidgetItem(f'{str(exp[4])}$'))
                row += 1
        except:
            self.input_cost.setText('Must Be Number')
            self.input_freq.setText('Must Be Number')

    def remove_expense(self) -> None:
        '''
        Removes an expense from the table
        Uses row number
        :return:
        '''
        try:
            row_num = int(self.input_row_rem.text())
            if (row_num -1) >= len(Logic_List.expense_list):
                self.input_row_rem.setText('Number Too High')
            elif (row_num - 1) < 0:
                self.input_row_rem.setText('Number Too Low')
            else:
                Logic_List.expense_list.pop(row_num - 1)
                row = 0
                self.table_expenses.setRowCount(len(Logic_List.expense_list))
                for exp in Logic_List.expense_list:
                    self.table_expenses.setItem(row, 0, QtWidgets.QTableWidgetItem(exp[0]))
                    self.table_expenses.setItem(row, 1, QtWidgets.QTableWidgetItem(f'{str(exp[1])}$'))
                    self.table_expenses.setItem(row, 2, QtWidgets.QTableWidgetItem(str(exp[2])))
                    self.table_expenses.setItem(row, 3, QtWidgets.QTableWidgetItem(f'{str(exp[3])}$'))
                    self.table_expenses.setItem(row, 4, QtWidgets.QTableWidgetItem(f'{str(exp[4])}$'))
                    print(row)
                    row += 1
        except:
            self.input_row_rem.setText('Must Be Number')

    def save(self) -> None:
        '''
        Saves the data to CSV file
        :return:
        '''
        with open(f'files\\{Logic_Input.login_list[0]}.csv', 'w', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)
            header = ['Name','Cost','Freq','Monthly Cost','Yearly Cost']
            csv_writer.writerow(header)
            for exp in Logic_List.expense_list:
                csv_writer.writerow(exp)

class Logic_Sum(QMainWindow, Ui_SumWindow):
    '''
    Class that applies the Summary GUI
    Also houses functions return2 and update
     '''
    def __init__(self) -> None:
        '''
        Initializes Summary GUI
        '''
        super().__init__()
        self.setupUi(self)
        self.button_return.clicked.connect(lambda: self.return2())
        self.button_upda.clicked.connect(lambda: self.update())

    def return2(self) -> None:
        '''
        :return: Access List GUI
        '''
        self.application = QApplication([])
        self.window = Logic_List()
        self.window.show()
        self.application.exec()

    def update(self) -> None:
        '''
        Uses the variables income, savings, and goal in order to
        determine the time and status of the users expenses
        :return:
        '''
        try:
            #Establish Variables / Calculate Monthly Profit
            monthly_income = float(self.input_income.text())
            savings = float(self.input_save.text())
            goal = float(self.input_goal.text())
            if monthly_income < 0:
                self.input_income.setText('Must Be Positive')
            elif goal < 0:
                self.input_goal.setText('Must Be Positive')
            else:
                monthly_expense = 0
                for item in Logic_List.expense_list:
                    monthly_expense += item[3]
                if monthly_income <= monthly_expense:
                    self.label_out_month.setText(f'None')
                    self.label_out_time.setText(f'Never')
                    self.label_out_status.setText('RED ALERT!')
                else:
                    monthly_profit = monthly_income - monthly_expense
                    self.label_out_month.setText(f'{str(monthly_profit)}$')

                    #Calculate Goal_time Into Years and Months
                    goal_time = (goal - savings) // monthly_profit
                    year_time = 0
                    if goal % monthly_profit != 0:
                        goal_time += 1
                    if goal_time // 12 == 0:
                        month_time = int(goal_time % 12)
                        if month_time == 1:
                            self.label_out_time.setText(f'{str(month_time)} month')
                        else:
                            self.label_out_time.setText(f'{str(month_time)} months')
                    elif goal_time % 12 != 0:
                        year_time = int(goal_time // 12)
                        month_time = int(goal_time % 12)
                        if year_time == 1 and month_time == 1:
                            self.label_out_time.setText(f'{str(year_time)} year, {str(month_time)} month')
                        elif year_time == 1:
                            self.label_out_time.setText(f'{str(year_time)} year, {str(month_time)} months')
                        elif month_time == 1:
                            self.label_out_time.setText(f'{str(year_time)} years, {str(month_time)} month')
                        else:
                            self.label_out_time.setText(f'{str(year_time)} years, {str(month_time)} months')
                    else:
                        year_time = int(goal_time // 12)
                        if year_time == 1:
                            self.label_out_time.setText(f'{str(year_time)} year')
                        else:
                            self.label_out_time.setText(f'{str(year_time)} years')

                    #Determine Money Status
                    if year_time == 0:
                        self.label_out_status.setText('Excellent')
                        status = 2
                    elif year_time <= 2:
                        self.label_out_status.setText('Ok')
                        status = 1
                    elif year_time < 10:
                        self.label_out_status.setText('Bad')
                        status = 0
                    else:
                        self.label_out_status.setText('EMERGENCY')
                        status = -1
        except:
            self.input_income.setText('Must be Number')
            self.input_goal.setText('Must be Number')
            self.input_save.setText('Must be Number')

