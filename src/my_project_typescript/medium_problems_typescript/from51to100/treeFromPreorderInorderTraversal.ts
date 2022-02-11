

import { TreeNode } from "./lowestCommonAncestorOfTree"

 function buildTree(preorder: number[], inorder: number[]): TreeNode | null {
    let p: number = 0
    let i: number = 0
    const build =(stop: number | undefined): TreeNode | null => {
        if(inorder[i] !== stop){
            let root: TreeNode | null = new TreeNode(preorder[p++])
            root.left = build(root.val)
            i++
            root.right = build(stop)
            return root
        }
        return null
    }
    return build(undefined)
};