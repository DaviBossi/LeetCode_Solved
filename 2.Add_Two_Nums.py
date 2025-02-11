def addTwoNumbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        current = dummy
        carry = 0

        while l1 or l2 or carry:
            if l1:
                carry +=l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next
            
            current.next = ListNode(carry%10)
            carry //= 10 
            current = current.next
        return (dummy.next)
    