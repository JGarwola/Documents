// harmonic oscillator with the metropolis method
//
//           h = -1/2 \nabla^2 + 1/2 x^2, psi=exp(-\beta x^2)
//
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <math.h>

double rnd();

int main () {
  int i,n;
  double x,xp,acc,p,delta,beta,lnpsi,lnpsip,ekin,epot,etot;

  n=20000;    // number of mnte carlo steps
  beta=0.5;   // variational parameter
  delta=5.0;  // size of the move
  x=10.0;     // initial position

  srand((unsigned)time(NULL));

  lnpsi=-beta*pow(x,2);
  ekin=-0.5*(pow(2*beta*x,2)-2*beta);
  epot=+0.5*pow(x,2);
  etot=ekin+epot;

  for (i=0; i<n ; i++) {
    xp=x+delta*(rnd()-0.5);
    lnpsip=-beta*pow(xp,2.0);
    p=exp(2*(lnpsip-lnpsi));
    if(p>rnd()){
      acc=1;
      x=xp;
      lnpsi=lnpsip;
      ekin=-0.5*(pow(2*beta*x,2)-2*beta);
      epot=+0.5*pow(x,2);
      etot=ekin+epot;
    }
    else{
      acc=0;
    }
    printf("%f %f %f %f %f\n",x,ekin,epot,etot,acc);
  }
}

double rnd() {
  double r=((double)rand()+1.)/((double)RAND_MAX+2.);
  return r;
}
