# Planet_Orbital_Motion_Simualtion
[![Pull-Request-Action](https://github.com/pmorande27/Planet_Orbital_Motion_Simualtion/actions/workflows/workfon_pull_request.yml/badge.svg?branch=master)](https://github.com/pmorande27/Planet_Orbital_Motion_Simualtion/actions/workflows/workfon_pull_request.yml)
[![codecov](https://codecov.io/gh/pmorande27/Planet_Orbital_Motion_Simualtion/branch/master/graph/badge.svg?token=8OBGZHK5RM)](https://codecov.io/gh/pmorande27/Planet_Orbital_Motion_Simualtion)
[![CodeFactor](https://www.codefactor.io/repository/github/pmorande27/planet_orbital_motion_simualtion/badge?s=03f8a45c87cfeeedf14c40144c54351a01c8c765)](https://www.codefactor.io/repository/github/pmorande27/planet_orbital_motion_simualtion)
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
## Introduction
While there exists an analytical solution for the 2-body problem, there is none for the 3-body problem or the N-body problem. This programe simulates the behaviour and the evolutions of the Planets in the Solar System. As no exact solution exists for this problem numerical methods have been used. For the purpose of the animation, the method used it known as the Beeman's Algorithm which is a symplectic integrator (Based on the Hamiltonian).
## Installation
The project was build using `Python 3.9.2`. To install all the dependencies please run `py pip install -r requirements.txt`
## Run
To run the programe use the command `py /src/main.py` in the root directory
## Tests
To run the tests you may run `py -m unittest discover`. This command will run all tests, if you are in linux you might want to use `python` instead of `py`.
Please do not try to run the tests outside the root directory.
To get the coverage I recommend `coverage.py`. To install it use: `pip install coverage` once installed and in the root repository run: `coverage run -m source=../src unittest discover`, to generate the report you can either execute `coverage report -m` or `coverage html` to get the information in the terminal or as html respectively.
