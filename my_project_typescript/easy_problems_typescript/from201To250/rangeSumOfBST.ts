

class TreeNode {
    val: number
    left: TreeNode | null
    right: TreeNode | null
    constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
        this.val = (val===undefined ? 0 : val)
        this.left = (left===undefined ? null : left)
        this.right = (right===undefined ? null : right)
    }
}
 

function rangeSumBST(root: TreeNode | null, low: number, high: number): number {

    let sum: number = 0;
    if (root == null) {
        return sum;
    }

    if (root.val > low) {
        sum += rangeSumBST(root.left, low, high);
    }
    if (root.val <= high && root.val >= low) {
        sum += root.val;
    }
    if (root.val < high) {
        sum += rangeSumBST(root.right, low, high);    
    }    
    
    return sum;

};