import { TreeNode } from './TreeNode';     

function averageOfLevels(root: TreeNode | null): number[] {
    if (!root) {
        return [];
    }
    
    const queue: TreeNode[] = [];
    queue.push(root);
    const answer: number[] = [];
    
    while (queue.length > 0) {
        const qlen = queue.length;
        let row = 0;
        
        for (let i = 0; i < qlen; i++) {
            const node = queue.shift()!;
            row += node.val;
            
            if (node.left) queue.push(node.left);
            if (node.right) queue.push(node.right);
        }
        
        answer.push(row / qlen);
    }
    
    return answer;
}