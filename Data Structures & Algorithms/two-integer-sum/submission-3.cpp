class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int,int> numMap;

        for(int i= 0; i < nums.size(); i++){
            int index = target - nums[i];

            if(numMap.find(index) != numMap.end()){
                return{numMap[index], i };
            }
            numMap[nums[i]] = i;

        }
        return{};
    }
};
