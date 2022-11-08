#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <math.h>

double rnd();

int main () {
  int i,n;
  double x;

  srand((unsigned)time(NULL));

  n=1000000;
  for (i=0; i<n ; i++) {
    x=rnd();       // sample uniform distribution in (0,1)
    printf("%f %f %f\n",x,pow(x,-0.4),pow(x,-0.8)); // f(x)=pow(x,y)
  }
}

double rnd() {
  double r=((double)rand()+1.)/((double)RAND_MAX+2.);
  return r;
}
