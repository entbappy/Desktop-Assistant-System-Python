'''
Author: BOKTIAR AHMED BAPPY
Designation: Data Scientist
Date: 14/04/1022
Email: 1. boktiar@ineuron.ai  2. entbappy73@gmail.com
'''


import uuid
import sys
from datetime import datetime
from desktop_utils_layer.utils import CommonUtils
from desktop_data_access_layer.mongo_db.mongo_db_atlas import MongoDBOperation
from desktop_exception_layer.exception import GenericException as LogRequestException
from desktop_config_layer.configuration import AssistantConfiguration



class LogRequest:
    def __init__(self,execution_id=None):
        self.configs = AssistantConfiguration()
        self.utils = CommonUtils()
        self.log_database=self.configs.DB_NAME
        self.log_collection_name="requests"
        self.execution_id=execution_id
        self.mongo_db_object = MongoDBOperation()
        self.log_start_date=self.utils.get_date()
        self.log_start_time=self.utils.get_time()


    def get_log_data(self, request_data):
        try:
            log_data = request_data
            return log_data
        except Exception as e:
            log_exception = LogRequestException(
                "Failed during getting log data in module [{0}] class [{1}] method [{2}] -->log detail[{3}]"
                    .format(LogRequest.__module__.__str__(), LogRequest.__name__,
                            self.get_log_data.__name__, request_data))
            raise Exception(log_exception.error_message_detail(str(e), sys)) from e 
      

    def log_start(self,request):
        try:
            self.log_writer_id=str(uuid.uuid4())
            self.now = datetime.now()
            self.date = self.now.date()
            self.current_time = self.now.strftime("%H:%M:%S")
            log_data = {
                'log_start_date':self.log_start_date,
                'log_start_time': self.log_start_time,
                'execution_id': self.execution_id,
                'log_writer_id':self.log_writer_id,
                'request':self.get_log_data(request),
                'log_updated_time':datetime.now()
            }
            self.mongo_db_object.insert_record_in_collection(self.log_database, self.log_collection_name, log_data)
        except Exception as e:
            log_exception = LogRequestException(
                "Failed during starting log in module [{0}] class [{1}] method [{2}] -->log detail[{3}]"
                    .format(LogRequest.__module__.__str__(), LogRequest.__name__,
                            self.log_start.__name__, log_data))
            raise Exception(log_exception.error_message_detail(str(e), sys)) from e


    def log_stop(self,response:dict):
        try:
            self.now = datetime.now()
            self.date = self.now.date()
            self.current_time = self.now.strftime("%H:%M:%S")

            log_stop_date= self.utils.get_date()
            log_stop_time= self.utils.get_time()
            future_date="{} {}".format(log_stop_date,log_stop_time)
            past_date="{} {}".format(self.log_start_date,self.log_start_time)
            log_data = {
                'log_stop_date':log_stop_date,
                'log_stop_time': log_stop_time,
                'log_writer_id': self.log_writer_id,
                'execution_time_milisecond':self.utils.get_difference_in_milisecond(future_date,past_date)

            }
            log_data.update(response)
            query={'execution_id': self.execution_id,}

            self.mongo_db_object.update_record_in_collection(self.log_database, self.log_collection_name, query,log_data)

        except Exception as e:
            log_exception = LogRequestException(
                "Failed during stopping log in module [{0}] class [{1}] method [{2}] -->log detail[{3}]"
                    .format(LogRequest.__module__.__str__(), LogRequest.__name__,
                            self.log_stop.__name__, log_data))
            raise Exception(log_exception.error_message_detail(str(e), sys)) from e

