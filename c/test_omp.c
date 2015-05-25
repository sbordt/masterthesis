#include <stdio.h>
#include <omp.h>

int main(int argc, char **argv)
{
  int i, thread_id, nloops;

  int x[] = {1,2,3,4};

  int j;

  for (j=0;j<10;j=j+1)
  {
    #pragma omp parallel 
      {
        #pragma omp for
          for (i=0; i<4; ++i)
            {
              x[i] = x[i]+1;
            }

      
/*
      #pragma omp sections
      {

      #pragma omp section
        {
          x[0] = x[0] + 1;
          thread_id = omp_get_thread_num();

          printf("Thread %d performed the first section.\n", thread_id );
        }

      #pragma omp section
        {
          x[1] = x[1] + 1;
          thread_id = omp_get_thread_num();

          printf("Thread %d performed the second section.\n", thread_id );
        }

      #pragma omp section
        {
          x[2] = x[2] + 1;
          thread_id = omp_get_thread_num();

          printf("Thread %d performed the second section.\n", thread_id );
        }

      #pragma omp section
        {
          x[3] = x[3] + 1;
          thread_id = omp_get_thread_num();

          printf("Thread %d performed the second section.\n", thread_id );
        }
      }*/

      #pragma omp barrier
        {

        }

      #pragma omp master
        {
          printf("Barrier reached, this is x:\n" );
          int i;
          for (i=0;i<4;i++)
          {
            printf("%d\n", x[i]);
          }
        }
      }

  }

  return 0;
}