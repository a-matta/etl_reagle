# etl_reagle

This repository contains the unit tests for ETL assignment for Realge Oy.

This task is designed to evaluate your approach to testing a simple Extract-Transform-Load (ETL) data pipeline.

---

*Documentation**: [https://a-matta.github.io/etl_reagle](https://a-matta.github.io/etl_reagle)

**Source Code**: [https://github.com/a-matta/etl_reagle](https://github.com/a-matta/etl_reagle)

---

## Development

* Requirements:
  * [Poetry](https://python-poetry.org/)
  * Python 3.12+
  * [Install Allure Report](https://allurereport.org/docs/install/)
* Clone this repository
* Create a virtual environment and activate it
  ```sh
  poetry shell
  ```
* Install the dependencies
  ```sh
  poetry install
  ```
* Running the tests
  ```sh
  # Uses PyInvoke
  inv tests
  ```
* To view the allure reports.
  ```sh
  allure serve allure-results
  ```

---

This project was generated using the [playwright-python-cookiecutter](https://github.com/a-matta/playwright-python-cookiecutter) template.
