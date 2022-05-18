from msilib.schema import Error
from Main_window import *

import sys
import numpy as np

class Function_Plotter(Ui_MainWindow):

    def __init__(self, window) :
        self.setupUi(window)
        # click listener
        self.plot_button.clicked.connect(self.plot)

    func = ""
    min = ""
    max = ""

    def plot(self) :
        # clear the error field and the plot
        self.error_label.setText("")
        self.graphicsView.clear()
        # assign the input fields and check for min and max inputs
        self.func = self.function_text.text()
        if self.is_number(self.min_text.text()):
            self.min = int(self.min_text.text())
        else :
            print("Input Error: Min value isn't a numeric value or empty !!")
            self.error_label.setText("Input Error: Min value isn't a numeric value or empty!!")
            
            return
        if self.is_number(self.max_text.text()) :
            self.max = int(self.max_text.text())
        else :
            print("Input Error: Max value isn't a numeric value or empty !!")
            self.error_label.setText("Input Error: Max value isn't a numeric value or empty!!")
            return

        # Check
        if (self.check(self.min, self.max) == True):
            # Plot
            x_list = np.arange(self.min, self.max+0.1, 0.1)
            #x_list = np.arange(-10, 10.1, 0.1)
            self.func = self.fix_power_sign(self.func)
            try :
                y_list = self.f(self.func, x_list)
                self.graphicsView.plot(x_list, y_list, pen=5)
            except Exception as err:
                print("Input Error: Invalid function input - {0}".format(err))
                self.error_label.setText("Input Error: Invalid function input !!")


        else :
            # Clear the plot
            print("Input Error: Min value couldn't be bigger than Max value !!")
            self.error_label.setText("Input Error: Min value couldn't be bigger than Max value !!")
            print("Clear the plot")


    # Check if the input min and max inputs are correct
    def check(self, min, max) :
        if min >= max :
            return False

        return True


    # Check if the function input is correct and Calculate y = f(x)
    def f(self, func, x) :
        try :
            y_list = eval(func)
            # eval("3*x^2+1*x+4") 
            return y_list
        except Exception as err:
            raise err


    # Check if a string is a number
    def is_number(self, string):
        if len(string) == 0 :
            return False
        if string[0] == '-':
            return string[1:].isnumeric()
        else:
            return string.isnumeric()


    # fix the power sign
    def fix_power_sign(self, funct):
        return funct.replace("^", "**")


app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()

# Create an instance of the app
ui = Function_Plotter(MainWindow)

# show the window and start the app
MainWindow.show()
app.exec_()