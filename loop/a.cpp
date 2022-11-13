#include<bits/stdc++.h>
using namespace std;

int main(){
    vector<int> nums;
    for(int i = 0;i<10;i++){
        nums.emplace_back(i);
    }
    for(auto x:nums) cout<<x<<endl;
    for(auto x:nums) x = x+100000;
    for(auto x:nums) cout<<x<<endl;
}