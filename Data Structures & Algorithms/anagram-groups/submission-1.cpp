class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> set;

        for (string& s : strs) {
            int count[26] = {0};

            for (char& c : s) {
                count[c - 'a']++;
            }

            string key;
            for (int i = 0; i < 26; i++) {
                key += to_string(count[i]) + '-';
            }

            set[key].push_back(s);
        }

        vector<vector<string>> result;
        for (const pair<const string, vector<string>>& element : set) {
            result.push_back(element.second);
        }

        return result;
    }
};