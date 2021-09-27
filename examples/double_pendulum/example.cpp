#include "euler_lagrange.cpp"
#include <iostream>
using namespace std;
int main() {
  MechanicalSystem myObj;  // Create an object of MyClass
  double* data = new double[2];
  // Access attributes and set values
  numerical_combined(2,3,4,5,6,7,8,9,0,12,21,data);
  cout << data[0];
  // Print values
  return 0;
}
