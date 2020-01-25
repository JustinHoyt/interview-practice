const isMatchingWord = (isMatchedSoFar, [wordChar, queryChar]) => {
    return isMatchedSoFar && (queryChar === wordChar || queryChar === "*");
};

const isMatchInWords = (isMatchInArray, [word, query]) => {
    const zippedWordAndQuery = Array.from(word).map((wordChar, i) => [wordChar, query[i]]);
    const matched = zippedWordAndQuery.reduce(isMatchingWord, true);

    return matched || isMatchInArray;
};

const dictionary_wildcard = (words, query) => {
    const filteredWords = words.filter( word => word.length == query.length);
    const zippedWordsAndQuery = filteredWords.map((word) => [word, query]);

    return zippedWordsAndQuery.reduce( isMatchInWords, false);
};


const words = ["foo", "bar", "baz"];
console.log(dictionary_wildcard(words, "b*r"));
console.log(dictionary_wildcard(words, "baz*"));
