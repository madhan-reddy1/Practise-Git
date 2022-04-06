#include<iostream>
using namespace std;

int oddoccur(int arr[],int n){

	int res=0;
	for (int i = 0; i < n; ++i)
	{
		res=res^arr[i];
	}
	return res;
}

int main(int argc, char const *argv[])
{	
	int arr[]={1,1,10,2,2},k=5;
	cout<<oddoccur(arr,k);
	
}