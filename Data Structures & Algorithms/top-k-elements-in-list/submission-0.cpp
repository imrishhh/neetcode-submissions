class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        int n = nums.size();
        vector<int> result(k);
        unordered_map<int, int> numberMap;
        for (int i = 0; i < n; i++) {
            numberMap[nums[i]]++;
        }

        priority_queue<pair<int, int>,
        vector<pair<int, int>>, greater<pair<int, int>>> pq;

        for (const pair<int, int>& number : numberMap) {
            pq.push({number.second, number.first});
            if (pq.size() > k)
                pq.pop();
        }

        for (int i = k - 1; i >= 0; i--) {
            result[i] = pq.top().second;
            pq.pop();
        }

        return result;
    }
};
