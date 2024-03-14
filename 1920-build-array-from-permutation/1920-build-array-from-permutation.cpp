class Solution {
public:
    vector<int> buildArray(vector<int>& nums) {
        int n = nums.size();
        vector<int> res;
        for(int i=0; i<n; i++){
            int index = nums[i];
            res.push_back(nums[index]);
        }
        return res;
    }
};