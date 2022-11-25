const participantNums = [[1, 3, 2, 2, 1],
[3, 7, 100, 21, 13, 6, 5, 7, 5, 6, 3, 13, 21],
[9, 1, 8, 7, 71, 33, 62, 35, 11, 4, 7, 71, 33, 8, 9, 1, 4, 11, 35]
]

function findSolo(arr) {
    // 카운트 결과를 담아줄 딕셔너리
    let counts = {}

    // 각 번호를 부여받은 사람을 count
    for (num of arr) {
        // counts 객체에 키가 없다면 1을 할당, 있다면 1을 더해줌
        if (counts[num] === undefined) {
            counts[num] = 1
        } else {
            counts[num] = counts[num] + 1
        }
    }

    // 깍두기 ( 값이 1인 0key ) 를 찾음
    for (count in counts) {
        if (counts[count] === 1) {
            console.log(count)
            break
        }
    }
}

participantNums.forEach((tc) => findSolo(tc))


    // if (!(num in counts)) {
    //     counts[num] = 1
    // } else {
    //     counts[num] = counts[num] + 1
    // }