// 백준 2588번
// 곱셈
// 입출력, 사칙연산, 수학

const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().split("\n");

const a = parseInt(input[0].trim());
const b = parseInt(input[1].trim());
const b1 = b % 10;
const b2 = Math.floor((b % 100) / 10);
const b3 = Math.floor(b / 100);

console.log(a * b1);
console.log(a * b2);
console.log(a * b3);
console.log(a * b);