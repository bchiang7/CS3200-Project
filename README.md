# CS 3200 Final Project
By Brittany Chiang (bchiang7), Isabel Tripp (tahitihat)

Provide a README section for creating and running the project. I need complete specifications for building your project on my computer. Specify all libraries, software, etc. needed to run the application.
Specify expected installation directories. If you use a specific technology for the project, the technology’s download page must be listed.

### Prerequisites
[Python 2.7.13](https://www.python.org/downloads/)

(unfortunately mysql-connector is not backwards compatible with 3.6)

If you already have python 3.6.* installed on your computer, it's probably easiest to download [virtualenv](https://virtualenv.pypa.io/en/stable/) or [pyenv](https://github.com/pyenv/pyenv) to manage python versions.

### Packages
[flask](http://flask.pocoo.org/): `pip install flask`

[pymysql](https://github.com/PyMySQL/PyMySQL): `pip install pymysql`

mysql-connector: `pip install mysql-connector`

### Database Dump
Provide link to database dump file here

### Running the project
Once you have cloned this repository and navigated to the directory in your terminal, simply run
```
python app.py
```
to start the project and navigate to `localhost:5000` in your browser.