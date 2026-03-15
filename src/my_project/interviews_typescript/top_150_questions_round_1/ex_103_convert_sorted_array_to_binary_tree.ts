import { TreeNode } from './TreeNode';      

function sortedArrayToBST(nums: number[]): TreeNode | null {
    function buildBST(left: number, right: number): TreeNode | null {
        if (left > right) {
            return null;
        }
        
        // Choose middle element as root to ensure height-balanced tree
        const mid = Math.floor((left + right) / 2);
        
        // Create root node with middle element
        const root = new TreeNode(nums[mid]);
        
        // Recursively build left and right subtrees
        root.left = buildBST(left, mid - 1);
        root.right = buildBST(mid + 1, right);
        
        return root;
    }
    
    return buildBST(0, nums.length - 1);
}

