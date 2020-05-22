# Software Testing

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT) 
![GitHub repo size](https://img.shields.io/github/repo-size/SpencerOfwiti/software-testing.svg)
![Open Source](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)
[![contributors](https://img.shields.io/github/contributors/SpencerOfwiti/software-testing.svg)](https://github.com/SpencerOfwiti/software-testing/contributors)

Implementation of Test Driven Development in python using pytest and unittest.

## Table of contents
* [Build Status](#build-status)
* [Built With](#built-with)
* [Features](#features)
* [Code Example](#code-example)
* [Prerequisites](#prerequisites)
* [Installation](#installation)
* [Tests](#tests)
* [Contributions](#contributions)
* [Bug / Feature Request](#bug--feature-request)
* [Authors](#authors)
* [License](#license)

## Build Status

[![Build Status](https://travis-ci.com/SpencerOfwiti/software-testing.svg?branch=master)](https://travis-ci.com/SpencerOfwiti/software-testing)

## Built With
* [Python 3.6](https://www.python.org/) - The programming language used.
* [Pytest](https://docs.pytest.org/en/latest/) - The testing framework used.
* [Travis CI](https://travis-ci.com/) - CI-CD tool used.

## Features

- Unit testing
- Intergration testing

## Code Example

```python
class SimpleCalculator:
	def __init__(self):
		pass

	def sum(self, num1, num2):
		if isinstance(num1, int) and isinstance(num2, int):
			return num1 + num2
		return 'ERROR'

	def divide(self, a, b):
		if b == 0:
			raise ZeroDivisionError
		return a / b
```

## Prerequisites

What things you need to install the software and how to install them

* **python 3**

Linux:
```
sudo apt-get install python3.6
```

Windows:

Download from [python.org](https://www.python.org/downloads/windows/) 

Mac OS:
```
brew install python3
```

* **pip**

Linux and Mac OS:
```
pip install -U pip
```

Windows:
```
python -m pip install -U pip
```

## Installation

Clone this repository:
```
git clone https://github.com/SpencerOfwiti/software-testing
```

To set up virtual environment and install dependencies:
```
source setup.sh
```

To run python scripts:
```
python3 calculator/calculator.py
```

## Tests

This system uses pytest to run automated tests.

To run automated tests:
```
pytest
```

## Contributions

To contribute, follow these steps:

1. Fork this repository.
2. Create a branch: `git checkout -b <branch_name>`.
3. Make your changes and commit them: `git commit -m '<commit_message>'`
4. Push to the original branch: `git push origin <project_name>/<location>`
5. Create the pull request.

Alternatively see the GitHub documentation on [creating a pull request](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request).


## Bug / Feature Request

If you find a bug (the website couldn't handle the query and / or gave undesired results), kindly open an issue [here](https://github.com/SpencerOfwiti/software-testing/issues/new) by including your search query and the expected result.

If you'd like to request a new function, feel free to do so by opening an issue [here](https://github.com/SpencerOfwiti/software-testing/issues/new). Please include sample queries and their corresponding results.

## Authors

* **[Spencer Ofwiti](https://github.com/SpencerOfwiti)** - *Initial work* 
    
[![github follow](https://img.shields.io/github/followers/SpencerOfwiti?label=Follow_on_GitHub)](https://github.com/SpencerOfwiti)
[![twitter follow](https://img.shields.io/twitter/follow/SpencerOfwiti?style=social)](https://twitter.com/SpencerOfwiti)

See also the list of [contributors](https://github.com/SpencerOfwiti/software-testing/contributors) who participated in this project.

## License

This project is licensed under the MIT license - see the [LICENSE.md](LICENSE.md) file for details
