const letterCombinataions1 = (digits) => {
    digit_map = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl",
                 "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}

    const genPerms = (idx) => {
        if(idx === -1) return [""]

        const chars = [...digit_map[digits[idx]]]
        return chars.reduce((results, char) =>
            results.concat(genPerms(idx-1).map((perm) => perm + char)), [])
    }

    return genPerms(digits.length-1)
}

const letterCombinataions2 = (digits) => {
    digit_map = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl",
                 "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}

    results = []
    const genPerms = (idx=0, word="") => {
        if(idx === digits.length) return results.push(word)

        for(let char of digit_map[digits[idx]])
            genPerms(idx+1, word.concat(char))
    }

    genPerms()
    return digits.length > 0 ? results : []
}


console.log(letterCombinataions1("23"))
console.log(letterCombinataions2("23"))

