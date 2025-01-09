# Web Automation Tool

A web-based automation tool for managing network devices and jumpbox connections.

## Table of Contents

* [Introduction](#introduction)
* [Features](#features)
* [Requirements](#requirements)
* [Installation](#installation)
* [Usage](#usage)
* [Contributing](#contributing)
* [License](#license)

## Introduction

This web automation tool is designed to simplify the process of managing network devices and jumpbox connections. It provides a user-friendly interface for adding, editing, and deleting devices and jumpbox connections, as well as for running automated tasks.

## Features

* User-friendly interface for managing network devices and jumpbox connections
* Support for multiple device types and jumpbox connections
* Automated task execution
* Real-time monitoring and logging
* Secure authentication and authorization

## Requirements

* Python 3.8 or later
* Flask 2.0 or later
* SQLAlchemy 1.4 or later
* Netmiko 3.4 or later
* Flask-Login 0.5 or later
* Flask-WTF 0.14 or later
* Flask-Mail 0.9 or later

## Installation

1. Clone the repository using `git clone https://github.com/Fateeh89/web-automation-tool.git`
2. Install the required dependencies using `pip install -r requirements.txt`
3. Create a new database using `flask db init`
4. Run the application using `python app.py`

## Usage

1. Open a web browser and navigate to `http://localhost:5000`
2. Log in using your username and password
3. Add, edit, or delete devices and jumpbox connections using the user-friendly interface
4. Run automated tasks using the "Run Task" button

## Contributing

Contributions are welcome! If you'd like to contribute to this project, please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License. See the LICENSE file for more information.