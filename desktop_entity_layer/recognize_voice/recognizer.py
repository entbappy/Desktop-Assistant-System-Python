
import sys
import speech_recognition as sr
from desktop_entity_layer.assistant_speak.speaker import Speaker
from desktop_exception_layer.exception import GenericException as RecognizeException


class SpeechRecognizer:
    def __init__(self, language='en-in'):
        try:
            self.language = language
            self.r = sr.Recognizer()
            self.m = sr.Microphone()
            self.SPEAK = Speaker()
        
        except Exception as e:
            recognize_exception = RecognizeException(
                "Failed during setting up recognizer in module [{0}] class [{1}] method [{2}]"
                    .format(self.__module__, SpeechRecognizer.__name__,
                            self.__init__.__name__))
            raise Exception(recognize_exception.error_message_detail(str(e), sys)) from e
            

    def listen(self):
        """This method is used to listen the voice.
        Returns: query (_str_): query from user.
        """
       
        with self.m as source:
            print("Listening...")
            self.r.pause_threshold = 1
            audio = self.r.listen(source)
        try:
            print("Recognizing...")
            query = self.r.recognize_google(audio, language=self.language)
            print(f"User said: {query}\n")

        except Exception as e:
            self.SPEAK.speak("Say that again please...")
            return "None"
        return query



