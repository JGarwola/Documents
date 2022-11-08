#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <math.h>

double rnd();

int main () {
  int i,n;
  double x,y,k;

  srand((unsigned)time(NULL));

  n=1000000;
  k=-0.7;
  y=1.0/(1.0+k);
  for (i=0; i<n ; i++) {
    x=pow(rnd(),y); // sample the distribution pi(x)=0.3*pow(x,-0.7)
    printf("%f %f\n",x,pow(x,-0.1)); // f(x) is the remaining factor pow(x,-0.1)
  }
}

double rnd() {
  double r=((double)rand()+1.)/((double)RAND_MAX+2.);
  return r;
}
