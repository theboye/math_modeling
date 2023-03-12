
#include <iostream>
#include <math.h>
using namespace std; 
int main () 
{ 
  int x = 0;
  int y = 0;
  int z = 0;
  cout<<"Введите x координату точки";
  cin>>x;
  cout<<"Введите y координату точки";
  cin>>y;
  cout<<"Введите z координату точки";
  cin>>z;

  float res = sqrt(x*x + y*y + z*z);
  cout<<res;
} 
