// sampling a gaussian with the metropolis method
//
//           \pi(x)=(2\beta\pi)^{1/2} exp(-2\beta x^2)
//
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <math.h>

double rnd();

int main () {
  int i,n;
  double x,xp,acc,p,delta,beta,lnpi,lnpip;

  n=200000;   // number of monte carlo steps
  beta=0.3;   // variational parameter
  delta=5.0;  // size of the move
  x=10.0;     // initial position

  srand((unsigned)time(NULL));

  lnpi=-2*beta*pow(x,2);




  for (i=0; i<n ; i++) {
    xp=x+delta*(rnd()-0.5);
    lnpip=-2*beta*pow(xp,2.0);
    p=exp(lnpip-lnpi);
    if(p>rnd()){
      acc=1;
      x=xp;
      lnpi=lnpip;



    }
    else{
      acc=0;
    }
    printf("%f %f\n",x,acc);
  }
}

double rnd() {
  double r=((double)rand()+1.)/((double)RAND_MAX+2.);
  return r;
}
