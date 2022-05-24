import yaml
import sys
from datetime import datetime
from dateutil.parser import parse
from desktop_exception_layer.exception import GenericException as LoadYamlException

class CommonUtils:
    
    def read_yaml(self,path_to_yaml: str) -> dict:
        """This method is used to read yaml file.
        Args: path_to_yaml: path to yaml file.
        Returns: content: type(__dict__) content of yaml file.
        """
        try:
            with open(path_to_yaml) as yaml_file:
                content = yaml.safe_load(yaml_file)
            # print(f"YAML file: {path_to_yaml} loaded successfully")
            return content
        
        except Exception as e:
            load_yaml_exception = LoadYamlException(
                "Failed during loading yaml file in module [{0}] class [{1}] method [{2}]"
                    .format(self.__module__, CommonUtils.__name__,
                            self.read_yaml.__name__))
            raise Exception(load_yaml_exception.error_message_detail(str(e), sys)) from e
    

    def get_time(self):
        """
        :return current time:
        """
        return datetime.now().strftime("%H:%M:%S").__str__()

    def get_date(self):
        """
        :return current date:
        """
        return datetime.now().date().__str__()


    def get_difference_in_second(self,future_date_time:str,past_date_time:str):
        """
        :param future_date_time:
        :param past_date_time:
        :return difference in second:
        """
        future_date = parse(future_date_time)
        past_date = parse(past_date_time)
        difference = (future_date - past_date)
        total_seconds = difference.total_seconds()
        return total_seconds


    def get_difference_in_milisecond(self,future_date_time:str,past_date_time:str):
        """
        :param future_date_time:
        :param past_date_time:
        :return difference in milisecond:
        """
        total_seconds = self.get_difference_in_second(future_date_time,past_date_time)
        total_milisecond=total_seconds*1000
        return total_milisecond