# Tiffany's Coding Cheat Sheet

## Markdown
- Using Markdown Preview Enhanced, view the formatted markdown using ctrl+k + v

## HTML and CSS
- Typical files include index.html (the structure), styles.css (the formatting and colors), and app.js (the javascript script to do stuff)
- <b>Add stylesheet:</b> `<link rel="stylesheet" href="styles.css">`
- <b>Add script.js:</b> `<script src="path/to/script.js" defer async></script>`
  - defer async is because scripts are linked to the top of the index.html page but run at the end
### shorthands in VS Code
- Can use ! + tab to make the html head
- elem > child.class * number, specify the format using selectors, can specify #id or .class, and multiply for repeat
- An HTML element can have multiple classes separated by spaces e.g. class="class1 class2", then can style by combining multiple CSS styles

## Python
### Lambda Functions
TBD but I want to write something about it

## Javascript
- <b>if-else shorthand:</b> condition ? true-expression : false-expression
### DOM stuff
- getElementsByClassName() returns an HTMLCollection, not an array. To use array methods, cast to Array using Array.from()
### Arrow Functions
Arrow functions are good to use for one-liner functions. They're compact and quicker to write. General recommendation is to use arrow functions when possible. Do not use arrow functions for class methods, for functions that you want to reuse outside of the current function, and for functions that lose too much readability/clarity.

#### Example Syntax
##### No parameters:
```
function() {
    expression;
    expression;
    more expressions;
}
```
You can use these arrow functions:
```
() => expression;   // Short functions

() => {             
  expressions;      // Long functions
}
```
##### One parameter:
```
function(param) {
    expression;
    expression using param;
    more expressions;
}
```
You can use these arrow functions:
```
param => expression     // Short functions

(param) => expression   // Short functions

param => {
  statements            // Long functions
}
```
##### More than one parameter
```
function(param1, param2, param3) {
    expression using param1;
    expression using param1 and param2;
    expression using param 3;
}
```
You can use these arrow functions:
```
// Short functions
(param1, paramN) => expression 

// Long functions
(param1, paramN) => {
  statements
}
```
### Array Manipulation
#### Filter 
Filter is a method for array manipulation. It takes a function and keeps all elements that return true in the function. Below example filters out all elements less than 5.
```
function exampleFilter(arr) { 
    return arr.filter((elem) => elem > 5); 
}
console.log(exampleFilter([1, 3, 5, 7, 9, 11]));
// Prints [7, 9, 11]
```