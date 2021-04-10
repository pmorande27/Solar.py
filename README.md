[![build](https://github.com/pmorande27/Solar.py/actions/workflows/build_action.yml/badge.svg?branch=master)](https://github.com/pmorande27/Solar.py/actions/workflows/build_action.yml)
[![codecov](https://codecov.io/gh/pmorande27/Planet_Orbital_Motion_Simualtion/branch/master/graph/badge.svg?token=8OBGZHK5RM)](https://codecov.io/gh/pmorande27/Planet_Orbital_Motion_Simualtion)
[![CodeFactor](https://www.codefactor.io/repository/github/pmorande27/solar.py/badge)](https://www.codefactor.io/repository/github/pmorande27/solar.py)
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
## Introduction
While there exists an analytical solution for the 2-body problem, there is none for the 3-body problem or the N-body problem. This programe simulates the behaviour and the evolutions of the Planets in the Solar System. As no exact solution exists for this problem numerical methods have been used. For the purpose of the animation, the method used it known as the Beeman's Algorithm which is a symplectic integrator (Based on the Hamiltonian).
## Installation
The project was build using `Python 3.9.2`. To install all the dependencies please run `py pip install -r requirement.txt`
## Run
To run the programe use the command `py ./src/main.py` in the root directory. I would not recommend running the program in any other way as the imports use sys and they will probably fail if done otherwise.
## Tests
To run the tests you may run `py -m unittest discover`. This command will run all tests, if you are in linux you might want to use `python` instead of `py`.
Please do not try to run the tests outside the root directory.
To get the coverage I recommend `coverage.py`. To install it use: `pip install coverage` once installed and in the root repository run: `coverage run -m source=./src unittest discover`, to generate the report you can either execute `coverage report -m` or `coverage html` to get the information in the terminal or as html respectively
## Program
By default the main.py file will run the animation with the probe apprahing Mars, other options that display data have been commented out, feel free to un-comment it to look at the data.
<br/>
The animation might appear to be stpped at the beginning and when the satellite approaches Mars, this is on purpose as a variable time-step has been implemented, when the probe is near a body it will automatically lower the time step to capture the correct behaviour of the probe.
<br/>
Do not add another star type body to the simulation or Probe as they will cause a division by zero. Feel free to add any planet that you want from the Solar system. you can use the funtion in writer class or add it by hand. If doing the latter please follow the given json format
