import { _Node } from "./Node";

function copyRandomList(head: _Node | null): _Node | null {
    /**
     * Approach: Using HashMap
     * Time Complexity: O(n)
     * Space Complexity: O(n)
     */
    if (head === null) {
        return null;
    }

    // Map old nodes to new nodes
    const oldToNew = new Map<_Node, _Node>();

    // First pass: create all new nodes
    let curr: _Node | null = head;
    while (curr !== null) {
        oldToNew.set(curr, new _Node(curr.val));
        curr = curr.next;
    }

    // Second pass: assign next and random pointers
    curr = head;
    while (curr !== null) {
        const newNode = oldToNew.get(curr)!;

        if (curr.next !== null) {
            newNode.next = oldToNew.get(curr.next)!;
        }

        if (curr.random !== null) {
            newNode.random = oldToNew.get(curr.random)!;
        }

        curr = curr.next;
    }

    return oldToNew.get(head)!;
}
