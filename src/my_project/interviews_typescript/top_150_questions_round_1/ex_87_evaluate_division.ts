function calcEquation(equations: string[][], values: number[], queries: string[][]): number[] {
    // Build graph: adjacency list with weights
    const graph = new Map<string, Map<string, number>>();
    
    for (let i = 0; i < equations.length; i++) {
        const [dividend, divisor] = equations[i];
        const value = values[i];
        
        if (!graph.has(dividend)) {
            graph.set(dividend, new Map<string, number>());
        }
        if (!graph.has(divisor)) {
            graph.set(divisor, new Map<string, number>());
        }
        
        graph.get(dividend)!.set(divisor, value);
        graph.get(divisor)!.set(dividend, 1.0 / value);
    }
    
    function bfs(start: string, end: string): number {
        // Check if variables exist in graph
        if (!graph.has(start) || !graph.has(end)) {
            return -1.0;
        }
        
        // If start equals end and it exists in graph
        if (start === end) {
            return 1.0;
        }
        
        // BFS to find path from start to end
        const queue: [string, number][] = [[start, 1.0]]; // [node, accumulated_product]
        const visited = new Set<string>([start]);
        
        while (queue.length > 0) {
            const [node, product] = queue.shift()!;
            
            // Check all neighbors
            const neighbors = graph.get(node)!;
            for (const [neighbor, weight] of neighbors.entries()) {
                if (neighbor === end) {
                    return product * weight;
                }
                
                if (!visited.has(neighbor)) {
                    visited.add(neighbor);
                    queue.push([neighbor, product * weight]);
                }
            }
        }
        
        return -1.0;
    }
    
    // Process all queries
    const results: number[] = [];
    for (const [dividend, divisor] of queries) {
        results.push(bfs(dividend, divisor));
    }
    
    return results;
}