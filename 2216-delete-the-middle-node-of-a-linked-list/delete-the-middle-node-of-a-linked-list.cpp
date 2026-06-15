/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* deleteMiddle(ListNode* head) {

        if (head->next == nullptr){
            return nullptr;
        }

        ListNode* slow = head;
        ListNode* fast = head->next;
        ListNode* prev = slow;
        while(fast != nullptr and fast->next != nullptr){
            prev = slow;
            slow = slow->next;
            fast = fast->next->next;   
        }


        if (fast == nullptr)
            prev->next = prev->next->next;
        else
            slow->next = slow->next->next;

        return head;

        return head;


        
    }
};