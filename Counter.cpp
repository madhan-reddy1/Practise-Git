#include<iostream>
using namespace std;

void rec1(int n){
	if(n==0){
		return ;
	}
	else{
		rec1(n-1);
		cout<<n<<"\n";
	}
}

int main(int argc, char const *argv[])
{
	rec1(5);
	return 0;
}

saikiranmadala10@gmail.com
