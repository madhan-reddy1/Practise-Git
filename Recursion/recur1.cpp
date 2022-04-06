#include <iostream>
using namespace std;
int fun1(int n){
	if (n==1){
		return 0;
	}
	else{
		return 1+fun1(n/2);
	}
}
void fun2(int n){
	if(n==0){
		return ;
	}
	fun2(n/2);
	cout<<(n%2);
}
void fun3(int n){
	if (n==0)
	{
		return ;
	}
	fun3(n-1);
	cout<<n<<endl;

}

int main(int argc, char const *argv[])
{
	fun3(7);
	return 0;
}