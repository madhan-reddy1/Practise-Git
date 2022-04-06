#include <iostream>
using namespace std;

void twooddoccur(int arr[],int n)
{
	int uni=0,res1=0,res2=0;
	for(int i = 0; i < n; ++i)
	{
		uni=uni^arr[i]; // we will get xor of two odd numbers
	}
	int temp=uni&~(uni-1); //we are going to get the set bit from right side
	for (int i = 0; i < n; ++i)
	{
		if( arr[i]&temp!=0 )
		{
			res1=res1^arr[i];
		}
		else{
			res2=res2^arr[i];
		}
	}
	cout<<res1<<endl<<res2;
}

int main(int argc, char const *argv[])
{
	int arr[]={1,1,2,2,3,4,4,6},k=8;
	twooddoccur(arr,k);
	return 0;
}