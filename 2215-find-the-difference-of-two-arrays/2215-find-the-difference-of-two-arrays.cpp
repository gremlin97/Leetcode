class Solution {
public:
    vector<vector<int>> findDifference(vector<int>& nums1, vector<int>& nums2) {
        unordered_set<int> set1;
        unordered_set<int> set2;
        vector<int> arr1;
        vector<int> arr2;
        
        for(auto x:nums1){
            set1.insert(x);
        }
        
        for(auto x:nums2){
            set2.insert(x);
        }
        
        for(auto x:set1){
            if(set2.find(x) == set2.end()){
                arr1.push_back(x);
            }
        }
               
        for(auto x:set2){
            if(set1.find(x) == set1.end()){
                arr2.push_back(x);
            }
        }       
               
        return {{arr1},{arr2}};
    }
};