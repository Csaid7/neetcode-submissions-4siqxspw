class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {

        unordered_set<int> seen;// create a hashmanp
        for(int i : nums){ //iterating through the map and add the content to the hashmap
            if(seen.count(i)){
                return true;
            }
            seen.insert(i);
        }
        return false;

    }
};
