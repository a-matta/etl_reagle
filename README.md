# etl_reagle

This repository contains the unit tests for ETL assignment for Realge.

This task is designed to evaluate your approach to testing a simple Extract-Transform-Load (ETL) data pipeline.

## Requirements:

* python3.10 or later
* SQLite3
* [Poetry](https://python-poetry.org/)
* [Install Allure Report](https://allurereport.org/docs/install/)

## How to Get Started

1. Clone this repository 
1. Create a virtual environment and activate it
   ```sh
   poetry shell
   ```
1. Install the dependencies
   ```sh
   poetry install
   ```
1. Initialize the Database and run the ETL
   ```sh
   python main.py --method init
   ```
1. Run pipeline to fetch open job applications load them into a local SQLite database 
   ```sh
   python main.py
   ```
1. Running the tests
   ```sh
   # Uses PyInvoke
   inv tests
   ```
1. To view allure reports.
   ```sh
   allure serve allure-results
   ```

---

This project was generated using the [playwright-python-cookiecutter](https://github.com/a-matta/playwright-python-cookiecutter) template.
