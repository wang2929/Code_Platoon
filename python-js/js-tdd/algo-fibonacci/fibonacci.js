function fibonacci(num) {
  if (num == 0) {
    return 0;
  }
  if (num == 1) {
    return 1;
  }
  let fibList = [0, 1];
  for (let i = 2; i <= num; i++) {
    let nextNum = fibList[i-1] + fibList[i-2];
    fibList.push(nextNum);
  }
  return fibList[fibList.length - 1];
}

module.exports = fibonacci;