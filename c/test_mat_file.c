#include <stdio.h>
#include <string.h> 
#include <stdlib.h> 

#include "matrix.h"
#include "mat.h"

// suite sparse
#define CS_LONG
#include "cs.h"

typedef struct MatlabSparseMatrix {
	mxArray *array;
	int nzmax; 
	double *Pr;
	mwIndex *Ir;
	mwIndex *Jc;
} MatlabSparseMatrix;

MatlabSparseMatrix readSparseMatrix(MATFile *pmat, const char* name) {
	MatlabSparseMatrix result = {NULL, 0, NULL, NULL, NULL};

  	result.array = matGetVariable(pmat, name);

  	if (result.array == NULL) {
    	printf("Error reading variable %s!\n", name);
    	return result;
  	}

  	result.nzmax = mxGetNzmax(result.array);
  	result.Pr = mxGetPr(result.array);
  	result.Ir = mxGetIr(result.array);
  	result.Jc = mxGetJc(result.array);

  	return result;
}

// function to read the integer variable N
int readN(MATFile *pmat) {
  mxArray *pN = matGetVariable(pmat, "N");

  if (pN == NULL) {
    printf("Error reading variable N!\n");
    return 0;
  }

  int N = mxGetScalar(pN);
  mxDestroyArray(pN);

  return N;
}


int main() {
  MATFile *pmat;

  const char *file = "/home/sbordt/Dropbox/Masterarbeit/masterthesis/data/test.mat";

  pmat = matOpen(file, "r");

  if (pmat == NULL) {
    printf("Error opening %s\n", file);
    return 0;
  }

  // read variables
  int N = readN(pmat);
  printf("N: %d\n", N);

  MatlabSparseMatrix sp = readSparseMatrix(pmat, "P");
  printf("Number of non-zero entries: %d\n", sp.nzmax);

  printf("%lu, %lu\n", sizeof(mwIndex), sizeof(CS_INT));

  printf("Jc: ");
  int i = 0;
  for (i=0;i<N+1;i++) {
  	printf("%lu ", sp.Jc[i]);
  }
  printf("\n");

  printf("Ir: ");
  i = 0;
  for (i=0;i<sp.nzmax;i++) {
  	printf("%lu ", sp.Ir[i]);
  }
  printf("\n");

  printf("Pr: ");
  i = 0;
  for (i=0;i<sp.nzmax;i++) {
  	printf("%lf ", sp.Pr[i]);
  }
  printf("\n");

  cs matrix;
  matrix.nzmax = sp.nzmax;
  matrix.n = N;
  matrix.m = N;
  matrix.p = sp.Jc;
  matrix.i = sp.Ir;
  matrix.x = sp.Pr;
  matrix.nz = -1;

  cs_print(&matrix, 0);

  // 5 vectors in a row
  int num = 2;
	cs *x = cs_spalloc(N, num, num, 1, 1);
	
	int j=0;
	for (j=0;j<num;j++) {
		cs_entry(x,0,j,1.0);	
	}

	cs_print(x, 1);

  // multiplication!
	x = cs_compress(x);

	for (i=0;i<10000;i++) {
		cs *y = cs_multiply(&matrix, x);
		cs_free(x);
		x = y;
	}
	
	cs_print(x, 1);	

  // clean up
  mxDestroyArray(sp.array);
  matClose(pmat);

  return 0;
}