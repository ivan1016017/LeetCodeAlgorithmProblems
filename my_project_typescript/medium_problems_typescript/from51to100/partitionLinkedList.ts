
class ListNode {
    val: number
    next: ListNode | null
    constructor(val?: number, next?: ListNode | null) {
        this.val = (val===undefined ? 0 : val)
        this.next = (next===undefined ? null : next)
    }
}


function partition(head: ListNode | null, x: number): ListNode | null {

        let smallerCur: ListNode = new ListNode(0)
        let largerCur: ListNode = new ListNode(0)
        let dummySmaller: ListNode = smallerCur
        let dummyLarger: ListNode = largerCur
        let cur: ListNode = head
        while (cur){
            if (cur.val < x){
                smallerCur.next = cur 
                smallerCur = smallerCur.next
            }
            else {
                largerCur.next = cur 
                largerCur = largerCur.next
            }
            cur = cur.next
        }
        largerCur.next = null 
        smallerCur.next = dummyLarger.next

        return dummySmaller.next


};