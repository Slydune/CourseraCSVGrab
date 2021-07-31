# CourserCSVScript
This is a script to automate the search and download of a CSV file from the coursera course search engine.

## Table of Contents
* [General info](#general-information)
* [Technologies](#technologies)
* [Setup](#technologies)
* [Examples of Usage](#example-of-usage)

## General Information
The aim of this project is to automate the data collection to feed to a model for learning purposes.


## Technologies
Project is created with:
- Python 3.8
- Selenium

## Setup
To run this script simply download the repo, load it into an IDE of your choice and click run, or run the `CourseaCSVScript.py` file
from your command line using `Python 3.8`, the parameters are as follows `driver, school_name, course_name`.

### Example of Usage

The following example downloads the CSV for Christopher Newport University using the script provided.

```python
driver = webdriver.Chrome("C:/Users/temp/Desktop/chromedriver.exe")
temp = CourseaCSVScript(driver, 'Christopher Newport Universitry')
temp.load_webpage()
temp.search_school()
temp.download()
```

The CSV download will then appear wherever the selenium driver downloads appear.