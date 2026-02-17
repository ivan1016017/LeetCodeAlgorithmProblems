import { TreeNode } from './TreeNode';              

function rightSideView(root: TreeNode | null): number[] {
    if (!root) {
        return [];
    }
    
    const result: number[] = [];
    const queue: TreeNode[] = [root];
    
    while (queue.length > 0) {
        const levelSize = queue.length;
        
        for (let i = 0; i < levelSize; i++) {
            const node = queue.shift()!;
            
            // Add the rightmost node of each level
            if (i === levelSize - 1) {
                result.push(node.val);
            }
            
            // Add children to queue (left first, then right)
            if (node.left) {
                queue.push(node.left);
            }
            if (node.right) {
                queue.push(node.right);
            }
        }
    }
    
    return result;
}