'''
Author: BOKTIAR AHMED BAPPY
Designation: Data Scientist
Date: 14/04/1022
Email: 1. boktiar@ineuron.ai  2. entbappy73@gmail.com
'''

import sys
from PyQt5.QtWidgets import QApplication
from desktop_business_logic_layer.business_logic import Gui_Start



def main():
    """This method is used to start the application.
    Args: None.
    Returns: None.
    """
    GuiApp = QApplication(sys.argv)
    gui_Start = Gui_Start()
    gui_Start.show()
    sys.exit(GuiApp.exec_())


if __name__ == '__main__':
    main()