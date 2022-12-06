class ListNode {
        val: number
       next: ListNode | null
       constructor(val?: number, next?: ListNode | null) {
           this.val = (val===undefined ? 0 : val)
           this.next = (next===undefined ? null : next)
        }
    }

function isPalindrome(head: ListNode | null): boolean {

    let currentNode = head;
    let arr: number[] = [];

    while (currentNode){
        arr.push(currentNode.val);
        currentNode = currentNode.next;
    }

    let lenArr: number = arr.length



    for (let i = 0; i < Math.floor(lenArr/2);i++){
        if (arr[i] !== arr[lenArr-1-i]) return false 
    }
    return true 

    // return arr.join('') === arr.reverse().join('')

}

