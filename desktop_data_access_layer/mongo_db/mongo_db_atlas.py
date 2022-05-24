'''
Author: BOKTIAR AHMED BAPPY
Designation: Data Scientist
Date: 14/04/1022
Email: 1. boktiar@ineuron.ai  2. entbappy73@gmail.com
'''

import pymongo
import sys
from desktop_exception_layer.exception import GenericException as DBException
from desktop_config_layer.configuration import AssistantConfiguration
from desktop_entity_layer.encryption.encrypt_confidential_data import EncryptData



class MongoDBOperation:
    def __init__(self, user_name=None, password=None):
        try:
            self.configs = AssistantConfiguration()
            self.db_name = self.configs.DB_NAME
            self.is_cloud = self.configs.IS_ATLAS

            if user_name is None or password is None:
                self.user_name = EncryptData().decrypt_message(self.configs.ATLAS_CLUSTER_USERNAME)
                self.password = EncryptData().decrypt_message(self.configs.ATLAS_CLUSTER_PASSWORD)
                
            else:
                self.user_name = user_name
                self.password = password
           
        except Exception as e:
            db_exception = DBException(
                "Failed during setting up MongoDB operation in module [{0}] class [{1}] method [{2}]"
                    .format(self.__module__, MongoDBOperation.__name__,
                            self.__init__.__name__))
            raise Exception(db_exception.error_message_detail(str(e), sys)) from e

    
    def get_mongo_db_url(self):
        """This method is used to get mongo db url.
        Args: None.
        Returns: mongo db url.
        """
        try:
            if self.is_cloud == 1:
                #Change the url to your Atlas Cluster URL
                #Demo: mongodb+srv://<username>:<password>@<cluster-name>.mongodb.net/test?retryWrites=true&w=majority
                url = f"mongodb+srv://{self.user_name}:{self.password}@cluster1.js9v5.mongodb.net/{self.db_name}?retryWrites=true&w=majority"
                return url
            else:
                #This is the default url for local mongo db
                url = "mongodb://localhost:27017/"
                return url

        except Exception as e:
            db_exception = DBException(
                "Failed during getting MongoDB url in module [{0}] class [{1}] method [{2}]"
                    .format(self.__module__, MongoDBOperation.__name__,
                            self.get_mongo_db_url.__name__))
            raise Exception(db_exception.error_message_detail(str(e), sys)) from e


    
    def get_database_client_object(self):
        """This method is used to get database client object.
        Args: None.
        Returns: database client object.
        """
        try:
            client = pymongo.MongoClient(self.get_mongo_db_url())
            return client
                                          
        except Exception as e:
            db_exception = DBException(
                "Failed during getting mongoDB client object in module [{0}] class [{1}] method [{2}]"
                    .format(self.__module__, MongoDBOperation.__name__,
                            self.get_database_client_object.__name__))
            raise Exception(db_exception.error_message_detail(str(e), sys)) from e


    
    def close_database_client_object(self, obj_name):
        """This method is used to close database client object.
        Args: None.
        Returns: None.
        """
        try:
            obj_name.close()
            return True
        except Exception as e:
            db_exception = DBException(
                "Failed during closing mongoDB client object in module [{0}] class [{1}] method [{2}]"
                    .format(self.__module__, MongoDBOperation.__name__,
                            self.close_database_client_object.__name__))
            raise Exception(db_exception.error_message_detail(str(e), sys)) from e


    
    def is_database_present(self, client, db_name):
        """This method is used to check if database is present.
        Args: None.
        Returns: True if database is present else False.
        """
        try:
            if db_name in client.list_database_names():
                return True
            else:
                return False
        except Exception as e:
            db_exception = DBException(
                "Failed during checking database present in module [{0}] class [{1}] method [{2}]"
                    .format(self.__module__, MongoDBOperation.__name__,
                            self.is_database_present.__name__))
            raise Exception(db_exception.error_message_detail(str(e), sys)) from e


    
    def create_database(self, client, db_name):
        """This method is used to create database.
        Args: None.
        Returns: True if database is created else False.
        """
        try:
            return client[db_name]
        except Exception as e:
            db_exception = DBException(
                "Failed during creating database in module [{0}] class [{1}] method [{2}]"
                    .format(self.__module__, MongoDBOperation.__name__,
                            self.create_database.__name__))
            raise Exception(db_exception.error_message_detail(str(e), sys)) from e


    
    def create_collection_in_database(self, database, collection_name):
        """This method is used to create collection in database.
        Args: None.
        Returns: True if collection is created else False.
        """
        try:
            return database[collection_name]
        except Exception as e:
            db_exception = DBException(
                "Failed during creating collection in database in module [{0}] class [{1}] method [{2}]"
                    .format(self.__module__, MongoDBOperation.__name__,
                            self.create_collection_in_database.__name__))
            raise Exception(db_exception.error_message_detail(str(e), sys)) from e


    
    def is_collection_present(self, collection_name, database):
        """This method is used to check if collection is present.
        Args: None.
        Returns: True if collection is present else False.
        """
        try:
            collection_list = database.list_collection_names()

            if collection_name in collection_list:
                return True
            return False
        except Exception as e:
            db_exception = DBException(
                "Failed during checking collection present in database in module [{0}] class [{1}] method [{2}]"
                    .format(self.__module__, MongoDBOperation.__name__,
                            self.is_collection_present.__name__))
            raise Exception(db_exception.error_message_detail(str(e), sys)) from e

    

    def insert_one_record(self, collection, data):
        """This method is used to insert one record in collection.
        Args: None.
        Returns: True if record is inserted else False.
        """
        try:
            collection.insert_one(data)  
            return True
        except Exception as e:
            db_exception = DBException(
                "Failed during inserting one record in collection in module [{0}] class [{1}] method [{2}]"
                    .format(self.__module__, MongoDBOperation.__name__,
                            self.insert_one_record.__name__))
            raise Exception(db_exception.error_message_detail(str(e), sys)) from e

    

    def insert_many_record(self, collection, data):
        """This method is used to insert many record in collection.
        Args: None.
        Returns: True if record is inserted else False.
        """
        try:
            collection.insert_many(data)  
            return True
        except Exception as e:
            db_exception = DBException(
                "Failed during inserting many record in collection in module [{0}] class [{1}] method [{2}]"
                    .format(self.__module__, MongoDBOperation.__name__,
                            self.insert_many_record.__name__))
            raise Exception(db_exception.error_message_detail(str(e), sys)) from e



    def create_collection_in_database(self, database, collection_name):
        """This method is used to create collection in database.
        Args: None.
        Returns: True if collection is created else False.
        """
        try:
            return database[collection_name]
        except Exception as e:
            db_exception = DBException(
                "Failed during creating collection in database in module [{0}] class [{1}] method [{2}]"
                    .format(self.__module__, MongoDBOperation.__name__,
                            self.create_collection_in_database.__name__))
            raise Exception(db_exception.error_message_detail(str(e), sys)) from e



    def get_collection(self, collection_name, database):
        """This method is used to get collection.
        Args: None.
        Returns: collection object.
        """
        try:
            collection = self.create_collection_in_database(database, collection_name)
            return collection
        except Exception as e:
            db_exception = DBException(
                "Failed during getting collection in module [{0}] class [{1}] method [{2}]"
                    .format(self.__module__, MongoDBOperation.__name__,
                            self.get_collection.__name__))
            raise Exception(db_exception.error_message_detail(str(e), sys)) from e


    
    def is_record_present(self, db_name, collection_name, record):
        """This method is used to check if record is present.
        Args: None.
        Returns: True if record is present else False.
        """
        try:
            client = self.get_database_client_object()  # client object
            database = self.create_database(client, db_name)  # database object
            collection = self.get_collection(collection_name, database)  # collection object
            record_found = collection.find(record)  # fetching record
            if len(list(record_found)) > 0:
                client.close()
                return True
            else:
                client.close()
                return False
        except Exception as e:
            db_exception = DBException(
                "Failed during checking record present in module [{0}] class [{1}] method [{2}]"
                    .format(self.__module__, MongoDBOperation.__name__,
                            self.is_record_present.__name__))
            raise Exception(db_exception.error_message_detail(str(e), sys)) from e

    
    def create_record(self, collection, data):
        """This method is used to create record.
        Args: None.
        Returns: True if record is created else False.
        """
        try:
            collection.insert_one(data)  
            return 1
        except Exception as e:
            db_exception = DBException(
                "Failed during creating record in module [{0}] class [{1}] method [{2}]"
                    .format(self.__module__, MongoDBOperation.__name__,
                            self.create_record.__name__))
            raise Exception(db_exception.error_message_detail(str(e), sys)) from e



    def insert_record_in_collection(self, db_name, collection_name, record):
        """This method is used to insert record in collection.
        Args: None.
        Returns: True if record is inserted else False.
        """
        try:
            no_of_row_inserted = 0
            client = self.get_database_client_object()
            database = self.create_database(client, db_name)
            collection = self.get_collection(collection_name, database)
            if not self.is_record_present(db_name, collection_name, record):
                no_of_row_inserted = self.create_record(collection=collection, data=record)
            client.close()
            return no_of_row_inserted

        except Exception as e:
            db_exception = DBException(
                "Failed during inserting record in collection in module [{0}] class [{1}] method [{2}]"
                    .format(self.__module__, MongoDBOperation.__name__,
                            self.insert_record_in_collection.__name__))
            raise Exception(db_exception.error_message_detail(str(e), sys)) from e 


    
    def update_record_in_collection(self, database_name, collection_name, query, new_value):
        """This method is used to update record in collection.
        Args: None.
        Returns: True if record is updated else False.
        """
        try:
            client = self.get_database_client_object()
            database = self.create_database(client, database_name)
            collection = self.get_collection(collection_name=collection_name, database=database)
            update_query = {'$set': new_value}
            collection.update_one(query, update_query)
            client.close()
    
        except Exception as e:
            db_exception = DBException(
                "Failed during updating record in collection in module [{0}] class [{1}] method [{2}]"
                    .format(self.__module__, MongoDBOperation.__name__,
                            self.update_record_in_collection.__name__))
            raise Exception(db_exception.error_message_detail(str(e), sys)) from e






    
