OUTDIR = ../bin/

OPEN_BLAS = -I /opt/OpenBLAS/include/ -L/opt/OpenBLAS/lib -lopenblas

MATLABROOT = /usr/local/MATLAB/R2014a/

MATLAB = -I $(MATLABROOT)extern/include -L $(MATLABROOT)bin/glnxa64

MATLABLINKS = -lmat -lmwfl -lmwi18n -lut -lmx -l:libboost_filesystem.so.1.49.0 -l:libboost_system.so.1.49.0 -lmwcpp11compat -l:libhdf5_hl.so.6 -l:libhdf5.so.6 -lmwresource_core -lmwMATLAB_res -l:libboost_chrono.so.1.49.0 -l:libboost_date_time.so.1.49.0 -l:libboost_regex.so.1.49.0 -l:libboost_serialization.so.1.49.0 -l:libboost_signals.so.1.49.0 -l:libboost_thread.so.1.49.0 -l:libboost_log.so.1.49.0 -l:libboost_log_setup.so.1.49.0 -l:libicudata.so.49 -l:libicuuc.so.49 -l:libicui18n.so.49 -l:libicuio.so.49

SUITESPARSE = -lcxsparse

CFLAGS = -O2 -lpthread -lgfortran

all: clean test_open_blas test_omp test_mat_file

clean:
	rm -f $(OUTDIR)test_open_blas $(OUTDIR)test_omp $(OUTDIR)test_mat_file

test_open_blas:
	gcc -o $(OUTDIR)test_open_blas test_open_blas.c $(OPEN_BLAS) $(CFLAGS)

test_omp:
	gcc -fopenmp -o $(OUTDIR)test_omp test_omp.c

test_mat_file:
	gcc -o $(OUTDIR)test_mat_file test_mat_file.c $(MATLAB) $(MATLABLINKS) $(SUITESPARSE) $(CFLAGS)

