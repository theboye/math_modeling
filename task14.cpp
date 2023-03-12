
#include <iostream>
#include <math.h>
using namespace std; 
int main () 
{ 
  int a = 0;
  int b = 0;
    int c = 0;
    int d = 0;
    int num = 0;
    cout<<"write nomor: ";
    cin>>num;
    
     a = num%10;
     b = num%100/10;
     c = num%1000/100;
     d = num/1000;
    
    cout<<a+b+c+d;
} 
