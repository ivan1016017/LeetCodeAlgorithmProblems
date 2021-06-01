function countPrimes(n: number): number {
  let tempBoolean: boolean = false;

  let count: number = 0;
  // 0, and 1 are not prime numbers

  if (n === 0 || n === 1) {
    return count;
  }

  for (let i = 2; i < n; i++) {
    if (isPrime(i)) {
      count += 1;
    }
  }
  return count;
}

function isPrime(n: number): boolean {
  let isPrimeNumber: boolean = false;

  if (n === 0 || n === 1) {
    return isPrimeNumber;
  }
  if (n === 2) {
    isPrimeNumber = true;
    return isPrimeNumber;
  } 
  
  if (n >= 3) {
    for (let i = 2; i <= Math.sqrt(n); i++) {
      if (n % i === 0) {
        return false;
      }
    }
    isPrimeNumber = true;
    return isPrimeNumber;
  }
  else {
      return false;
  }
}

console.log(countPrimes(10));



