
class ListNode {
     val: number
     next: ListNode | null
     constructor(val?: number, next?: ListNode | null) {
         this.val = (val===undefined ? 0 : val)
         this.next = (next===undefined ? null : next)
    }
 }


 function sortList(head: ListNode | null): ListNode | null {
     if (!head){
         return null
     }
     let myList: Array<number> = []
     while (head){
        myList.push(head.val)
        head = head.next
     }

     myList.sort( (a,b) => a<=b?-1:1)

     let point: ListNode = new ListNode(0)
     let newHead: ListNode = point

     for (let i = 0; i < myList.length; i++){
         point.next = new ListNode(myList[i])
         point = point.next
     }
    return newHead.next

};