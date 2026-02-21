import { TreeNode } from './TreeNode';             

function isValidBST(root: TreeNode | null): boolean {
    function validate(node: TreeNode | null, minVal: number, maxVal: number): boolean {
        // Empty tree is valid
        if (!node) {
            return true;
        }
        
        // Check if current node violates BST property
        if (node.val <= minVal || node.val >= maxVal) {
            return false;
        }
        
        // Recursively validate left and right subtrees
        // Left subtree: all values must be < node.val
        // Right subtree: all values must be > node.val
        return validate(node.left, minVal, node.val) && 
               validate(node.right, node.val, maxVal);
    }
    
    return validate(root, -Infinity, Infinity);
}