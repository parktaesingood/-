
function printSSAFY() {
  return new Promise(function (resolve, reject) {
    setTimeout(() => {
      console.log('SSAFY')
      resolve()
    }, 1500)
  })
}

console.log('Hi')
printSSAFY().then(() => {
  console.log('Bye')
})

// 3.1 Pending(대기) 상태
//    - 비동기 처리 로직이 아직 완료되지 않은 상태


new Promise() // -> Pending 상태

// resolve 와 reject 는 콜백함수
new Promise(function (resolve, reject) {
  // 여기에 로직 작성
})

// 3.2 Fulfilled(이행) 상태
//    - 비동기 처리 로직이 정상적으로 완료되어, Promise 가 결과 값을 반환해준 상태

const getData = new Promise(function (resolve, reject) {
  resolve(123)
})

getData.then((value) => {
  console.log(value);
  return value
})
.then((value) => {
  console.log(value);
  return value
})

// 3.3 Rejected(실패) 상패
//    - 비동기 처리가 실패하거나, 오류가 발생한 상태

const getData = new Promise(function (resolve, reject) {
  // 강제로 실패했다를 명시
  reject('실패')
})

// 많이 보게될 코드 구조
// 성공 시 로직 -> 다른 로직 -> 다른 로직
//    -> 하나라도 중간에 실패하거나 오류가 나면 catch 호출
getData.then((value) => {
  console.log(value);
  return value
}).then((value) => {
  console.log(value);
  return value
}).then((value) => {
  console.log(value);
  return value
}).catch((error) => {
  console.log(error)
})
