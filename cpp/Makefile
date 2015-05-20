all: test_open_blas test_armadillo

test_open_blas:
	g++ -o ../bin/test_open_blas_cpp test_open_blas.cpp -I /opt/OpenBLAS/include/ -L/opt/OpenBLAS/lib -lopenblas -lpthread -lgfortran

test_armadillo:
	g++ test_armadillo.cpp -o ../bin/test_armadillo -O2 -larmadillo 