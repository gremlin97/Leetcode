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
        ListNode* prev = nullptr;
        ListNode* curr = head;
        ListNode* fast = head;
            
        if(curr->next == nullptr){
            return nullptr;
        }
        
        while(fast != nullptr){
            if(fast->next == nullptr){
                break;
            }
            fast = fast->next;
            fast = fast->next;
            prev = curr;
            curr = curr->next;
        }
        
        prev->next = curr->next; 
        return head;
    }
};