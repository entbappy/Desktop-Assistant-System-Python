import sys
import pyttsx3
from desktop_exception_layer.exception import GenericException as SpeakException


class Speaker:
    def __init__(self):
        try:
            self.engine = pyttsx3.init('sapi5')
            self.voices = self.engine.getProperty('voices')
            self.engine.setProperty('voice', self.voices[0].id)  # set the voice to use (1=Female, 0=Male)

        except Exception as e:
            speak_exception = SpeakException(
                "Failed during setting up voice for speaker in module [{0}] class [{1}] method [{2}]"
                    .format(self.__module__, Speaker.__name__,
                            self.__init__.__name__))
            raise Exception(speak_exception.error_message_detail(str(e), sys)) from e


    # text to speech conversion
    def speak(self,text):
        """This method is used to speak the text.

        Args:
            text (_str_): text to be spoken.
        """
        try:
            self.engine.say(text)
            print(text)
            self.engine.runAndWait()

        except Exception as e:
            speak_exception = SpeakException(
                "Failed during speak in module [{0}] class [{1}] method [{2}]"
                    .format(self.__module__, Speaker.__name__,
                            self.speak.__name__))
            raise Exception(speak_exception.error_message_detail(str(e), sys)) from e

        