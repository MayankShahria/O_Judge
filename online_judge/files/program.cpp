#include<bits/stdc++.h>
using namespace std;
int main(){
	int n;
	cin>>n;
	vector<int> vect(n+1);
	for(int i=0;i<n;i++){
		cin>>vect[i];
	}
	if(n%2!=0){
		cout<<"{}";
		return 0;
	}
	
	vector<int> nums;
	int l=0;
	int r=n-1;
	int mid = l+(r-l)/2;
	
	partial_sort(nums.begin(),nums.begin()+mid,vect.end());
	
	nth_element(nums.begin()+mid+1,nums.begin()+n,nums.end());
	mid = mid+1;
	for(int i=0;i<mid;i++){
		if(abs(vect[i]-vect[mid+i])!=vect[i]){
			cout<<"{}";
			return 0;
		}
		nums.push_back(vect[i]);
	}
	
	for(int i=0;i<nums.size();i++){
		cout<<nums[i]<<" ";
	}
	return 0;
}
