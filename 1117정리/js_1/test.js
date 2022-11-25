// const colors = ['red','green','black']

// const printFunc = function (color) {
//     console.log(color)
// }
// colors.forEach(printFunc)


// let star = ''
// for (let i = 0; i<5; i++) {
//     star += '*'
//     console.log(star)
// }


// function palindrome(str) {
//     let lst = ''
//     for (let i = 4; i>0; i--) {
//         lst += str[i]
//     } 
//     console.log(lst)
//   }
// palindrome('level')
  
  // 출력
  // palindrome('level') => true
  // palindrome('hi') => false


function palindrome(str) {
    const reversed = str.split('').reverse().join('');
    return reversed === str ? true : false
}


function palindrom1(str) {
    return str.split(''.every((element,idx) => element === str[str.length - 1 - idx]))
}


console.log(palindrome('level'))
console.log(palindrome('leveld'))