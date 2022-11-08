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
    x = -log(rnd());   // random numbers distributed as exp(-x)
    printf("%10.5f\n",x);
  }

}

double rnd() {
  double r=((double)rand()+1.)/((double)RAND_MAX+2.);
  return r;
}
