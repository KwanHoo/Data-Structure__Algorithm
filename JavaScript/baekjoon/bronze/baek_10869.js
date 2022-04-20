// 백준 10869번
// 사칙연산
// 입출력, 사칙연산

//* JS에서 콘솔을 통해 값을 입력 받기 위해서는 readlin 모듈 이용가능
//! 하지만 readline 모듈 보다는 fs 모듈 사용할것!

var fs = require('fs');
var input = fs.readFileSync('/dev/stdin').toString().split(' ');
var a = parseInt(input[0]);
var b = parseInt(input[1]);
console.log(a + b);
console.log(a - b);
console.log(a * b);
console.log(parseInt(a / b));
console.log(a % b);