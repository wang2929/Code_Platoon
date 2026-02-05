function linearSearch(searchTerm, arr) {
  for (let i = 0; i < arr.length; i++) {
    if (arr[i] == searchTerm) {
      return i;
    }
  }
  return undefined;
}

function globalLinearSearch(searchTerm, arr) {
  let foundList = [];
  for (let i = 0; i < arr.length; i++) {
    if (arr[i] == searchTerm) {
      foundList.push(i);
    }
  }
  return foundList;
}

module.exports = { linearSearch, globalLinearSearch };
