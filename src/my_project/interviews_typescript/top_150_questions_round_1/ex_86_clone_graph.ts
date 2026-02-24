class _Node {
    val: number
    neighbors: _Node[]

    constructor(val?: number, neighbors?: _Node[]) {
        this.val = (val===undefined ? 0 : val)
        this.neighbors = (neighbors===undefined ? [] : neighbors)
    }
}

function cloneGraph(node: _Node | null): _Node | null {
    if (!node) {
        return null;
    }
    
    // HashMap to store original node -> cloned node mapping
    const oldToNew = new Map<_Node, _Node>();
    
    // BFS approach
    const queue: _Node[] = [node];
    oldToNew.set(node, new _Node(node.val));
    
    while (queue.length > 0) {
        const curr = queue.shift()!;
        
        // Process all neighbors
        for (const neighbor of curr.neighbors) {
            // If neighbor hasn't been cloned yet
            if (!oldToNew.has(neighbor)) {
                // Clone the neighbor
                oldToNew.set(neighbor, new _Node(neighbor.val));
                // Add to queue for processing
                queue.push(neighbor);
            }
            
            // Add the cloned neighbor to the current cloned node's neighbors
            oldToNew.get(curr)!.neighbors.push(oldToNew.get(neighbor)!);
        }
    }
    
    return oldToNew.get(node)!;
}
    