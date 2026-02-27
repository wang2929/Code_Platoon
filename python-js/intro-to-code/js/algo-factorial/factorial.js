function factorial(num) {
  let product = 1;
  for (let i = 1; i <= num; i++) {
    product = product * i;
  }
  return product;
}

module.exports = factorial;
