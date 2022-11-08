#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main () {
  int i,j,k,n;

  srand((unsigned)time(NULL)); // initialize random sequence

  n=2000;
  for (i=0; i<n ; i++) {
    j=rand();                  // integers distributed in [0,RAND_MAX]
    k=j%21;                    // integers distributed in [0,20]
    printf("%10d %10d\n",k,j);
  }

}
