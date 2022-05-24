import sys
import time
import datetime
from desktop_entity_layer.assistant_speak.speaker import Speaker
from desktop_exception_layer.exception import GenericException as WishException


class WishMe:
    def __init__(self):
        try:
            self.SPEAK = Speaker()
            self.HOUR = int(datetime.datetime.now().hour)
            self.TIME = time.strftime('%I:%M:%p')

        except Exception as e:
            wish_exception = WishException(
                "Failed during setting up wish params in module [{0}] class [{1}] method [{2}]"
                    .format(self.__module__, WishMe.__name__,
                            self.__init__.__name__))
            raise Exception(wish_exception.error_message_detail(str(e), sys)) from e


    def wishMe(self):
        """This method is used to wish the user.
        returns: None.
        """

        if self.HOUR >= 0 and self.HOUR < 12:
            self.SPEAK.speak(f"Good Morning! its {self.TIME}")
        elif self.HOUR  >= 12 and self.HOUR  < 18:
            self.SPEAK.speak(f"Good Afternoon! its {self.TIME}")
        else:
            self.SPEAK.speak(f"Good Evening! its {self.TIME}")

        self.SPEAK.speak("Hi, I am Neuron Sir. Please tell me how may I help you")









