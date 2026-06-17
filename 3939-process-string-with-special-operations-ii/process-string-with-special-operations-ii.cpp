class Solution {
public:
    char processStr(string s, long long k) {

        int sz = s.size();
        vector<long long> lengths(sz, 0);
        long long length = 0;

        for (int i = 0; i < sz; ++i) {
            if (s[i] >= 'a' && s[i] <= 'z') {
                length++;
            } else if (s[i] == '*') {
                if (length > 0) {
                    length--;
                }
            } else if (s[i] == '#') {
                length *= 2;
            }

            lengths[i] = length;
        }

        if (k >= lengths[sz - 1])
            return '.';

        for (int i = sz - 1; i >= 0; --i) {
            char c = s[i];
            long long curr = lengths[i];
            long long prev = i > 0 ? lengths[i - 1] : 0;

            if (c >= 'a' && c <= 'z') {
                if (k == prev)
                    return c;
            }

            else if (c == '#') {
                if (prev > 0) {
                    k = k % prev;
                }
            } else if (c == '%') {
                k = prev - 1 - k;
            }
        }

        return '.';
    }
};