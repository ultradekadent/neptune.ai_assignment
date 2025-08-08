INTRODUCTION
-------------------------------
The technical basis for the test automation part is Playwright and Pytest (Python).

The solution is comprised of five test cases:
	- test_attr_values_match_expected_data.py
	- test_download_csv.py
	- test_download_png.py
	- test_navigate_tree.py
	- test_search_attribute.py

A 'conftest.py' file containing shared fixtures, and a Page Object Model called 'single_run.py' are also included.

The 'attributes.json' from the 'test_files' folder is needed for 'test_attr_values_match_expected_data.py' to succeed.

The provided config file 'pytest.ini' is used to specify test paths, fixture markers, and nothing else.



DIRECTORY TREE
-------------------------------

neptune.ai_assignment/
├── pages/
│   ├── __init__.py
│   └── single_run.py
├── test_files/
│   └── attributes.json
├── tests/
│   ├── __init__.py
│   ├── conftest.py
│   ├── test_attr_values_match_expected_data.py
│   ├── test_download_csv.py
│   ├── test_download_png.py
│   ├── test_navigate_tree.py
│   └── test_search_attribute.py
├── pytest.ini
├── README.txt
└── requirements.txt


INSTALLATION
-------------------------------

WINDOWS (tested against Win 10 and 11 Home)
	
	1.	Install Python.

		a. Visit the official page for Python https://www.python.org/downloads/ on the Windows operating system. Locate a reliable version of Python 3, preferably 3.13.3, which was used in creating this solution. Choose the correct link for your device from the options provided: either Windows installer (64-bit) or Windows installer (32-bit) and proceed to download the executable file.
	
		b. Once you have downloaded the installer, open the .exe file, such as python-3.13.3-amd64.exe, by double-clicking it to launch the Python installer. 
			
		c. Check 'Add python.exe to PATH'.
			
		c. After Clicking the 'Install Now' button the setup will start installing Python on your Windows system.
			
		d. After completing the setup. Python will be installed on your Windows system. You will see a successful message.
			
		e. Open a command prompt (cmd) and run
			
			python --version
			
		to verify the Python installation in Windows.
			
			
	2.	Install required packages.
			
		a. Unzip 'neptune.ai_assignment.zip'.
			
		b. Right-click on the 'neptune.ai_assignment' directory and select 'Open in Terminal'.
			
		c. Run
				
			pip install -r .\requirements.txt
				
	3. 	Install Playwright browsers
				
			playwright install
					

LINUX (Tested against Ubuntu 24.04)
	
	1.	Untar 'neptune.ai_assignment.tar.gz' and go to the root directory of the project. Then, open a terminal and run
		
			mkdir neptune.ai_assignment
			tar -xvf neptune.ai_assignment.tar.gz -C neptune.ai_assignment/
			cd neptune.ai_assignment/
			
	2.	Install pip for Python 3
			
			sudo apt update
			sudo apt install python3-pip
		
	3.	Install Virtual Environments
	
			sudo apt install virtualenv
	
	4.	Create a new environment
	
			virtualenv neptune_assignment_proj_env
		
	5.	Activate the environment
	
			source neptune_assignment_proj_env/bin/activate
		
			
	6.	Install required packages, ignoring pytest-retry (no matching distribution found for this package)
		
			grep -v 'pytest-retry' requirements.txt | pip install -r /dev/stdin
			
	7.	Install Playwright browsers
	
			playwright install
			playwright install-deps
			playwright install msedge (optional)
	
	

RUNNING THE TESTS
-------------------------------

To execute all tests, run

	pytest -s -k 'attributes'

The -s option is only needed for 'test_download_csv' to display contents of the downloaded CSV file.
	
	
You can execute tests in verbose mode by adding the '-v' option, e.g.

	pytest -v -s -k 'attributes'
	

You can run individual tests by using their pytest decorators metadata (or parts thereof) i.e.:

	- attributes_match_data
    - attributes_navigate_tree
    - attributes_search
    - attributes_download_png
    - attributes_download_csv

For example:

	pytest -k 'match'
	pytest -s -k 'csv'
	pytest -k 'navigate'
    
	

NOTES
-------------------------------

1.	All tests will be executed in headed mode by default. To run them in headless mode, comment out line #15 of the 'conftest.py' file.

2.	All browser interactions (clicks, typing, and navigation) will be significantly slowed down by default, to give you a chance to see what is happening on the screen. To speed things up, comment line #16 of the 'conftest.py' file, or decrease the associated value.
	
3.	Although the framework supports cross-browser testing, all tests will be executed in Chromium by default. This can be changed by modifying the parameter(s) in line #9 of the 'conftest.py' file.
	
The supported browsers are:
	- chromium
	- firefox
	- chrome
	- msedge
	- webkit (safari)
	
4.	The tests appear to be pretty robust, however I have introduced a retry logic, just in case. If a test fails, Pytest will re-execute it 3 times with 5-second intervals.

GOOD LUCK!
