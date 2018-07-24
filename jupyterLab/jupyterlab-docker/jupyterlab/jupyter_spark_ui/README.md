# Jupyter Server Extension Spark UI

 Allows a Jupyter Notebook user to access the spark UI from the notebook server itself by pointing the browser to <notebook-server-base-url>/spark/<port>, where <port> is the port where the Spark UI is listening.

 ## Requirements

  - `Python 3.5.2`

 ### Python dependencies

 To run this test, install:

 ```
 pip3 install pytest>=2.8 notebook bs4
 ```

 ## Testing (UT / IT)

 ### Execution with [pytest](http://doc.pytest.org/en/latest/)

 All tests are implemented using `unittest`. To launch tests we use `pytest`.


 To launch all tests in this module, use:

 ```
 # If you are in the module root
 PYTHONPATH=./src/main/jupyter_spark_ui pytest -v src/main/jupyter_spark_ui
 ```

 __WARNING__: It is necessary to set `PYTHONPATH` because `pytest` does not
 include the current directory by default in the `PYTHONPATH`.

 ### Execution with [Maven](https://maven.apache.org/)

 Test execution is integrated with _Maven_: `mvn test`
