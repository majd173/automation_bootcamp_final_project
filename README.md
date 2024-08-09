# <p style="color:green;">OrangeHRM Website API and UI Testing Project</p>
## <p style="color:orange;">Overview</p>

## 
This repository contains a set of automated tests for the OrangeHRM website, covering both API and UI testing. The goal of this project is to ensure the reliability and functionality of the OrangeHRM application by verifying its API endpoints and user interface.

### Table of Contents
1. [Overview](#overview)
2. [Prerequisites](#prerequisites)
3. [Installation](#installation)
4. [Configuration](#configuration)
5. [Running Tests](#running-tests)
6. [Test Structure](#test-structure)
7. [Contributing](#contributing)
9. [Contact](#contact)
### Before running the tests, ensure that you have the following installed:
- [Python](https://www.python.org/) for API tests
- [pytest](https://docs.pytest.org/) for running API tests
- [Selenium](https://www.selenium.dev/) for UI test automation
- [requests](https://docs.python-requests.org/) for API requests

### Clone the repository:
* git clone https://github.com/majd173/automation_bootcamp_final_project.git

### Install Dependencies:
* pip install -r requirements.txt
* pip install selenium
* pip install requests
* pip install allure
* pip install pytest

### Configuration
#### UI Tests
* Web Driver Configuration: Ensure you have the appropriate web driver installed (e.g., ChromeDriver for Chrome). Update the webdriver_path in the configuration file located in orange_hrm.json.

* Test Environment: Update the base URL in orange_hrm.json to point to your OrangeHRM instance.

#### API Tests
* Environment Configuration: Update the base_url in the orange_hrm.json file to point to your OrangeHRM API url.

### Running Tests:
#### Go to all_test_runner.py file in the tests folder and open in terminal:
* for regular test runner insert the following command: pytest
* for allure test runner: pytest --alluredir=./results
* for allure test report: allure serve ./results
* for html test report: pytest --html=report.html
* for xml test report: pytest --junitxml=path/to/report.xml

 
### Contributing:
Contributions are welcome! If you have suggestions or improvements, please fork the repository and submit a pull request. For major changes, please open an issue first to discuss what you would like to change.

### Contact
#### For any questions or issues, please contact:

* <p style="color:orange;">Name: Majd bader</p>
* <p style="color:orange;">Email: majdb173@gmail.com</p>
* <p style="color:orange;">GitHub: https://github.com/majd173/automation_bootcamp_final_project</p>


![Version](https://img.shields.io/badge/version-1.0.0-blue)

