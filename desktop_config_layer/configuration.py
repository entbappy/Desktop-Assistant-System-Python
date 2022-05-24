import os 
import sys
from desktop_utils_layer.utils import CommonUtils
from desktop_exception_layer.exception import GenericException as ConfigurationException


class AssistantConfiguration:
    def __init__(self):
        try:
            #Reading yaml file
            self.configs = CommonUtils().read_yaml('config.yaml')
            self.EMAIL_CONFIG = self.configs['EMAIL_CONFIG']
            self.DATABASE_CONFIG = self.configs['DATABASE_CONFIG']
            self.FILE_PATHS = self.configs['FILE_PATHS']
            self.GUI_MATERIALS_DIR = self.configs['GUI_MATERIALS_DIR']

            #Email
            self.YOUR_EMAIL_ID = self.EMAIL_CONFIG['YOUR_EMAIL_ID']
            self.YOUR_EMAIL_PASS = self.EMAIL_CONFIG['YOUR_EMAIL_PASS']
            self.RECIEVER_EMAIL_ID = self.EMAIL_CONFIG['RECIEVER_EMAIL_ID']
            #Files
            self.YOUR_MUSIC_DIR = self.FILE_PATHS['YOUR_MUSIC_DIR']
            self.YOUR_VS_CODE_PATH = self.FILE_PATHS['YOUR_VS_CODE_PATH']
            self.YOUR_PYCHARM_DIR = self.FILE_PATHS['YOUR_PYCHARM_DIR']
            self.YOUR_SUBLIME_DIR = self.FILE_PATHS['YOUR_SUBLIME_DIR']
            self.YOUR_NOTEPAD_DIR = self.FILE_PATHS['YOUR_NOTEPAD_DIR']
            #GUI
            self.BACKGROUND_IMAGE_DIR = self.GUI_MATERIALS_DIR['BACKGROUND_IMAGE_DIR']
            self.INITIALIZING_GIF_DIR = self.GUI_MATERIALS_DIR['INITIALIZING_GIF_DIR']
            self.CODE_LEFT_GIF_DIR = self.GUI_MATERIALS_DIR['CODE_LEFT_GIF_DIR']
            self.CODE_MIDDLE_GIF_DIR = self.GUI_MATERIALS_DIR['CODE_MIDDLE_GIF_DIR']
            self.EARTH_GIF_DIR = self.GUI_MATERIALS_DIR['EARTH_GIF_DIR']
            self.LOGO_IMAGE_DIR = self.GUI_MATERIALS_DIR['LOGO_IMAGE_DIR']
            self.VOICE_GIF_DIR = self.GUI_MATERIALS_DIR['VOICE_GIF_DIR']
            self.LOADING_GIF_DIR = self.GUI_MATERIALS_DIR['LOADING_GIF_DIR']
            self.HEALTH_GIF_DIR = self.GUI_MATERIALS_DIR['HEALTH_GIF_DIR']
            self.FRAME_IMAGE_DIR = self.GUI_MATERIALS_DIR['FRAME_IMAGE_DIR']
            #DATABASE
            self.ATLAS_CLUSTER_USERNAME = self.DATABASE_CONFIG['ATLAS_CLUSTER_USERNAME']
            self.ATLAS_CLUSTER_PASSWORD = self.DATABASE_CONFIG['ATLAS_CLUSTER_PASSWORD']
            self.IS_ATLAS = self.DATABASE_CONFIG['IS_ATLAS']
            self.DB_NAME = self.DATABASE_CONFIG['DB_NAME']
        

        except Exception as e:
            configuration_exception = ConfigurationException(
                "Failed during initializing assistant configuration in module [{0}] class [{1}] method [{2}]"
                    .format(self.__module__, AssistantConfiguration.__name__,
                            self.__init__.__name__))
            raise Exception(configuration_exception.error_message_detail(str(e), sys)) from e
