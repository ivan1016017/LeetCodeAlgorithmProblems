

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
 

function verticalOrder(root: TreeNode | null): number[][] {
    if(root == null) return [];
    let queue: [TreeNode, number][] = [[root, 100]]; 
    let dict : {[a : number]: Array<number>} = {};
    while(queue.length > 0){
        queue = queue.flatMap(tuple=>{
            let node = tuple[0];
            let index = tuple[1];
            let out: [TreeNode, number][] = [];
            if(index in dict){
                dict[index].push(node.val);
            }
            else{
                dict[index] = [node.val];
            }
            if(node.left != null){
                out.push([node.left, index - 1]);
            }
            if(node.right != null){
                out.push([node.right, index + 1]);
            }
            return out;
        });
    }
    return Object.values(dict);
};