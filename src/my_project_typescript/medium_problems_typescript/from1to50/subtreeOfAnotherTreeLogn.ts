
// * Definition for a binary tree node.
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


 function isSubtree(root: TreeNode | null, subRoot: TreeNode | null): boolean {
     let v1: boolean 
     let v2: boolean 
     let v3: boolean 

    if (root === null){
        return false
    }
    else {
        v1 = false 
        if (root.val === subRoot.val){
            v1 = checkSubtree(root,subRoot)
        }
        v2 = isSubtree(root.left, subRoot.left)
        v3 = isSubtree(root.right, subRoot.right)
    }

    return v1 || v2 || v3

};

function checkSubtree(root:TreeNode, subRoot:TreeNode):boolean{
    if (root === null && subRoot === null){
        return true 
    }
    else if (root === null || subRoot === null){
        return false
    }
    else {
        if (root.val === subRoot.val){
            let v1 = checkSubtree(root.left, subRoot.left)
            let v2 = checkSubtree(root.right, subRoot.right)
            return v1 && v2
        }
        return false 
    }
}