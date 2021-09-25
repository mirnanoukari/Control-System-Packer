#include <math.h>
#include "numerical_combined.h"
#include "numerical_coriolis.h"
#include "numerical_inertia.h"
#include "numerical_potential.h"
#include "numerical_momentum.h"
class MechanicalSystem {
  public:
    void numerical_inertia(double, double, double, double , double *);
    void numerical_potential(double, double, double, double, double, double, double, double *);
    void numerical_momentum(double, double, double , double, double, double, double *);
    void numerical_coriolis(double, double, double , double, double, double, double *);
    void numerical_combined(double, double, double, double, double, double, double, double, double, double, double, double *);
};