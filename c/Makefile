all: test_open_blas test_omp




test_open_blas:
	gcc -o ../bin/test_open_blas test_open_blas.c -I /opt/OpenBLAS/include/ -L/opt/OpenBLAS/lib -lopenblas -lpthread -lgfortran

test_omp:
	gcc -fopenmp -o ../bin/test_omp test_omp.c