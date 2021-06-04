
 
 class ListNode {
      val: number
      next: ListNode | null
      constructor(val?: number, next?: ListNode | null) {
          this.val = (val===undefined ? 0 : val)
          this.next = (next===undefined ? null : next)
      }
 }
 

 function mergeTwoLists(l1: ListNode | null, l2: ListNode | null): ListNode | null {
     return null;

};

let sampleListNode = new ListNode(1,);

console.log(sampleListNode.val)
console.log(sampleListNode)