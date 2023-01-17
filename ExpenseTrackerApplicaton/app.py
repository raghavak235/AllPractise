# Working with expense tracker is pretty easy, if I don't say also, then also you all will do it.
#
# You can seek the help by pressing H
# At first, Press C to continue or H to take help
# Press 1 to load your database or storage
# Press 2 to load your salary
# Press 3 to insert your expenses in the database
# Press 4 to see your expenses with core details
# Press 5 to update your expenses
# Press 6 to delete your expenses
# Press 7 to change your salary
# Press 8 to see your expenses in other currency
# Press 9 to exit or quit

import mysql.connector
class ExpenseTracker:
    def __init__(self):
        self.salary = None


    def load_database(self):
        import mysql.connector

        connection = mysql.connector.connect(host='localhost',
                                             database='employees',
                                             user='root',
                                             password='Chotabheem92')

    pass

    def load_salary(self, salary):
        self.salary = salary
        print(self.salary)
        pass

    def insert_expenses(self, expenses):

        pass

ep = ExpenseTracker()
ep.load_database()