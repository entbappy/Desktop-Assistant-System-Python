'''
Author: BOKTIAR AHMED BAPPY
Designation: Data Scientist
Date: 14/04/1022
Email: 1. boktiar@ineuron.ai  2. entbappy73@gmail.com
'''

import os
import sys
import uuid
import pyautogui
import webbrowser
import wikipedia
import datetime
import random
import cv2
import time
import pyjokes
import pywhatkit as kit
from requests import get
from desktop_entity_layer.assistant_speak.speaker import Speaker
from desktop_entity_layer.recognize_voice.recognizer import SpeechRecognizer
from desktop_entity_layer.wish_me.wish import WishMe
from desktop_config_layer.configuration import AssistantConfiguration
from desktop_entity_layer.email_sender.emailSender import EmailSender
from desktop_exception_layer.exception import GenericException as TasksException
from desktop_logging_layer.logger.log_request import LogRequest
from desktop_logging_layer.logger.log_exception import LogExceptionDetail


class AssistantTasks:
    def __init__(self):
        try:
            self.SPEAK = Speaker()
            self.SPEACH_RECOGNIZER = SpeechRecognizer()
            self.WISH_ME = WishMe()
            self.CONFIG = AssistantConfiguration()
            self.EMAIL_SENDER = EmailSender()
        
        except Exception as e:
            tasks_exception = TasksException(
                "Failed during setting up tasks params in module [{0}] class [{1}] method [{2}]"
                    .format(self.__module__, AssistantTasks.__name__,
                            self.__init__.__name__))
            raise Exception(tasks_exception.error_message_detail(str(e), sys)) from e

    
    def greeting(self):
        self.SPEAK.speak("Starting Engine")
        self.SPEAK.speak("Collecting required resources")
        self.SPEAK.speak("Initializing")
        self.SPEAK.speak("Getting information from system")
        self.SPEAK.speak("Connecting to mail services")
        self.SPEAK.speak("Connecting with your all social media")
        self.SPEAK.speak("Connecting with your all required services")
        self.SPEAK.speak("All processes are done, Now i am online")
        self.WISH_ME.wishMe()


    def myAssistantTasks(self):
        """This method is used to perform all the tasks.
        returns: None.
        Note: You can more tasks in this method as per your requirement.
        """
        
        self.greeting()

        while True:
            query = self.SPEACH_RECOGNIZER.listen().lower()

            if 'wikipedia' in query:
                try:
                    log_writer = LogRequest(execution_id=str(uuid.uuid4()))
                    log_writer.log_start(query)

                    self.SPEAK.speak('Searching Wikipedia...')
                    query = query.replace("wikipedia", "")
                    results = wikipedia.summary(query, sentences=2)
                    self.SPEAK.speak("According to Wikipedia")
                    print(results)
                    self.SPEAK.speak(results)

                    result = {'status': True}
                    log_writer.log_stop(result)
                except Exception as e:
                    exc_type, exc_obj, exc_tb = sys.exc_info()
                    file_name = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                    exception_type = e.__repr__()
                    exception_detail = {'exception_type': exception_type,
                                'file_name': file_name, 'line_number': exc_tb.tb_lineno,
                                'detail': sys.exc_info().__str__()}

                    log_exception=LogExceptionDetail(log_writer.execution_id)
                    log_exception.log(str(exception_detail))
                    context={'status': False}
                    log_writer.log_stop(context)
                    raise Exception(e) from e


            elif 'open terminal' in query:
                try:
                    log_writer = LogRequest(execution_id=str(uuid.uuid4()))
                    log_writer.log_start(query)
                    self.SPEAK.speak('Opening Terminal...')
                    os.system("start cmd")
                    # codePath = "C:\WINDOWS\system32\\cmd.exe"
                    # os.startfile(codePath)
                    result = {'status': True}
                    log_writer.log_stop(result)
                except Exception as e:
                    exc_type, exc_obj, exc_tb = sys.exc_info()
                    file_name = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                    exception_type = e.__repr__()
                    exception_detail = {'exception_type': exception_type,
                                'file_name': file_name, 'line_number': exc_tb.tb_lineno,
                                'detail': sys.exc_info().__str__()}

                    log_exception=LogExceptionDetail(log_writer.execution_id)
                    log_exception.log(str(exception_detail))
                    context={'status': False}
                    log_writer.log_stop(context)
                    raise Exception(e) from e


            elif 'close terminal' in query:
                try:
                    log_writer = LogRequest(execution_id=str(uuid.uuid4()))
                    log_writer.log_start(query)
                    self.SPEAK.speak('Closing terminal')
                    codePath = "taskkill /f /im cmd.exe"
                    os.system(codePath)
                    result = {'status': True}
                    log_writer.log_stop(result)
                except Exception as e:
                    exc_type, exc_obj, exc_tb = sys.exc_info()
                    file_name = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                    exception_type = e.__repr__()
                    exception_detail = {'exception_type': exception_type,
                                'file_name': file_name, 'line_number': exc_tb.tb_lineno,
                                'detail': sys.exc_info().__str__()}

                    log_exception=LogExceptionDetail(log_writer.execution_id)
                    log_exception.log(str(exception_detail))
                    context={'status': False}
                    log_writer.log_stop(context)
                    raise Exception(e) from e


            elif 'open youtube' in query:
                try:
                    log_writer = LogRequest(execution_id=str(uuid.uuid4()))
                    log_writer.log_start(query)
                    self.SPEAK.speak('Opening youtube...')
                    webbrowser.open("youtube.com")
                    result = {'status': True}
                    log_writer.log_stop(result)
                except Exception as e:
                    exc_type, exc_obj, exc_tb = sys.exc_info()
                    file_name = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                    exception_type = e.__repr__()
                    exception_detail = {'exception_type': exception_type,
                                'file_name': file_name, 'line_number': exc_tb.tb_lineno,
                                'detail': sys.exc_info().__str__()}

                    log_exception=LogExceptionDetail(log_writer.execution_id)
                    log_exception.log(str(exception_detail))
                    context={'status': False}
                    log_writer.log_stop(context)
                    raise Exception(e) from e


            elif 'open google' in query:
                try:
                    log_writer = LogRequest(execution_id=str(uuid.uuid4()))
                    log_writer.log_start(query)
                    self.SPEAK.speak('Opening google... What do you want to search?')
                    s_query = self.SPEACH_RECOGNIZER.listen().lower()
                    webbrowser.open(f"{s_query}")
                    result = {'status': True}
                    log_writer.log_stop(result)
                except Exception as e:
                    exc_type, exc_obj, exc_tb = sys.exc_info()
                    file_name = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                    exception_type = e.__repr__()
                    exception_detail = {'exception_type': exception_type,
                                'file_name': file_name, 'line_number': exc_tb.tb_lineno,
                                'detail': sys.exc_info().__str__()}

                    log_exception=LogExceptionDetail(log_writer.execution_id)
                    log_exception.log(str(exception_detail))
                    context={'status': False}
                    log_writer.log_stop(context)
                    raise Exception(e) from e
            

            elif 'close google' in query:
                try:
                    log_writer = LogRequest(execution_id=str(uuid.uuid4()))
                    log_writer.log_start(query)
                    self.SPEAK.speak('Closing google ...')
                    codePath = "taskkill /f /im iexplore.exe"
                    os.system(codePath)
                    result = {'status': True}
                    log_writer.log_stop(result)
                except Exception as e:
                    exc_type, exc_obj, exc_tb = sys.exc_info()
                    file_name = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                    exception_type = e.__repr__()
                    exception_detail = {'exception_type': exception_type,
                                'file_name': file_name, 'line_number': exc_tb.tb_lineno,
                                'detail': sys.exc_info().__str__()}

                    log_exception=LogExceptionDetail(log_writer.execution_id)
                    log_exception.log(str(exception_detail))
                    context={'status': False}
                    log_writer.log_stop(context)
                    raise Exception(e) from e


            elif 'open stackoverflow' in query:
                try:
                    log_writer = LogRequest(execution_id=str(uuid.uuid4()))
                    log_writer.log_start(query)
                    self.SPEAK.speak('Opening stackoverflow...')
                    webbrowser.open("stackoverflow.com")
                    result = {'status': True}
                    log_writer.log_stop(result)
                except Exception as e:
                    exc_type, exc_obj, exc_tb = sys.exc_info()
                    file_name = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                    exception_type = e.__repr__()
                    exception_detail = {'exception_type': exception_type,
                                'file_name': file_name, 'line_number': exc_tb.tb_lineno,
                                'detail': sys.exc_info().__str__()}

                    log_exception=LogExceptionDetail(log_writer.execution_id)
                    log_exception.log(str(exception_detail))
                    context={'status': False}
                    log_writer.log_stop(context)
                    raise Exception(e) from e


            elif 'play music' in query:
                try:
                    log_writer = LogRequest(execution_id=str(uuid.uuid4()))
                    log_writer.log_start(query)
                    self.SPEAK.speak('Playing music...')
                    music_dir = self.CONFIG.YOUR_MUSIC_DIR
                    songs = os.listdir(music_dir)
                    for song in songs:
                        if song.endswith('.mp3'):
                            num_of_music = len(songs)
                            random_music = random.randint(0,num_of_music)
                            print(songs[random_music])
                            os.startfile(os.path.join(music_dir, songs[random_music]))
                            break
                    result = {'status': True}
                    log_writer.log_stop(result)
                except Exception as e:
                    exc_type, exc_obj, exc_tb = sys.exc_info()
                    file_name = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                    exception_type = e.__repr__()
                    exception_detail = {'exception_type': exception_type,
                                'file_name': file_name, 'line_number': exc_tb.tb_lineno,
                                'detail': sys.exc_info().__str__()}

                    log_exception=LogExceptionDetail(log_writer.execution_id)
                    log_exception.log(str(exception_detail))
                    context={'status': False}
                    log_writer.log_stop(context)
                    raise Exception(e) from e


            elif 'the time' in query:
                try:
                    log_writer = LogRequest(execution_id=str(uuid.uuid4()))
                    log_writer.log_start(query)
                    strTime = datetime.datetime.now().strftime("%H:%M:%S")
                    self.SPEAK.speak(f"Sir, the time is {strTime}")
                    result = {'status': True}
                    log_writer.log_stop(result)
                except Exception as e:
                    exc_type, exc_obj, exc_tb = sys.exc_info()
                    file_name = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                    exception_type = e.__repr__()
                    exception_detail = {'exception_type': exception_type,
                                'file_name': file_name, 'line_number': exc_tb.tb_lineno,
                                'detail': sys.exc_info().__str__()}

                    log_exception=LogExceptionDetail(log_writer.execution_id)
                    log_exception.log(str(exception_detail))
                    context={'status': False}
                    log_writer.log_stop(context)
                    raise Exception(e) from e


            elif 'open code' in query:
                try:
                    log_writer = LogRequest(execution_id=str(uuid.uuid4()))
                    log_writer.log_start(query)
                    self.SPEAK.speak('Opening code...')
                    codePath = self.CONFIG.YOUR_VS_CODE_PATH
                    os.startfile(codePath)
                    result = {'status': True}
                    log_writer.log_stop(result)
                except Exception as e:
                    exc_type, exc_obj, exc_tb = sys.exc_info()
                    file_name = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                    exception_type = e.__repr__()
                    exception_detail = {'exception_type': exception_type,
                                'file_name': file_name, 'line_number': exc_tb.tb_lineno,
                                'detail': sys.exc_info().__str__()}

                    log_exception=LogExceptionDetail(log_writer.execution_id)
                    log_exception.log(str(exception_detail))
                    context={'status': False}
                    log_writer.log_stop(context)
                    raise Exception(e) from e


            elif 'open pycharm' in query:
                try:
                    log_writer = LogRequest(execution_id=str(uuid.uuid4()))
                    log_writer.log_start(query)
                    self.SPEAK.speak('Opening pycharm...')
                    codePath = self.CONFIG.YOUR_PYCHARM_DIR
                    os.startfile(codePath)
                    result = {'status': True}
                    log_writer.log_stop(result)
                except Exception as e:
                    exc_type, exc_obj, exc_tb = sys.exc_info()
                    file_name = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                    exception_type = e.__repr__()
                    exception_detail = {'exception_type': exception_type,
                                'file_name': file_name, 'line_number': exc_tb.tb_lineno,
                                'detail': sys.exc_info().__str__()}

                    log_exception=LogExceptionDetail(log_writer.execution_id)
                    log_exception.log(str(exception_detail))
                    context={'status': False}
                    log_writer.log_stop(context)
                    raise Exception(e) from e


            elif 'open sublime' in query:
                try:
                    log_writer = LogRequest(execution_id=str(uuid.uuid4()))
                    log_writer.log_start(query)
                    self.SPEAK.speak('Opening sublime...')
                    codePath = self.CONFIG.YOUR_SUBLIME_DIR
                    os.startfile(codePath)
                    result = {'status': True}
                    log_writer.log_stop(result)
                except Exception as e:
                    exc_type, exc_obj, exc_tb = sys.exc_info()
                    file_name = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                    exception_type = e.__repr__()
                    exception_detail = {'exception_type': exception_type,
                                'file_name': file_name, 'line_number': exc_tb.tb_lineno,
                                'detail': sys.exc_info().__str__()}

                    log_exception=LogExceptionDetail(log_writer.execution_id)
                    log_exception.log(str(exception_detail))
                    context={'status': False}
                    log_writer.log_stop(context)
                    raise Exception(e) from e


            elif 'open visual code studio' in query:
                try:
                    log_writer = LogRequest(execution_id=str(uuid.uuid4()))
                    log_writer.log_start(query)
                    self.SPEAK.speak('Opening visual code studio...')
                    codePath = self.CONFIG.YOUR_VS_CODE_PATH
                    os.startfile(codePath)
                    result = {'status': True}
                    log_writer.log_stop(result)
                except Exception as e:
                    exc_type, exc_obj, exc_tb = sys.exc_info()
                    file_name = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                    exception_type = e.__repr__()
                    exception_detail = {'exception_type': exception_type,
                                'file_name': file_name, 'line_number': exc_tb.tb_lineno,
                                'detail': sys.exc_info().__str__()}

                    log_exception=LogExceptionDetail(log_writer.execution_id)
                    log_exception.log(str(exception_detail))
                    context={'status': False}
                    log_writer.log_stop(context)
                    raise Exception(e) from e


            elif 'close visual code' in query:
                try:
                    log_writer = LogRequest(execution_id=str(uuid.uuid4()))
                    log_writer.log_start(query)
                    self.SPEAK.speak('Closing visual code studio...')
                    codePath = "taskkill /f /im Code.exe"
                    os.system(codePath)
                    result = {'status': True}
                    log_writer.log_stop(result)
                except Exception as e:
                    exc_type, exc_obj, exc_tb = sys.exc_info()
                    file_name = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                    exception_type = e.__repr__()
                    exception_detail = {'exception_type': exception_type,
                                'file_name': file_name, 'line_number': exc_tb.tb_lineno,
                                'detail': sys.exc_info().__str__()}

                    log_exception=LogExceptionDetail(log_writer.execution_id)
                    log_exception.log(str(exception_detail))
                    context={'status': False}
                    log_writer.log_stop(context)
                    raise Exception(e) from e



            elif 'open notepad' in query:
                try:
                    log_writer = LogRequest(execution_id=str(uuid.uuid4()))
                    log_writer.log_start(query)
                    codePath = self.CONFIG.YOUR_NOTEPAD_DIR
                    self.SPEAK.speak('Opening notepad...')
                    os.startfile(codePath)
                    result = {'status': True}
                    log_writer.log_stop(result)
                except Exception as e:
                    exc_type, exc_obj, exc_tb = sys.exc_info()
                    file_name = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                    exception_type = e.__repr__()
                    exception_detail = {'exception_type': exception_type,
                                'file_name': file_name, 'line_number': exc_tb.tb_lineno,
                                'detail': sys.exc_info().__str__()}

                    log_exception=LogExceptionDetail(log_writer.execution_id)
                    log_exception.log(str(exception_detail))
                    context={'status': False}
                    log_writer.log_stop(context)
                    raise Exception(e) from e


            elif 'close notepad' in query:
                try:
                    log_writer = LogRequest(execution_id=str(uuid.uuid4()))
                    log_writer.log_start(query)
                    self.SPEAK.speak('Closing notepad...')
                    codePath = "taskkill /f /im notepad.exe"
                    os.system(codePath)
                    result = {'status': True}
                    log_writer.log_stop(result)
                except Exception as e:
                    exc_type, exc_obj, exc_tb = sys.exc_info()
                    file_name = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                    exception_type = e.__repr__()
                    exception_detail = {'exception_type': exception_type,
                                'file_name': file_name, 'line_number': exc_tb.tb_lineno,
                                'detail': sys.exc_info().__str__()}

                    log_exception=LogExceptionDetail(log_writer.execution_id)
                    log_exception.log(str(exception_detail))
                    context={'status': False}
                    log_writer.log_stop(context)
                    raise Exception(e) from e


            elif 'open camera' in query:
                try:
                    log_writer = LogRequest(execution_id=str(uuid.uuid4()))
                    log_writer.log_start(query)
                    self.SPEAK.speak('Opening camera...')
                    cap = cv2.VideoCapture(0)
                    while True:
                        ret, frame = cap.read()
                        cv2.imshow('cam', frame)
                        k = cv2.waitKey(50)
                        if k==27:
                            break
                    cap.release()
                    cv2.destroyAllWindows()
                    result = {'status': True}
                    log_writer.log_stop(result)
                except Exception as e:
                    exc_type, exc_obj, exc_tb = sys.exc_info()
                    file_name = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                    exception_type = e.__repr__()
                    exception_detail = {'exception_type': exception_type,
                                'file_name': file_name, 'line_number': exc_tb.tb_lineno,
                                'detail': sys.exc_info().__str__()}

                    log_exception=LogExceptionDetail(log_writer.execution_id)
                    log_exception.log(str(exception_detail))
                    context={'status': False}
                    log_writer.log_stop(context)
                    raise Exception(e) from e
                # press ESC key to close camera



            elif 'ip address' in query:
                try:
                    log_writer = LogRequest(execution_id=str(uuid.uuid4()))
                    log_writer.log_start(query)
                    ip = get('https://api.ipify.org?format=json').json()['ip']
                    self.SPEAK.speak(f"Sir, your ip address is {ip}")
                    result = {'status': True}
                    log_writer.log_stop(result)
                except Exception as e:
                    exc_type, exc_obj, exc_tb = sys.exc_info()
                    file_name = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                    exception_type = e.__repr__()
                    exception_detail = {'exception_type': exception_type,
                                'file_name': file_name, 'line_number': exc_tb.tb_lineno,
                                'detail': sys.exc_info().__str__()}

                    log_exception=LogExceptionDetail(log_writer.execution_id)
                    log_exception.log(str(exception_detail))
                    context={'status': False}
                    log_writer.log_stop(context)
                    raise Exception(e) from e

            #send whats app message
            elif 'send message' in query:
                try:
                    log_writer = LogRequest(execution_id=str(uuid.uuid4()))
                    log_writer.log_start(query)
                    self.SPEAK.speak('OK sir, what do you want to send?')
                    kit.sendwhatmsg("+91 91671 80803","This is a test message send from my Python Assistant",2,25)
                    result = {'status': True}
                    log_writer.log_stop(result)
                except Exception as e:
                    exc_type, exc_obj, exc_tb = sys.exc_info()
                    file_name = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                    exception_type = e.__repr__()
                    exception_detail = {'exception_type': exception_type,
                                'file_name': file_name, 'line_number': exc_tb.tb_lineno,
                                'detail': sys.exc_info().__str__()}

                    log_exception=LogExceptionDetail(log_writer.execution_id)
                    log_exception.log(str(exception_detail))
                    context={'status': False}
                    log_writer.log_stop(context)
                    raise Exception(e) from e

                
            elif 'play songs on youtube' in query:
                try:
                    log_writer = LogRequest(execution_id=str(uuid.uuid4()))
                    log_writer.log_start(query)
                    self.SPEAK.speak('OK sir, what do you want to search?')
                    s_query = self.SPEACH_RECOGNIZER.listen().lower()
                    kit.playonyt(f"{s_query}")
                    result = {'status': True}
                    log_writer.log_stop(result)
                except Exception as e:
                    exc_type, exc_obj, exc_tb = sys.exc_info()
                    file_name = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                    exception_type = e.__repr__()
                    exception_detail = {'exception_type': exception_type,
                                'file_name': file_name, 'line_number': exc_tb.tb_lineno,
                                'detail': sys.exc_info().__str__()}

                    log_exception=LogExceptionDetail(log_writer.execution_id)
                    log_exception.log(str(exception_detail))
                    context={'status': False}
                    log_writer.log_stop(context)
                    raise Exception(e) from e

            
            
            elif 'email to' in query:
                try:
                    log_writer = LogRequest(execution_id=str(uuid.uuid4()))
                    log_writer.log_start(query)
                    self.SPEAK.speak('OK sir, what do you want to send?')
                    content = self.SPEACH_RECOGNIZER.listen().lower()
                    to = self.CONFIG.RECIEVER_EMAIL_ID
                    self.EMAIL_SENDER.send_email(to, content)
                    self.SPEAK.speak("Email has been sent!")
                    result = {'status': True}
                    log_writer.log_stop(result)
                except Exception as e:
                    print(e)
                    self.SPEAK.speak("Sorry sir, I am not able to send this email")
                    exc_type, exc_obj, exc_tb = sys.exc_info()
                    file_name = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                    exception_type = e.__repr__()
                    exception_detail = {'exception_type': exception_type,
                                'file_name': file_name, 'line_number': exc_tb.tb_lineno,
                                'detail': sys.exc_info().__str__()}

                    log_exception=LogExceptionDetail(log_writer.execution_id)
                    log_exception.log(str(exception_detail))
                    context={'status': False}
                    log_writer.log_stop(context)
                    


            elif 'tell me a joke' in query:
                try:
                    log_writer = LogRequest(execution_id=str(uuid.uuid4()))
                    log_writer.log_start(query)
                    self.SPEAK.speak('OK sir, Here is a joke for you')
                    self.SPEAK.speak(pyjokes.get_joke())
                    result = {'status': True}
                    log_writer.log_stop(result)
                except Exception as e:
                    exc_type, exc_obj, exc_tb = sys.exc_info()
                    file_name = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                    exception_type = e.__repr__()
                    exception_detail = {'exception_type': exception_type,
                                'file_name': file_name, 'line_number': exc_tb.tb_lineno,
                                'detail': sys.exc_info().__str__()}

                    log_exception=LogExceptionDetail(log_writer.execution_id)
                    log_exception.log(str(exception_detail))
                    context={'status': False}
                    log_writer.log_stop(context)
                    raise Exception(e) from e



            elif 'where am i' in query:
                try:
                    log_writer = LogRequest(execution_id=str(uuid.uuid4()))
                    log_writer.log_start(query)
                    self.SPEAK.speak('wait sir, let me check')
                    idAdd = get('https://api.ipify.org').text
                    url = 'https://get.geojs.io/v1/ip/geo/' + idAdd + '.json'
                    geo_request = get(url)
                    geo_data = geo_request.json()
                    city = geo_data['city']
                    country = geo_data['country']
                    self.SPEAK.speak(f"Sir, you are in {city} {country}")
                    result = {'status': True}
                    log_writer.log_stop(result)
                except Exception as e:
                    print(e)
                    self.SPEAK.speak("Sorry sir, I am not able to find your location")
                    exc_type, exc_obj, exc_tb = sys.exc_info()
                    file_name = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                    exception_type = e.__repr__()
                    exception_detail = {'exception_type': exception_type,
                                'file_name': file_name, 'line_number': exc_tb.tb_lineno,
                                'detail': sys.exc_info().__str__()}

                    log_exception=LogExceptionDetail(log_writer.execution_id)
                    log_exception.log(str(exception_detail))
                    context={'status': False}
                    log_writer.log_stop(context)
                    pass

            
            elif "take a screenshot" in query:
                try: 
                    log_writer = LogRequest(execution_id=str(uuid.uuid4()))
                    log_writer.log_start(query)
                    self.SPEAK.speak("OK sir, let me take a screenshot, Tell me the name of the screenshot")
                    name = self.SPEACH_RECOGNIZER.listen().lower()
                    time.sleep(2)
                    img = pyautogui.screenshot()
                    img.save(f"{name}.png")
                    self.SPEAK.speak("Screenshot has been taken, Please check your folder")
                    result = {'status': True}
                    log_writer.log_stop(result)
                except Exception as e:
                    exc_type, exc_obj, exc_tb = sys.exc_info()
                    file_name = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                    exception_type = e.__repr__()
                    exception_detail = {'exception_type': exception_type,
                                'file_name': file_name, 'line_number': exc_tb.tb_lineno,
                                'detail': sys.exc_info().__str__()}

                    log_exception=LogExceptionDetail(log_writer.execution_id)
                    log_exception.log(str(exception_detail))
                    context={'status': False}
                    log_writer.log_stop(context)
                    raise Exception(e) from e


            elif "love letter" in query:
                try:
                    log_writer = LogRequest(execution_id=str(uuid.uuid4()))
                    log_writer.log_start(query)
                    self.SPEAK.speak("Sure, I am writing..")
                    npath = self.CONFIG.YOUR_NOTEPAD_DIR
                    os.startfile(npath)
                    time.sleep(2)
                    love = """Dear _____,

                    I know I am in love because I see you every way I turn--no matter what I am doing. 
                    I know I want to be with you, not just with you, but share everything with you, too. 
                    Just being close to you is not enough for me. I want to be a part of you; A part of your 
                    life forever. I never have to wonder if you love me. You complete me--my heart and my soul.

                    You're my best friend, my lover, and my soul mate. You have been there and supported me 
                    like no one else has before. I'm lost without you. I love you more than life itself. 
                    There are no words I can say to truly tell you how much I really love you. 
                    I couldn't picture myself without you in my life. You are perfect for me in every possible 
                    way, and I want to spend the rest of my life with you.

                    You give me reason to strive for more of everything. 
                    I learn more and more from you every day. My heart is forever yours. 
                    I know saying, "I love you" is powerful, yet I feel it's not enough. 
                    My life was a wreck before now. I never thought it would change, 
                    but you came into my life and everything took a turn for the best. 
                    You show me the value of life. You give me the most amazing feelings inside. 
                    It feels great to actually love and be loved in return. We have been friends for over 
                    three years now, and I know we have only been dating for a short time now, 
                    but I know our love will last a lifetime. 
                    I can't wait until I am your wife. I love you with all my heart. I am yours forever.

                    Sincerely,
                    Neuron"""

                    pyautogui.typewrite(love)
                    self.SPEAK.speak("Your love letter has been completed, Now you can send it to your girlfriend")
                    result = {'status': True}
                    log_writer.log_stop(result)
                except Exception as e:
                    exc_type, exc_obj, exc_tb = sys.exc_info()
                    file_name = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                    exception_type = e.__repr__()
                    exception_detail = {'exception_type': exception_type,
                                'file_name': file_name, 'line_number': exc_tb.tb_lineno,
                                'detail': sys.exc_info().__str__()}

                    log_exception=LogExceptionDetail(log_writer.execution_id)
                    log_exception.log(str(exception_detail))
                    context={'status': False}
                    log_writer.log_stop(context)
                    raise Exception(e) from e

            
            elif 'close this' in query:
                try:
                    log_writer = LogRequest(execution_id=str(uuid.uuid4()))
                    log_writer.log_start(query)
                    self.SPEAK.speak('ok sir...')
                    codePath = "taskkill /f /im notepad.exe"
                    os.system(codePath)
                    result = {'status': True}
                    log_writer.log_stop(result)
                except Exception as e:
                    exc_type, exc_obj, exc_tb = sys.exc_info()
                    file_name = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                    exception_type = e.__repr__()
                    exception_detail = {'exception_type': exception_type,
                                'file_name': file_name, 'line_number': exc_tb.tb_lineno,
                                'detail': sys.exc_info().__str__()}

                    log_exception=LogExceptionDetail(log_writer.execution_id)
                    log_exception.log(str(exception_detail))
                    context={'status': False}
                    log_writer.log_stop(context)
                    raise Exception(e) from e

                


            elif 'ok bye' in query:
                log_writer = LogRequest(execution_id=str(uuid.uuid4()))
                log_writer.log_start(query)
                self.SPEAK.speak('OK sir, Have a nice day, I am always for you')
                result = {'status': True}
                log_writer.log_stop(result)
                sys.exit()
            


            ## Add more data & tasks as per your requirements