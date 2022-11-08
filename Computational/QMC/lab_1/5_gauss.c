#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <math.h>

double rnd();

int main () {
  int i,n;
  double x;

  srand((unsigned)time(NULL));

  n=2000;
  for (i=0; i<n ; i++) {
    x=cos(3.14159265358979*rnd())*pow(-2.0*log(rnd()),0.5);
    printf("%10.5f\n",x); // exp(-0.5*pow(x,2))/pow(2*pi,0.5) (boxmuller)
  }

}

double rnd() {
  double r=((double)rand()+1.)/((double)RAND_MAX+2.);
  return r;
}
