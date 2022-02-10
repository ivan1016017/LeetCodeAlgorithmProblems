

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
 

 function lowestCommonAncestor(root: TreeNode | null, p: TreeNode | null, q: TreeNode | null): TreeNode | null {


    let ans: TreeNode = null
    
    function recurseTree(currentNode: TreeNode | null,  p: TreeNode | null, q: TreeNode | null): boolean{

        if (currentNode == null){
            return false
        }
        let left: boolean = recurseTree(currentNode.left,p,q) ? true:false 

        let right: boolean = recurseTree(currentNode.right,p,q) ? true:false 


        let mid: boolean = (currentNode==p || currentNode==q)?true:false 

        if ([mid, left, right].filter(Boolean).length >= 2){
            ans = currentNode
        }

        return [mid, left, right].filter(Boolean).length > 0



    } 

    recurseTree(root,p,q)
    return ans
};