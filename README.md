# NOTES

To run the tests and generate allure reports, we have to make sure to provide the reports paths
```python 
 pytest -sv --alluredir=reports/allure-reports
```

To generate the allure report:
```python 
allure serve reports/allure-reports 
```