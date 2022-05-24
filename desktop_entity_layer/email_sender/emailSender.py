import sys
import smtplib
from desktop_config_layer.configuration import AssistantConfiguration
from desktop_exception_layer.exception import GenericException as EmailException
from desktop_entity_layer.encryption.encrypt_confidential_data import EncryptData


class EmailSender:

    def __init__(self, password=None):
        try:
            self.config = AssistantConfiguration()
            if password is None:
                self.email_password = EncryptData().decrypt_message(self.config.YOUR_EMAIL_PASS) 
            else:
                self.email_password = password
        except Exception as e:
            email_exception = EmailException(
                "Failed during initializing email configs in module [{0}] class [{1}] method [{2}]"
                    .format(self.__module__, EmailSender.__name__,
                            self.__init__.__name__))
            raise Exception(email_exception.error_message_detail(str(e), sys)) from e
  

    def send_email(self,to, content):
        """This method is used to send email.
        Args: to: reciever email id.
        content: content of email.
        Returns: None.
        """
        try:
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.ehlo()
            server.starttls()
            server.login(self.config.YOUR_EMAIL_ID, self.email_password)
            server.sendmail(self.config.YOUR_EMAIL_ID, to, content)
            server.close()

        except Exception as e:
            email_exception = EmailException(
                "Failed during sending email in module [{0}] class [{1}] method [{2}]"
                    .format(self.__module__, EmailSender.__name__,
                            self.send_email.__name__))
            raise Exception(email_exception.error_message_detail(str(e), sys)) from e

