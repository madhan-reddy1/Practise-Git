#include<iostream>
#include<math.h>
using namespace std;

void powerset(char *set,int set_size)
{
	unsigned int pow_set_size=pow(2,set_size);
	int counter,j;

	for (int counter= 0; counter < pow_set_size; ++counter)
	{
		for (int j = 0; j < set_size ; ++j)
		{
			if(counter & (1<<j))
				cout<<set[j];
		}
		cout<<endl;
	}

}
int main(int argc, char const *argv[])
{ 
	char set[] = {'a','b','c'};
	powerset(set,3);
	return 0;
}