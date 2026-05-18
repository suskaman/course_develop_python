# About the project "widget for bank"
## Description:
Project "widget for bank" - this is a feature for personal account of clients in bank application. 
It is a widget which show anything the last successful bank operations of the client.

## Installation:
1. Clone the repository:

```
git clone https://github.com/suskaman/course_develop_python.git
```

2. Install requirements:

```
pip install -r requirements.txt
```
3. Change git remote url to avoid accidental pushes to base project:
```
git remote set-url origin github_username/repo_name
git remote -v # confirm the changes
```
## Usage example
This application is under developing

## logging
The project write a logs into directory 'logs'.
* The default log level is DEBUG for all of them.
* Format for console: [YYYY-MM-DD HH:mm:ss] | levelname | funcName | name | message
* Format for file: [YYYY-MM-DD HH:mm:ss] | levelname | name | filename:lineno | funcName | message


## Testing of a modules
All code of this project are testing on the package **'tests'**.
Module **conftest.py** has a fixtures for test modules.

* There are tests for the module **'masks.py'** in the module **'test_masks.py'**.
A correct work of functions **'get_mask_card_number'** and **'get_mask_account'** checks with **'pytest.parametrize'**.
For more information look at the **tests/test_masks.py**


* There are tests for the module **'processing.py'** in the module **'test_processing.py'**.
A correct work of functions **'filter_by_state'** and **'sort_by_date'** checks with **'pytest.fixture'**.
For more information look at the **tests/test_processing.py**


* There are tests for the module **'widget.py'** in the module **'test_widget.py'**.
A correct work of the function **'mask_account_card'** checks with **'pytest.parametrize'**
A correct work of the function **'get_date'** checks with **'pytest.fixture'**
For more information look at the **tests/test_widget.py**


* There are tests for the module **'generators.py'** in the module **'test_generators.py'**.
A correct work of functions **'filter_by_currency'** and **'transaction_descriptions'**
and **'card_number_generator'** checks with **'pytest.fixture'**.
For more information look at the **tests/test_generators.py**


* There are tests for the module **'decorators.py'** in the module **'test_decorators.py'**.
A correct work of the decorator **'log'** checks with built-in fixture **capsys**.
For more information look at the **tests/test_decorators.py**


* There are tests for the module **'data_loader.py'** in the module **'test_data_loader.py'**.
A correct work of functions **'get_data_from_csv'** and **'get_data_from_excel'** checks with mock and patch.
For more information look at the **tests/test_data_loader.py**


* There are tests for the module **'external_api.py'** in the module **'test_external_api.py'**.
A correct work of the function **'get_amount_from_transaction'** checks with mock and patch.
For more information look at the **tests/test_external_api.py**


* There are tests for the module **'utils.py'** in the module **'test_utils.py'**.
A correct work of the function **'get_transactions'** checks with mock and patch.
For more information look at the **tests/test_utils.py**


**For start tests use this command in the terminal**:
```
pytest tests
```

## License
Distributed under the Unlicense License. See LICENSE.txt for more information