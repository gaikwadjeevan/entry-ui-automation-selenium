# Automation Entry Test

# Installation

## Installation

- **Programming language**: This project requires 3.12.x of [Python](https://www.python.org/downloads/)
- **IDE**: [Pycharm](https://www.jetbrains.com/)

## Pycharm Setup

1. To set up this project on your local machine, clone it from the GitHub repository.
2. From the command line in the project's root directory, run:
   - `python -m pip install --upgrade pip` to upgrade pip (use `python3` for MacOS).
   - `pip install virtualenv` to install the virtualenv.
   - `virtualenv venv` to create the virtualenv.
   - `venv\Scripts\activate` to active the virtualenv.
   - `pip install -r requirements.txt` to install all packages.
   - Add the Python interpreter corresponds to the virtualenv.

## Required packages
    - selenium=4.16.0
    - pytest~=8.0.2
    - pytest-html
    - pytest-xdist

## Running Tests in Pycharm
- Run `pytest` from the command line to run all tests.
- To see the console logs, user the `-v -s` option.
- To run tests go to the `testCases` dir
- To run the test with chrome use `--browser` option with `chrome`
- To run the test with chrome use `--browser` option with `firefox`
- If not provided `--browser` parameter it will launch by default with `Ie Browser`
- To generate the HTML test reports use `--html` option with `(absolute_path)/reports/report.html`
- Run tests with CLI arguments:

   - `pytest -v -s test_login.py --browser=chrome --html=<absolute_path>/reports/report.html`
   - `pytest -v -s test_login.py --browser=firefox --html=<absolute_path>/reports/report.html`

    
- Getting any issues while generating the reports simply provide the `reports/report.html` file name 
 it will create the report file under `testCases` dir
  