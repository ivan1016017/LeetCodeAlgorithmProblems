function simplifyPath(path: string): string {
    // Stack to keep track of valid directory names
    const stack: string[] = [];
    
    // Split the path by '/' and process each component
    const components = path.split('/');
    
    for (const component of components) {
        // Skip empty strings (from consecutive slashes) and current directory markers
        if (component === '' || component === '.') {
            continue;
        }
        // Parent directory - pop from stack if possible
        else if (component === '..') {
            if (stack.length > 0) {
                stack.pop();
            }
        }
        // Valid directory or file name
        else {
            stack.push(component);
        }
    }
    
    // Build the canonical path
    // Start with '/' and join all directories with '/'
    return '/' + stack.join('/');
}