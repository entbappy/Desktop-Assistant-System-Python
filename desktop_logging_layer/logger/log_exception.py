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
from desktop_exception_layer.exception import GenericException as LogException
from desktop_config_layer.configuration import AssistantConfiguration


class LogExceptionDetail:
    def __init__(self, execution_id):
        self.configs = AssistantConfiguration()
        self.utils = CommonUtils()
        self.log_database=self.configs.DB_NAME
        self.log_collection_name="exception"
        self.execution_id=execution_id
        self.mongo_db_object=MongoDBOperation()

    def log(self,  log_message):
        try:
            self.log_writer_id=str(uuid.uuid4())
            self.now = datetime.now()
            self.date = self.now.date()
            self.current_time = self.now.strftime("%H:%M:%S")
            log_data = {
                'log_updated_date': self.utils.get_date(),
                'log_update_time': self.utils.get_time(),
                'execution_id': self.execution_id,
                'message':log_message,
                'log_writer_id':self.log_writer_id
            }
            self.mongo_db_object.insert_record_in_collection(self.log_database, self.log_collection_name, log_data)
        except Exception as e:
            log_exception = LogException(
                "Failed during logging exception in database in module [{0}] class [{1}] method [{2}] -->log detail[{3}]"
                    .format(LogExceptionDetail.__module__.__str__(), LogExceptionDetail.__name__,
                            self.log.__name__, log_data))
            raise Exception(log_exception.error_message_detail(str(e), sys)) from e