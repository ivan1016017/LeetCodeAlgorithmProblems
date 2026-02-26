function canFinish(numCourses: number, prerequisites: number[][]): boolean {
    // Build adjacency list and in-degree array
    const graph: Map<number, number[]> = new Map();
    const inDegree: number[] = new Array(numCourses).fill(0);
    
    // Initialize graph
    for (let i = 0; i < numCourses; i++) {
        graph.set(i, []);
    }
    
    // Build graph and calculate in-degrees
    for (const [course, prereq] of prerequisites) {
        graph.get(prereq)!.push(course);
        inDegree[course]++;
    }
    
    // Add all courses with no prerequisites to queue
    const queue: number[] = [];
    for (let i = 0; i < numCourses; i++) {
        if (inDegree[i] === 0) {
            queue.push(i);
        }
    }
    
    let coursesTaken = 0;
    
    // Process courses using BFS (Kahn's algorithm)
    while (queue.length > 0) {
        const course = queue.shift()!;
        coursesTaken++;
        
        // Reduce in-degree for dependent courses
        for (const nextCourse of graph.get(course)!) {
            inDegree[nextCourse]--;
            if (inDegree[nextCourse] === 0) {
                queue.push(nextCourse);
            }
        }
    }
    
    // If we took all courses, no cycle exists
    return coursesTaken === numCourses;
}

