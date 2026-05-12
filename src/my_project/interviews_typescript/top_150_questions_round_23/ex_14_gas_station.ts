function canCompleteCircuit(gas: number[], cost: number[]): number {
    const n = gas.length;
    let totalGas = 0;
    let currentTank = 0;
    let startStation = 0;

    for (let i = 0; i < n; i++) {
        const netGas = gas[i] - cost[i];
        totalGas += netGas;
        currentTank += netGas;

        if (currentTank < 0) {
            startStation = i + 1;
            currentTank = 0;
        }
    }

    return totalGas >= 0 ? startStation : -1;
};        