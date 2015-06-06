#include <stdio.h>
#include <string.h> 
#include <stdlib.h> 

#include "matrix.h"
#include "mat.h"

// suite sparse
#define CS_LONG
#include "cs.h"

typedef struct MatlabDenseMatrix {
	mxArray *array;
	int N;
	int M; 
	double *Pr;
} MatlabDenseMatrix;

typedef struct MatlabSparseMatrix {
	mxArray *array;
	int N;
	int M;
	int nzmax; 
	double *Pr;
	mwIndex *Ir;
	mwIndex *Jc;
} MatlabSparseMatrix;

MatlabDenseMatrix readDenseMatrix(MATFile *pmat, const char *name) {
	MatlabDenseMatrix result = {NULL, 0, 0, NULL};

	result.array = matGetVariable(pmat, name);

  	if (result.array == NULL) {
    	printf("Error reading variable %s!\n", name);
    	return result;
  	}

  	result.M = mxGetM(result.array);
  	result.N = mxGetN(result.array);
  	result.Pr = mxGetPr(result.array);

  	return result;
}

MatlabSparseMatrix readSparseMatrix(MATFile *pmat, const char *name) {
	MatlabSparseMatrix result = {NULL, 0, 0, 0, NULL, NULL, NULL};

  	result.array = matGetVariable(pmat, name);

  	if (result.array == NULL) {
    	printf("Error reading variable %s!\n", name);
    	return result;
  	}

  	result.M = mxGetM(result.array);
  	result.N = mxGetN(result.array);
  	result.nzmax = mxGetNzmax(result.array);
  	result.Pr = mxGetPr(result.array);
  	result.Ir = mxGetIr(result.array);
  	result.Jc = mxGetJc(result.array);

  	return result;
}

cs *matlabDenseToCXSparse(const MatlabDenseMatrix* mat) {
  int i,j;
	cs *mat_cs = cs_spalloc(mat->N, mat->M, mat->N*mat->M, 1, 1);
	
	for (i=0; i<mat->M; i++) {
  		for (j=0; j<mat->N; j++) {
  			cs_entry(mat_cs, i, j, mat->Pr[i*mat->M+j]);
  		}	
  	}

  	cs *mat_cs_compressed = cs_compress(mat_cs);
  	cs_spfree(mat_cs);
  	return mat_cs_compressed;
}

cs *matlabSparseToCXSparse(const MatlabSparseMatrix* mat) {
  cs *matrix = malloc(sizeof(cs));

  matrix->nzmax = mat->nzmax;
  matrix->n = mat->N;
  matrix->m = mat->M;
  matrix->p = mat->Jc;
  matrix->i = mat->Ir;
  matrix->x = mat->Pr;
  matrix->nz = -1;	

  return matrix;
}

/*void printMatlabSparseMatrix(const *MatlabSparseMatrix sp) {
  printf("Number of non-zero entries: %d\n", sp.nzmax);

  printf("Jc: ");
  for (i=0;i<N+1;i++) {
  	printf("%lu ", sp.Jc[i]);
  }
  printf("\n");

  printf("Ir: ");
  for (i=0;i<sp.nzmax;i++) {
  	printf("%lu ", sp.Ir[i]);
  }
  printf("\n");

  printf("Pr: ");
  for (i=0;i<sp.nzmax;i++) {
  	printf("%lf ", sp.Pr[i]);
  }
  printf("\n");
}*/

int main(int argc, const char **argv) {
  int i, num_iter;

	if (argc != 7) {
		printf("Parameters: sparse-matrix-file.mat sparse-marix-name dense-matrix-file.mat dense-matrix-name number-of-iterations output-file.mat\n");
		return 0;
	}

	const char *sparse_file = argv[1];
	const char *sparse_name = argv[2];

	const char *dense_file = argv[3];
	const char *dense_name = argv[4];
	
  sscanf(argv[5], "%i", &num_iter);
	const char *output_file = argv[6];

	// read the sparse matrix
  printf("Reading sparse matrix...");

	MATFile *pmat_sparse = matOpen(sparse_file, "r");

	if (pmat_sparse == NULL) {
		printf("Error opening %s\n", sparse_file);
		return 0;
	}
	
	MatlabSparseMatrix mat_A = readSparseMatrix(pmat_sparse, sparse_name);

	// read the dense matrix
  printf("Reading dense matrix...");
	MATFile *pmat_dense = matOpen(dense_file, "r");

	if (pmat_dense == NULL) {
		printf("Error opening %s\n", dense_file);
		return 0;
	}

  MatlabDenseMatrix mat_B = readDenseMatrix(pmat_dense, dense_name);

  // iterate
  printf("Iterating...");

  cs *A = matlabSparseToCXSparse(&mat_A);
  cs *B = matlabDenseToCXSparse(&mat_B);

	for (i=0;i<num_iter;i++) {
		cs *C = cs_multiply(A,B);
		cs_free(B);
		B = C;
	}
	
	// output
	//cs_print(B, 1);	

  // clean up
  mxDestroyArray(mat_A.array);
  mxDestroyArray(mat_B.array);
  	
  matClose(pmat_dense);
  matClose(pmat_sparse);

  return 0;
}