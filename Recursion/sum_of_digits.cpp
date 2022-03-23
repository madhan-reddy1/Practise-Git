#include <iostream>
using namespace std;
int sum_of_digits_rec(int num){
	if(num<=9){
		return num;
	}
	else{
		return (num%10)+sum_of_digits_rec(num/10);
	}

}

int main(int argc, char const *argv[])
{
	cout<<sum_of_digits_rec(234);
	return 0;
}