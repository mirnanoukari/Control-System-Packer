# Design Decisions

A documentation for various Control System Packer project design decisions for public reference.

## Design Patterns

### 	Adapter Pattern

In this simple project, we could only see one pattern that can fit for it. We have one mechanical system class in Python, using Sympy Codegen the python class (and the entire python code) is the adapter that generates a C++ mechanical system class.

![pattern](https://drive.google.com/uc?export=view&id=1tT0nPSWq07iyYftKuTsJAVE8i_pI782d)

## SOLID Principles
For this project, since the goal is more or less a simple stream-lined process, we have decided to not follow all SOLID principles.

Namely, the main class of the project contains all the functions for convenience, and can be easily modified at any stage of execution.
Meaning it violates Single Responsibility and Open/Close principles.

This is done because the project itself is a convenience tool for robotics, mechanics programmers and other - people working with control systems in coding.
We leave the opportunity to the User to modify the variables according to their problem.

Instead of focusing on perfect OOP, we use this class as a collection of methods, that the User can easily import into their program.

## UML diagrams
### Views

![views](https://drive.google.com/uc?export=view&id=1McffMzsr15ay7Oef5M6L28VvHuLf_vFA)
The Allocation View is missing because it makes little sense for this project. Since this is a piece of software, we do not bother with managing of hardware and resources.
### Class diagram

The following is a generated class diagram from our Python MechanicalSystem class. 
It shows all the parameters needed for calculations to get desired control and generate C headers. If you want to know what exactly each parameter stands for, check our code in lib/symbolical_dynamics/euler_lagrange.py

Our project is simple, it does not rely on OOP principles, but rather uses the class as a collection of methods, that a programmer can use.

![class](https://drive.google.com/uc?export=view&id=1WfqgLHuwCF4okHD4LZZKSLPWPAh1b_Oa)

## Contribution

1. Create a pull request by filling out the [template](https://github.com/mirnanoukari/Control-System-Packer/blob/main/Design_decisions/TEMPLATE.md) and saving it under a unique name.
2. Document for and against arguments.
3. Document the decision.
4. Merge pull request.



