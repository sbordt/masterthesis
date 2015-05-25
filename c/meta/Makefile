OUTDIR = ../../bin/

CFLAGS = -O2 -lopenblas -lpthread -lgfortran

OPEN_BLAS = -I /opt/OpenBLAS/include/ -L/opt/OpenBLAS/lib

all: clean matrix_vector test_matrix_vector

clean:
	rm -f $(OUTDIR)test_matrix_vector $(OUTDIR)matrix_vector.o $(OUTDIR)matrix_vector.so

matrix_vector:
	gcc -o $(OUTDIR)matrix_vector.o -c generated/matrix_vector.c $(CFLAGS) -fPIC
	gcc -shared -o $(OUTDIR)matrix_vector.so $(OUTDIR)matrix_vector.o 

test_matrix_vector:
	gcc -o $(OUTDIR)test_matrix_vector test_matrix_vector.c $(OPEN_BLAS) $(CFLAGS)