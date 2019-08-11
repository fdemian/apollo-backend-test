# Morpheus API

Morpheus's REST API.

## How to run 

### Prerequisites

 To run this in your local environment you must install the following dependencies first:

 - Python 3.4+
 - PostgreSQL 9.6
 
### Installation

 Once you've installed all the dependencies follow this steps:

 1) Edit your configuration file and fill in all the reelevant options.
 
 2) Run the application configuration:
   
  ```python
  python3 setup.py 
  ```

 This will create your database, run the migrations and download all necesary python packages. 
  
 3) Run the application 

 ```python
 <python3> main.py
 ```
 
 ## Testing
 
 This application uses pyunit as its test suite.
 To run the tests from the command line use:
 
 ```python
 python -m unittest
 ```