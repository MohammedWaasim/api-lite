# python_framework
Python Pytest Framework


To have a dry run of the framework follow below steps.
1. Clone the repo 
```sh
git clone https://github.com/MohammedWaasim/api-lite.git
```
2. Have following plugin and software installed
```sh
   pip3 install pytest
   pip3 install ddt
   pip3 install allure-pytest
   pip3 install pyyaml
   pip3 install requests
 ```
3. Set up the env by running this command 
```sh
export PYTHONPATH=$PYTHONPATH:.
```
4. Run this line in the project folder 
```sh
pytest tests --alluredir=reports 
```

NOTE: To run skf test run below test.

```shell script
 pytest tests -v -s --alluredir="reports"
```
  To View test reports run below command
```shell script
allure serve reports
```