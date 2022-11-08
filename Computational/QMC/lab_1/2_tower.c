#include <stdio.h>
#include <stdlib.h>
#include <time.h>

double rnd();

int main () {
  int i,j,n;
  double x,p[6],c[6];

  srand((unsigned)time(NULL));

  n=2000;
  p[0]=0.0;
  for (i=1; i<6; i++) { p[i]=p[i-1]+rnd();}
  for (i=1; i<6; i++) { p[i]=p[i]/p[5];}

  for (i=1; i<6; i++) { c[i]=0.0;}
  for (i=0; i<n; i++) {
    x = rnd();
    j = 1;
    while (p[j]<x) { j++; }
    c[j]++;
  }

  for (i=1; i<6; i++) {printf("%f %f\n",p[i]-p[i-1],c[i]/n);}

}

double rnd() {
  double r=((double)rand()+1.)/((double)RAND_MAX+2.);
  return r;
}
