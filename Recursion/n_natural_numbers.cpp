#include <iostream>
using namespace std;
int sum_of_n(int n){
	if(n==0){
		return 0;
	}
	else{
		return n+sum_of_n(n-1);
	}
}

int main(int argc, char const *argv[])
{
	cout<<sumx_of_n(10)<<endl;
	return 0;
}