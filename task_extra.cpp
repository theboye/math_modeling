#include <iostream>
using namespace std; 
int main () 
{ 
    int R = 0;
    int r = 0;
    int razn = 0;
    cout<<"введите что-нибудь ";
    cin>>R;
    cin>>r;
    if (R>r)
        razn = R*R - r*r;
    else if (r>R)
        razn = r*r - R*R;
    else
    {
        cout<<"nenada";
        return 1;
    }
    cout<<razn<<"\n\r";
    float res = 3.14*(razn);
    
    cout<<res;
    
    
} 