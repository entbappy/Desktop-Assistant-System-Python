#!/bin/bash

echo [$(date)] : "STARTING INITIAL SETUP"
export _VERSION_=3.7

echo [$(date)] : "PROJECT DIRECTORY NAME"
read project_name
export project_name_=$project_name

echo [$(date)] : "CREATE API LAYER Y OR N"
read api_layer

echo [$(date)] : "CREATING PROJECT STRUCTURE"

echo [$(date)] : "CREATING CONFIGURATION LAYER"
mkdir ${project_name_}_config_layer
touch ${project_name_}_config_layer/__init__.py ${project_name_}_config_layer/configuration.py

echo [$(date)] : "CREATING UTILITY LAYER"
mkdir ${project_name_}_utils_layer
touch ${project_name_}_utils_layer/__init__.py ${project_name_}_utils_layer/utils.py

echo [$(date)] : "CREATING LOGGING LAYER"
mkdir ${project_name_}_logging_layer
touch ${project_name_}_logging_layer/__init__.py ${project_name_}_logging_layer/logging.py

echo [$(date)] : "CREATING BUSINESS_LOGIC LAYER"
mkdir ${project_name_}_business_logic_layer
touch ${project_name_}_business_logic_layer/__init__.py ${project_name_}_business_logic_layer/business_logic.py

echo [$(date)] : "CREATING DATA ACCESS LAYER"
mkdir ${project_name_}_data_access_layer
touch ${project_name_}_data_access_layer/__init__.py ${project_name_}_data_access_layer/data_access.py

echo [$(date)] : "CREATING EXCEPTION LAYER"
mkdir ${project_name_}_exception_layer
touch ${project_name_}_exception_layer/__init__.py ${project_name_}_exception_layer/exception.py

echo [$(date)] : "CREATING ENTITY LAYER"
mkdir ${project_name_}_entity_layer
touch ${project_name_}_entity_layer/__init__.py ${project_name_}_entity_layer/entity.py

echo [$(date)] : "CREATING TESTING LAYER"
mkdir ${project_name_}_testing
touch ${project_name_}_testing/__init__.py ${project_name_}_testing/tests.py

if [[ $api_layer -eq "Y" ]];
then
   echo [$(date)] : "CREATING API LAYER"
   mkdir ${project_name_}_api_layer
   touch ${project_name_}_api_layer/__init__.py ${project_name_}_api_layer/endpoints.py
else
   echo [$(date)] : "CREATING UI LAYER"
   mkdir ${project_name_}_ui_layer
   touch ${project_name_}_ui_layer/__init__.py ${project_name_}_ui_layer/static.py ${project_name_}_ui_layer/templates.py
fi

echo [$(date)] : "CREATING CONDA ENVIRONMENT"
conda create --prefix ./env python=${_VERSION_} -y
source activate ./env

echo [$(date)] : "CREATE REQUIREMENTS TEXT FILE"
touch requirements.txt

echo [$(date)]: "CREATING DOCKER FILE"
touch dockerfile

echo [$(date)]: "CREATING ADDITIONAL FILES"
touch setup.py
touch config.yaml

echo [$(date)] : "END"