# LLM-DATA-MINER

## Purpose and scope

Project was designed to mine data from large volume
of data files to extract information which is needed.

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


