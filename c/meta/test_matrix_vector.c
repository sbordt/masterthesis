#include <stdlib.h>
#include <stdio.h>
#include <time.h>
#include <omp.h>

#include "generated/matrix_vector.c"

void main()
{
  unsigned long n = MATRIX_VECTOR_N;

  double *x = malloc(n * sizeof(double));
  double *y = malloc(n * sizeof(double));

  unsigned long i;
  for (i=0; i<n; i = i+1) 
  {
    x[i] = 0.0;
  }
  x[0] = 1.0;

  double start = omp_get_wtime();

  /*for (i=0; i<1000; i=i+1) 
  {
    matrix_vector(x,y);
    matrix_vector(y,x);
  }*/
   
  /*unsigned long nloops = 5;
  unsigned long step = n/nloops;

  for (i=0; i<1000; i=i+1) 
  {
    int j;
    for(j=0;j<nloops;j++) 
    {
      if (j == nloops-1) {
        matrix_vector_partial(x,y,step*j,n);
      } else {
        matrix_vector_partial(x,y,step*j,step*(j+1));
      }
    }

    double *tmp;
    tmp = x;
    x = y;
    y = tmp;
  }*/

  // parallel approach  
  unsigned long nloops = 6;
  unsigned long step = n/nloops;
  int j;

  for (i=0; i<10000; i=i+1) 
  {
    #pragma omp parallel num_threads(nloops)
      {
        #pragma omp for
          for(j=0;j<nloops;j++) 
          {
            if (j == nloops-1) {
              matrix_vector_partial(x,y,step*j,n);
            } else {
              matrix_vector_partial(x,y,step*j,step*(j+1));
            }
          }

        #pragma omp barrier
          {}

        #pragma omp master
          {
            double *tmp;
            tmp = x;
            x = y;
            y = tmp;
          }
      }
  }

  double end = omp_get_wtime();
  double diff = (end - start);

  printf("Time taken: %lf seconds.\n", diff); 
  
  printf("%lf \n", x[0]);
  printf("%lf \n", x[n-1]);   

  free(x);
  free(y);
}


