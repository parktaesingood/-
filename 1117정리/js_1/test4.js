const p1 = ['rock', 'paper', 'scissors', 'scissors', 'rock', 'rock', 'paper', 'paper', 'rock', 'scissors']
const p2 = ['paper', 'paper', 'rock', 'scissors', 'paper', 'scissors', 'scissors', 'rock', 'rock', 'rock']

const playGame = (p1_choice, p2_choice) => {
    switch (p1_choice) {
        case 'rock': {
            switch (p2_choice) {
                case 'rock':
                    console.log(0)
                    break
                case 'scissors':
                    console.log(1)
                    break
                case 'paper':
                    console.log(2)
                    break
            }
        }
        break
        case 'scissors': {
            switch (p2_choice) {
                case 'rock':
                    console.log(2)
                    break
                case 'scissors':
                    console.log(0)
                    break
                case 'paper':
                    console.log(1)
                    break
            }
        }
        break
        case 'paper': {
            switch (p2_choice) {
                case 'rock':
                    console.log(1)
                    break
                case 'scissors':
                    console.log(2)
                    break
                case 'paper':
                    console.log(0)
                    break
            }
        }
        break
        
    }
}

for (let i = 0; i < p1.length; i++) {
    console.log(`${i+1}번째 게임`)
    playGame(p1[i],p2[i])
}
// 2
// 0
// 2
// 0
// 2
// 1
// 2
// 1
// 0
// 2
