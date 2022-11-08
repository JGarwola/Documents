#include <stdio.h>
#include <stdlib.h>
#include <time.h>

double rnd();

int main () {
  int i,n;
  double x,a,b,y;

//printf("%d\n\n",RAND_MAX);

  srand((unsigned)time(NULL));

  n=2000;
  a=3.5;
  b=5.3;
  for (i=0; i<n ; i++) {
    x = rnd();         // random numbers uniformly distributed in (0,1)
    y=a+(b-a)*x;       // random numbers uniformly distributed in (a,b)
    printf("%10.5f %10.5f\n",x,y);
  }

}

double rnd() {
  double r=((double)rand()+1.)/((double)RAND_MAX+2.);
  return r;
}
