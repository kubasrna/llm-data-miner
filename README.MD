# LLM Data Miner

## Purpose and scope

Project was designed to mine data from large volume
of data files to extract information which is needed.

## Before running the application for the first time
Since the application runs through console I'd suggest that the user uses virtual environment for installed dependencies. 

To provide venv capability on linux/mac machines use:
```
pip3 install virtualenv 
virtualenv {name of the environment}
source {name of the environment}/bin/activate
```

after that navigate to the root folder of the llm-data-miner project and use following command to install all required dependencies
```
pip install -r requirements.txt
```

After this you should be ready dependencies-wise. Steps to provide model for the app are:

1. Next step is download .gguf format of your favourite llm 
1. Place is within models folder within llm-data-miner repo.
1. Go to config folder and open config.yml in your favourite text editor
1. Update <b>MODEL_BIN_PATH</b> so that it matches with name of your model
1. Update <b>MODEL_TYPE</b> so that it matches the type. Supported types can be found [here](https://github.com/marella/ctransformers). 
    1. Mistral can be used as well. Seems like README at the link was not updated. Model type is <i>mistral</i> 

## Current status & bugs
For some reason .doc and .docx require installation of libre office
which I haven't had time to fix. Other than that. .PPTX, .PDF and .XLSX
files are supported for the FAISS space generation and tested through
prompt interaction with the model

## Usage
At this point project can be unfortunatelly used only through
console interaction with models. In data_source_model.py user
can comment and uncomment what source files should be provided to the
model.

When user wants to change the model, currently they have to download the
file and change path and type in config/config.yml

## Future work
develop UI using QT6 so that user can interactively change what 
source files are being used, how to include new models etc.




