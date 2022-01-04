#include<iostream>
#include <string>
using namespace std;

bool ispalindrome(string &str,int start,int end){
	if(start>=end)
		return true;
	if (str[start] != str[end])
		return false;
	
	return (str[start]==str[end]) && ispalindrome(str,start+1,end-1);

}

int main(int argc, char const *argv[])
{
	string str;
	cout<<"Enter String to check palindrome"<<endl;
	cin>>str;
	if ( ispalindrome(str,0,str.length()-1) )
	{
		cout<<"it is a palindrome"<<endl;
	}
	else{
		cout<<"Not a plaindrome"<<endl;
	}
	return 0;
}