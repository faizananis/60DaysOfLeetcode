class Solution {
public:
    string mergeAlternately(string word1, string word2) {
        string str;
        int i=0;
        while(i<word1.length()||i<word2.length())
        {
            if(i<word1.length())
            {
                str.push_back(word1[i]);
            }
            if(i<word2.length())
            {
                str.push_back(word2[i]);
            }
            i++;
        }
        return str;
    }
};