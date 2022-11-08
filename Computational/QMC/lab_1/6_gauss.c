#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <math.h>

double rnd();

int main () {
  int i,j,k,n;
  double x;

  srand((unsigned)time(NULL));

  n=200000;
  k=15;
  for (i=0; i<n ; i++) {
    x=0.0;
    for (j=0; j<k; j++) {
      x+=rnd();
    }
    x=(x-0.5*k)*pow(12.0/k,0.5);
    printf("%10.5f\n",x); // exp(-0.5*pow(x,2))/pow(2*pi,0.5) (CLT)
  }

}

double rnd() {
  double r=((double)rand()+1.)/((double)RAND_MAX+2.);
  return r;
}
