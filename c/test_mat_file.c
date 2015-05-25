#include <stdio.h>
#include <string.h> 
#include <stdlib.h> 
#include "mat.h"

#define BUFSIZE 256

int main() {
  MATFile *pmat;

  const char *file = "/home/sbordt/Dropbox/Masterarbeit/masterthesis/data/test.mat";

  pmat = matOpen(file, "w");

  //matPutVariable(pmat, "LocalString", pa3);

  matClose(pmat);

  return 0;
}