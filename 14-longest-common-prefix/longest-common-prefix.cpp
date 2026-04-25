class TrieNode{
public:
    TrieNode* children[26];
    bool isEnd;
    int childCount;
    TrieNode(){
        isEnd = false;
        childCount = 0;
        for(int i=0; i<26; ++i){
            children[i]=NULL;
        }
    }
};

class Trie{
public:
    TrieNode* root;
    Trie(){
        root = new TrieNode();
    }
    void insert(string& word){
        TrieNode* node = root;
        for(auto&c: word){
            int idx = c-'a';
            if (node->children[idx] == NULL){
                node->children[idx] = new TrieNode();
                node->childCount++;
            }
            node = node->children[idx];
        }
        node->isEnd = true;
    }

    string longestCommonPrefix(){
        string prefix = "";
        TrieNode* node = root;

        while (node->childCount==1 and node->isEnd == false){
            for(int i=0; i<26;++i){
                if (node->children[i]!= NULL){
                    prefix.push_back(i+'a');
                    node = node->children[i];
                    break;
                }
            }
        }
        return prefix;
    }
};

class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        Trie trie;
        for(auto& string:strs){
            trie.insert(string);
        }
        return trie.longestCommonPrefix();
    }
};