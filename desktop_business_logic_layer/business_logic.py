'''
Author: BOKTIAR AHMED BAPPY
Designation: Data Scientist
Date: 14/04/1022
Email: 1. boktiar@ineuron.ai  2. entbappy73@gmail.com
'''

import sys
from desktop_presentation_layer.assistant_gui.gui import Ui_iNeuronDesktopAssistant
from PyQt5 import QtGui
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, QTimer, QTime, QDate
from desktop_business_logic_layer.assistant_tasks.tasks import AssistantTasks
from desktop_exception_layer.exception import GenericException as LogicException
from desktop_config_layer.configuration import AssistantConfiguration


class MainThread(QThread):
    def __init__(self):
        super(MainThread, self).__init__()
        self.tasks_run = AssistantTasks()

    
    def run(self):
        """This method is used to perform all the tasks

        returns: None.
        """
        try:
            self.tasks_run.myAssistantTasks()

        except Exception as e:
            logic_exception = LogicException(
                "Failed during running assistant tasks in module [{0}] class [{1}] method [{2}]"
                    .format(self.__module__, MainThread.__name__,
                            self.run.__name__))
            raise Exception(logic_exception.error_message_detail(str(e), sys)) from e


startExe = MainThread()


class Gui_Start(QMainWindow):
    def __init__(self):
        try:
            super().__init__()
            self.ui = Ui_iNeuronDesktopAssistant()
            self.ui.setupUi(self) 
            self.ui.startButton_.clicked.connect(self.startTask)
            self.ui.exitButton.clicked.connect(self.close)
            self.config = AssistantConfiguration()

        except Exception as e:
            logic_exception = LogicException(
                "Failed during GUI start in module [{0}] class [{1}] method [{2}]"
                    .format(self.__module__, Gui_Start.__name__,
                            self.__init__.__name__))
            raise Exception(logic_exception.error_message_detail(str(e), sys)) from e


    def showTimeLive(self):
        """This method is used to show time and date.
        Args: None.
        Returns: None.
        """
        try:
            TIME = QTime.currentTime()
            time_text = TIME.toString()
            DATE = QDate.currentDate()
            date_text = DATE.toString()

            label_time = "Time :" + time_text 
            label_date = "Date :" + date_text 

            self.ui.text_time.setText(label_time)
            self.ui.text_date.setText(label_date)
        
        except Exception as e:
            logic_exception = LogicException(
                "Failed during showing live time & date in module [{0}] class [{1}] method [{2}]"
                    .format(self.__module__, Gui_Start.__name__,
                            self.showTimeLive.__name__))
            raise Exception(logic_exception.error_message_detail(str(e), sys)) from e


    def startTask(self):
        """This method is used to start the assistant tasks & UI.
        Args: None.
        Returns: None.
        """
        try:
            self.ui.label1 = QtGui.QMovie(self.config.INITIALIZING_GIF_DIR)  #INITIALIZING_GIF_DIR
            self.ui.initializing_gif.setMovie(self.ui.label1)
            self.ui.label1.start()
            
            self.ui.label2 = QtGui.QMovie(self.config.CODE_LEFT_GIF_DIR)  #CODE_LEFT_GIF_DIR
            self.ui.prog_gif.setMovie(self.ui.label2)
            self.ui.label2.start()

            self.ui.label3 = QtGui.QMovie(self.config.EARTH_GIF_DIR)  #EARTH_GIF_DIR
            self.ui.world_gif.setMovie(self.ui.label3)
            self.ui.label3.start()

            self.ui.label4 = QtGui.QMovie(self.config.LOADING_GIF_DIR)  #LOADING_GIF_DIR
            self.ui.loading_gif.setMovie(self.ui.label4)
            self.ui.label4.start()

            self.ui.label5 = QtGui.QMovie(self.config.VOICE_GIF_DIR)  #VOICE_GIF_DIR
            self.ui.round_gif.setMovie(self.ui.label5)
            self.ui.label5.start()

            self.ui.label6 = QtGui.QMovie(self.config.CODE_MIDDLE_GIF_DIR)  #CODE_MIDDLE_GIF_DIR
            self.ui.prg2_gif.setMovie(self.ui.label6)
            self.ui.label6.start()

            self.ui.label7 = QtGui.QMovie(self.config.HEALTH_GIF_DIR)  #HEALTH_GIF_DIR
            self.ui.human_gif.setMovie(self.ui.label7)
            self.ui.label7.start()

            timer = QTimer(self)
            timer.timeout.connect(self.showTimeLive)
            timer.start(999)

            startExe.start()
        
        except Exception as e:
            logic_exception = LogicException(
                "Failed during starting tasks & UI in module [{0}] class [{1}] method [{2}]"
                    .format(self.__module__, Gui_Start.__name__,
                            self.startTask.__name__))
            raise Exception(logic_exception.error_message_detail(str(e), sys)) from e


      



    