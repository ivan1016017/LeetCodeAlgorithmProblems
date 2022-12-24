
class ListNode {
    val: number
    next: ListNode | null
    constructor(val?: number, next?: ListNode | null) {
        this.val = (val===undefined ? 0 : val)
        this.next = (next===undefined ? null : next)
    }
}
 

function mergeKLists(lists: Array<ListNode | null>): ListNode | null {
    if(lists===null)return null
    function listToArray(list:ListNode|null){
        if(list===null)return[]
        const array:number[] = []
        while(list !== null){
            array.push(list.val)
            list = list.next
        }
        return array
    }
    const arrayList = lists.map(val=>listToArray(val))

    const arrays:number[] = []
    arrayList.forEach(val=>arrays.push(...val))
    arrays.sort((a:number,b:number)=>a-b)

    if(arrays.length===0)return null
    const node = new ListNode(arrays.shift())
    let current = node
    while(arrays.length>0){
        current.next = new ListNode(arrays.shift())
        current = current.next
    }

    return node

};