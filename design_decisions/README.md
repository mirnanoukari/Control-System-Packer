# Design Decisions

A documentation for various Control System Packer project design decisions for public reference.

## Design Patterns

### 	Adapter Pattern

In this simple project, we could only see one pattern that can fit for it. We have one mechanical system class in python, using Sympy Codegen the python class (and the entire python code) is the adapter that generates a C++ mechanical system class.

![pattern](https://drive.google.com/uc?export=view&id=1tT0nPSWq07iyYftKuTsJAVE8i_pI782d)

## UML diagrams
### Views

![views](https://drive.google.com/uc?export=view&id=1McffMzsr15ay7Oef5M6L28VvHuLf_vFA)

### Class diagram

The following is a generated class diagram from our python MechanicalSystem class. It shows all the parameters needed for calculations to get desired control.

![class](https://drive.google.com/uc?export=view&id=1WfqgLHuwCF4okHD4LZZKSLPWPAh1b_Oa)

## Contribution

1. Create a pull request by filling out the [template](https://github.com/mirnanoukari/Control-System-Packer/blob/main/Design_decisions/TEMPLATE.md) and saving it under a unique name.
2. Document for and against arguments.
3. Document the decision.
4. Merge pull request.



