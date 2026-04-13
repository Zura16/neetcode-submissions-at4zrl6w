class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int  write = 1;
        for(int i =0;i<nums.size()-1;i++){
            if(nums[i]!=nums[i+1]){
                nums[write] = nums[i+1];
                write++;
            }
            else{
               continue;
            }
        }
        return write;
    }
};