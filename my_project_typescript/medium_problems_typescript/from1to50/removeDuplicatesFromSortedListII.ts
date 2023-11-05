
 
 class ListNode {
     val: number
     next: ListNode | null
      constructor(val?: number, next?: ListNode | null) {
         this.val = (val===undefined ? 0 : val)
          this.next = (next===undefined ? null : next)
      }
 }
 

 function deleteDuplicates(head: ListNode | null): ListNode | null {

    if (head == null){
        return null
    }
    if (head.next == null){
        return head
    }
    if (head.val == head.next.val){
        let temp = deleteDuplicates(head.next)
        while(temp!=null){
            if (temp.val!=head.val){
                break
            }
            temp = temp.next
        }
        return temp
    }
    else{
        head.next = deleteDuplicates(head.next)
        return head
    }

};