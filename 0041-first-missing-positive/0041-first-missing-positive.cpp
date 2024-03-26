class Solution {
public:
    int firstMissingPositive(vector<int>& nums) {
        if(nums.size() == 1){
            if(nums[0] == 1){
                return 2;
            }
            else{
                return 1;
            }
        }
        set<int> s;
        for(auto x:nums){
            if(x>0){
                s.insert(x);
            }
        }
        auto it = s.begin();
        int i = 1;
        for(i; i<nums.size() + 1; i++){
            cout<<(*it)<<' '<<i<<endl;
            if(i != *it){
                return i;
            }
            it++;
        }
        return (i);
    }
};