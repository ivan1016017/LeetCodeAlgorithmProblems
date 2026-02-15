import { TreeNode } from './TreeNode';                    

function countNodes(root: TreeNode | null): number {
    if (!root) {
        return 0;
    } else {
        return countNodes(root.left) + countNodes(root.right) + 1;
    }
}