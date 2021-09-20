# Control System Packer

![alt text](https://i.ibb.co/Ph0x5bG/Untitled.png)

Control System Packer is a lightweight, low-level program to transform energy equations into the compact libraries for control systems. Packer supports Python 🐍 and C++ 💻libraries.  

## Features

- Input the energy equations and get a compact library for the chosen language. 
- Parametrize the system for usage with different parameters
- Get a control system out of robot's physical equations

> Our goal is to make the lives of robotics developers easier, so you
> can just type in the energy equations and obtain ready-to-use libraries.
> You can import them straight away into the robot for the control!

## Tech

Packer now supports 2 types of the language libraries:

- [Python] - Python libraries
- [C++] - C++ libraries

## Getting Started

You can clone the mechanical system from our branch symbolical-dynamics/lib/dir by running the command:

```sh
sudo python3 setup.py develop
```

or you can use your own mechanical/electronical system, after following our user guidelines.

## Development

Want to contribute? Check out our [contribution policy](CONTRIBUTE.md)

## Glossary
Packer - a program that allows you to turn input (energy equations) into compact libraries for various programming languages.

Control system - a system, which provides the desired response by controlling the output.

Header -  a file containing C language declarations and macro definitions to be shared between several source files.

Library - a collection of non-volatile resources used by computer programs for software development.

Energy equations - potential and kinetic energies equations in symbolic format.

Method of Lagrange multipliers - strategy for finding the local maxima and minima of a function subject to equality constraints.


## License

[MIT](https://github.com/mirnanoukari/Control-System-Packer/blob/main/LICENSE) 

**Free Software, Hell Yeah!**


[Python]: <https://www.python.org/>
[C++]: <http://www.cplusplus.org/>
[Packer]: <https://github.com/mirnanoukari/Control-System-Packer>
