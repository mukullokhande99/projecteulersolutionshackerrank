#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int palindrome(int z){
	int ra = 1;
    int num=z;
    int pal = 1;
    while(num!=0){num/=10;pal*=10;} 
    
    pal /= 10;
    while(pal > ra){
       if((z/pal)%10 != (z/ra)%10){
           return false;
       }
        pal/=10;ra*=10;
    }
    return true;
}
int main() {
    int a; cin >> a;
    while(a--){
        int num;cin>>num;
        int mo =0;
        for(int i=1;i<1000;i++){
            for(int j=1;j<1000;j++){
                if(i*j < num && palindrome(i*j)){
                    mo = max(mo, i*j);
                }
            }
            }
        cout << mo <<endl;
    }
    return 0;
}
