#include <iostream>
using namespace std;
int max_pieces(int num,int a,int b,int c)
{
	if(num==0){
		return 0;
	} 
	if(num<=-1){
		return -1;
	}
	int res =  max(max_pieces(num-a,a,b,c),
			max(max_pieces(num-b,a,b,c),max_pieces(num-c,a,b,c)));
	if(res==-1)
		return -1;
	return res+1;
}
int main(int argc, char const *argv[])
{
	int num = 23, a = 9, b = 11, c = 5;
	cout<<max_pieces(num,a,b,c);
	return 0;
}