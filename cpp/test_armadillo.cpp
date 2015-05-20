#include <iostream>
#include <armadillo>
#include <ctime>

using namespace std;
using namespace arma;

int main(int argc, char** argv)
{
	int n = 10000;
  	mat A = ones<mat>(n,n); 
  	mat B = ones<mat>(n,n);
 
 	time_t tstart, tend; 
 	tstart = time(0);  

  	mat C = A*B;

  	tend = time(0); 

  	cout << "It took "<< difftime(tend, tstart) <<" second(s)."<< endl;
   
  	return 0;
}