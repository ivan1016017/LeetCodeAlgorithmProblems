import { TreeNode } from './TreeNode';             

function kthSmallest(root: TreeNode | null, k: number): number {
    const result: number[] = [];
    
    function inorder(node: TreeNode | null): void {
        if (!node) return;
        
        inorder(node.left);
        result.push(node.val);
        inorder(node.right);
    }
    
    inorder(root);
    return result[k - 1];
}