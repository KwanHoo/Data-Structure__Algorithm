// 백준 18108번
// 1998년생인 내가 태국에서는 2541년생 ? !
// 입출력, 수학, 사칙연산

var fs = require('fs');
var input = fs.readFileSync('/dev/stdin').toString()

var n = parseInt(input);

console.log(n - 543);