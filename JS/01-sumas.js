function contar(n) {
    for(let i = 0; i < n; i++) {
        console.log(i);
    }
}

console.time('contar');
contar(5);
console.timeEnd('contar');