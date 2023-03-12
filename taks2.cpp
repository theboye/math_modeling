#include <iostream>
#include <math.h>
using namespace std; 
int main () 
{ 
  int x = 0;
  int y = 0;
  int z = 0;
  cout<<"Введите первое число: ";
  cin>>x;
  cout<<"Введите второе число: ";
  cin>>y;
  cout<<"Введите третье число: ";
  cin>>z;
    
    int sum = x+y+z;
    int mul = x*y*z;
    float arif = (x+y+z)/3 ;

  cout<<sum<<"\n\r" ;
  cout<<mul<<"\n\r" ;
  cout<<arif<<"\n\r" ;
} 
