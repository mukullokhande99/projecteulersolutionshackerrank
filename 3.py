#include <iostream>
#include <cmath>
#include <algorithm>
#include <vector>
#include <cstdio>



using namespace std;
typedef long long ll;

ll solve(ll k){
    ll q = k;
    for(ll j=2;;j++){
        if(j*j > q){
            return q;
        }
        if(k%j == 0){
            return max(j, solve(k/j));
        }
    }
}
int main() {
    int a;cin>>a;
    while(a--){
        ll k; cin >> k;
        ll p = solve(k);
        cout<<p<<endl;
    }
    return 0;
}