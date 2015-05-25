#include <stdio.h>
#include <time.h>

#include "generated/matrix_vector.c"

void main()
{
  unsigned long n = MATRIX_VECTOR_N;

  double x[n];
  double y[n]; 

  unsigned long i;
  for (i=0; i<n; i = i+1) 
  {
    x[i] = 0.0;
  }
  x[0] = 1.0;

  clock_t launch = clock();

  for (i=0; i<1000; i=i+1) 
  {
    matrix_vector(x,y);
    matrix_vector(y,x);
  }
    
  clock_t done = clock();
  double diff = (done - launch) / CLOCKS_PER_SEC;

  printf("Time taken: %lf seconds.\n", diff); 

  //for (i=0; i<n; i=i+1) 
  //{
  // printf("%lf \n", x[i]);
  //}
  
  printf("%lf \n", x[0]);
  printf("%lf \n", x[n-1]);   
}


