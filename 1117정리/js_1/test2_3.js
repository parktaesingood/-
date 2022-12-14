
    /* 
      1. 아래 코드를 object destructuring을 활용해 리팩토링 하시오.
      2. Rest operator를 활용해 아래 코드를 리팩토링 하시오.
      3. Spread operator를 활용해 아래 코드를 리팩토링 하시오.
    */

    // 1-1
    const savedFile = {
      name: 'profile',
      extension: 'jpg',
      size: 29930
    }
    function fileSummary({ file, extension, size, }) {
        console.log(`The file ${file.name}.${file.extension} is size of ${file.size} bytes.`)
    }
    fileSummary(savedFile);

    // 1-2
    const data = {
      username,
      password,
      email,
    }

    const username = data.username
    const password = data.password
    const email = data.email
    
    // 2 spread syntax(...)
    function addNumbers(...numbers) {
      const numbers = [a, b, c, d, e];
      return numbers.reduce((sum, number) => { 
        return sum + number
      }, 0)
    }

    // 3-1 spread syntax(...)
    const defaultColors = ['red', 'green', 'blue'];
    const favoriteColors = ['navy', 'black', 'gold', 'white']
    const palette = [...defaultColors, ...favoriteColors]
    console.log(palette)

    // 3-2
    const info1 = { name: 'Tom', age: 30 }
    const info2 = { isMarried: true, balance: 3000 }
    const fullInfo = {...info1, ...info2}
    console.log(fullInfo)
