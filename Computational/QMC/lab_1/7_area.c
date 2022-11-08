#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <math.h>

double rnd();

int main () {
  int i,n;
  double x,y;

  srand((unsigned)time(NULL));

  n=2000;
  for (i=0; i<n ; i++) {
    x=-1.0+2.0*rnd();       // sample the uniform distribution in the square
    y=-1.0+2.0*rnd();       //
    if(pow(x,2)+pow(y,2)<1.0){printf("%d\n",1);} // f(x,y)=1 in the circle
    else{printf("%d\n",0);}                      // f(x,y)=0 out
  }

}

double rnd() {
  double r=((double)rand()+1.)/((double)RAND_MAX+2.);
  return r;
}
