# Control System Packer
![alt text](https://i.ibb.co/Ph0x5bG/Untitled.png)


[![Reliability Rating](https://sonarcloud.io/api/project_badges/measure?project=mirnanoukari_Control-System-Packer&metric=reliability_rating)](https://sonarcloud.io/dashboard?id=mirnanoukari_Control-System-Packer)
[![Version](https://img.shields.io/badge/CSPacker-v.%201.0.0-blue)](https://github.com/mirnanoukari/Control-System-Packer/releases/tag/v.1.0.0)
[![Licence](https://img.shields.io/badge/license-MIT-orange)](https://github.com/mirnanoukari/Control-System-Packer/blob/symbolical_dynamics/LICENSE)

Control System Packer is a lightweight, low-level program to transform energy equations into the compact libraries for control systems. Packer supports Python 🐍, C 💻 and C++ 💻libraries.  

## Table of Contents
- [Control System Packer](#control-system-packer)
  * [Features](#features)
  * [Why is our project useful and better than the existing solutions?](#why-is-our-project-useful-and-better-than-the-existing-solutions)
  * [Supported languages](#supported-languages)
  * [Getting Started](#getting-started)
    + [Cloning a repository](#cloning-a-repository)
    + [Installing the package](#installing-the-package)
    + [Importing phase](#importing-phase)
      - [Python](#python)
    + [Initialization of your system](#intialization-of-your-system)
    + [Getting lagrange equations](#getting-lagrange-equations)
      - [C](#c)
      - [C++](#c-1)
  * [Development](#development)
  * [Technical stack](#technical-stack)
  * [Glossary](#glossary)
  * [Further Development](#further-development)
  * [License](#license)

## Features

- Input the energy equations and get a compact library for the chosen language. 
- Parametrize the system for usage with different parameters
- Get a control system out of robot's physical equations

> Our goal is to make the lives of robotics developers easier, so you
> can just type in the energy equations and obtain ready-to-use libraries.
> You can import them straight away into the robot for the control!

![descrip](https://drive.google.com/uc?export=view&id=10ZnH-RKtUVluY_jIP1SGduzLt8r4Uy-2)

## Why is our project useful and better than the existing solutions?
- Our system works with any mechanical model. Every model has it's own general positions and energy equations.
- Most of the programmers used to code and transform these equations manually, there was no popular tool to solve this issue.  
- Complex control tasks are done in high-level PLs (such as Python), but low-level computers usually work this C or C++. We provide fast and easy transition from Python to C or C++.
## Supported languages
Packer now supports 2 types of the language libraries:
- [Python] - Python libraries
- [C++] - C++ libraries
- [C] - C headers

## Getting Started
### Cloning a repository
1.   Open the command line interface
2.   Using the command line, access a folder in which you want your project to be saved 
3.   Type in:    
 ```sh
 git clone https://github.com/mirnanoukari/Control-System-Packer.git
 ```
### Installing the package
You can install the package from our branch symbolical-dynamics/lib/dir by running the command:

```sh
sudo python3 setup.py develop # for Linux
```
```sh
python3 setup.py develop # for Windows
```

### Importing phase
#### Python
Then, you need to import Mechanicalsystem class from euler_lagrange to your mechanical system, use one of our examples in the example folder

```python
from lib.symbolical_dynamics.euler_lagrange import MechanicalSystem
```
### Initialization of your system

```python
name_of_your_system = MechanicalSystem(q,K,P,R)
```
- q (generalized coordinates)
- K (kinetic energy)
- P (potential energy)
- R (rayleigh dissipative function)

Or you can assign values to your mechanical system using set functions:

```python
name_of_your_system = MechanicalSystem(q)
name_of_your_system.set_kinetic_energy(K)
name_of_your_system.set_potential_energy(P)
name_of_your_system.set_rayleigh(R)
```
### Getting lagrange equations
```python
name_of_your_system.get_lagrange_equations(simp=True)
```
The model then produces an equation, and results a combined terms of potential energy and inertia matrix.

Great! Now, your system is initialized with values. You can use them both in Python, C and C++ Below we present the usage of both cases.

```python
print(f'\nEquations of motion:\n{name_of_your_system.Q}')
print(f'\nInertia matrix:\n{name_of_your_system.D}')
print(f'\nGeneralized momenta:\n{name_of_your_system.p}')
```
#### C
First of all, we should generate headers from Python code:
```python
name_of_your_system.get_headers()
```
Now you can simply import these headers, and use built-in functions to find exact value for any numerical arguments:
```c
#include "numerical_combined.h"
#include <stdio.h>
int main(void) {
   result = ... ; // initialize the array to store the result
   numerical_combined(2,3,4,5,6,7,8,9,0,12,21,result);  // Example of usage of generated headers
   printf("%d", result[0])
   return 0;
}
```
#### C++
In your python file, set create_cpp to True and generate an optional cpp class file  (euler_lagrange.cpp) which will include all our headers in it:
```python
numerical_combined.get_headers(create_cpp=True)
```
The file euler_lagrange.cpp will contain ready-to-use functions, and you can import it in your code:
```cpp
#include "euler_lagrange.cpp"
```
#### Python
You can access this C++ library in python using PyBind11. This will automatically add the PyBind code to the cpp file.
```python
name_of_your_system.bind_cpp_file()
```
Afterwards, you will need to run the cpp file. It will create a python module you can import, and it will use the C++ implementation.

Here is a [full tutorial](https://pybind11.readthedocs.io/en/stable/installing.html) on how to install and work with pybind11.
## Development

Want to contribute? Check out our [contribution policy](CONTRIBUTING.md)
## Technical stack
- [Python] 🐍 
- [SymPy] (Python) 🧮
- [PyBind] (Python) 📚
- [Setuptools] (Python) 🔧
- [C] 🖥️
- [C++] 💻
- [Markdown]📃

## Glossary
Packer - a program that allows you to turn input (energy equations) into compact libraries for various programming languages.

Control system - a system, which provides the desired response by controlling the output.

Header -  a file containing C language declarations and macro definitions to be shared between several source files.

Library - a collection of non-volatile resources used by computer programs for software development.

Energy equations - potential and kinetic energies equations in symbolic format.

Method of Lagrange multipliers - strategy for finding the local maxima and minima of a function subject to equality constraints.

## Further Development
At the moment, the development of a reverse conversion to Python is underway, using cython and the PyBind library. It is planned to compare the execution speeds of methods in C ++ and in Python.

## License

[MIT](https://github.com/mirnanoukari/Control-System-Packer/blob/main/LICENSE) 

**Free Software, Hell Yeah!**


[Python]: <https://www.python.org/>
[C++]: <http://www.cplusplus.org/>
[Packer]: <https://github.com/mirnanoukari/Control-System-Packer>
[C]: <https://www.iso.org/standard/74528.html>
[SymPy]: <https://www.sympy.org/en/index.html>
[PyBind]: <https://github.com/pybind/pybind11>
[Setuptools]: <https://pypi.org/project/setuptools/>
[Markdown]: <https://www.markdownguide.org/>
