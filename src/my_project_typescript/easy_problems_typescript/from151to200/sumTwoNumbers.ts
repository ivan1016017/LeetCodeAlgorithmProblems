
 class ListNode {
      val: number
      next: ListNode | null
      constructor(val?: number, next?: ListNode | null) {
          this.val = (val===undefined ? 0 : val)
         this.next = (next===undefined ? null : next)
      }
 }


let carry = 0
function addTwoNumbers(l1: ListNode | null, l2: ListNode | null): ListNode | null {

    if (!l1 && !l2 && carry === 0){
        return null;
    }

    let x = l1 ? l1.val : 0
    let y = l2 ? l2.val : 0

    let nextL1 = l1 ? l1.next : null
    let nextL2 = l2 ? l2.next : null 

    let sum = x + y + carry 
    carry = Math.floor(sum/10)
    sum = sum%10



    return {
        val: sum,
        next: addTwoNumbers(nextL1,nextL2)
    }

};