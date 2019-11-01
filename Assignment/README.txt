# Humanity QA task

This project is written in Pycharm 2018.2 using Python as programing language and his unittest framework

Suggested tools:
* Python version: 3.7
* PyCharm - Python IDE
* WebDriver: ChromeWebDriver

Requirements:

install package:
HTML test runner for reporting
```
pip install html-testRunner
```
and selenium
```
pip install selenium
```

WebDriver:

The ChromeDriver controls the browser using Chrome's automation proxy framework.
The server expects you to have Chrome installed in the default location for each system:

Download ChromeDriver on this [link](https://chromedriver.storage.googleapis.com/index.html) (version I am currently using is 2.41)

Set path of ChromeWebDriver:

For Linux:

1) Move the file to /usr/bin directory - mv ChromeDriver /usr/bin

2) Go to /usr/bin directory and you would need to run something like "chmod a+x ChromeDriver" to mark it executable.

For Windows:

Paste the ChromeDriver.exe file in "C:\Python\Scripts" Folder.

more detail on [ChromeDriver wiki](https://github.com/SeleniumHQ/selenium/wiki/ChromeDriver)

Structure of the project is:

```

└── Assignment
   ├── Locators
   |   └── locators.py
   ├── Pages
   |   └── humanity.py
   ├── Parameters
   |   └── parameters.py
   ├── Tests
   |   ├── Reports
   |   └── Qatask.py
   └── README.txt

```

Here's a brief explanation of the files:
* **parameters.py**: File where parameters used for this test are stored
* **locators**: Place where locators are stored
* **humanity**: Place where our methods are written
* **QAtask**: Python file in which we are combining our methods and making tests
* **Reports**: Place where reports are stored.

To run test cases:
```
1. Open QAtask.py file
2. Right click inside of it and select "Run 'Unittest for QAtask.py'" or open terminal and type "python QAtask.py"
```
