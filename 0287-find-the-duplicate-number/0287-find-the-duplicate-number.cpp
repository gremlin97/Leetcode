class Solution {
public:
    int findDuplicate(vector<int>& nums) {
        unordered_set<int> set;
        for(auto x:nums){
            if(set.find(x) != set.end()){
                return x;
            }
            else{
                set.insert(x);
            }
        }
    return 0;
    }
};