function findOrder(numCourses: number, prerequisites: number[][]): number[] {
    // Build adjacency list and in-degree array
    const graph: Map<number, number[]> = new Map();
    const inDegree: number[] = new Array(numCourses).fill(0);
    
    // Initialize graph
    for (let i = 0; i < numCourses; i++) {
        graph.set(i, []);
    }
    
    // Build the graph
    for (const [course, prereq] of prerequisites) {
        graph.get(prereq)!.push(course);
        inDegree[course]++;
    }
    
    // Initialize queue with courses that have no prerequisites
    const queue: number[] = [];
    for (let i = 0; i < numCourses; i++) {
        if (inDegree[i] === 0) {
            queue.push(i);
        }
    }
    
    const result: number[] = [];
    
    // Process courses in topological order
    while (queue.length > 0) {
        const course = queue.shift()!;
        result.push(course);
        
        // Reduce in-degree for dependent courses
        for (const nextCourse of graph.get(course)!) {
            inDegree[nextCourse]--;
            if (inDegree[nextCourse] === 0) {
                queue.push(nextCourse);
            }
        }
    }
    
    // If we processed all courses, return the order; otherwise return empty array
    return result.length === numCourses ? result : [];
}

  