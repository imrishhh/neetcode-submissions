class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        vector<int> result(nums.size(), 1);

        int prefix = 1, suffix = 1;

        for (int i = 0; i < nums.size(); i++) {
            result[i] *= prefix;
            prefix *= nums[i];

            result[nums.size() - i - 1] *= suffix;
            suffix *= nums[nums.size() - i - 1];
        }

        return result;
    }
};

/*
// [1, 2, 4, 6]
// prefix initial: 1
// suffix initial: 1
// result initial: [1, 1, 1, 1]
// LOOP BEGINS:
// i = 0
    prefix: 1;
    suffix: 6;
    [1, 1, 1, 1]
// i = 1
    prefix: 2;
    suffix: 24;
    [1, 1, 6, 1]
// i = 2
    prefix: 8;
    suffix: 48;
    [1, 24, 12, 1]
// i = 3
    prefix: 48;
    suffix: 48;
    [48, 24, 12, 8];*/