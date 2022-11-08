#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <math.h>

double rnd();

int main () {
  int i,n;
  double x,y,k;

  srand((unsigned)time(NULL));

  n=2000;
  k=3.0;
  y=1.0/(1.0+k);
  for (i=0; i<n ; i++) {
    x=pow(rnd(),y); // random numbers distributed as (k+1)*pow(x,k)
    printf("%10.5f\n",x);
  }

}

double rnd() {
  double r=((double)rand()+1.)/((double)RAND_MAX+2.);
  return r;
}
