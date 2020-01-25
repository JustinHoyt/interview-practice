/*
 You are given an array of words and a string query. You must return true or false
 depending on whether the array of words match the query or not. A query may contain
 the wildcard character "*" which can match with any character at that spot.

Examples:
isMember(["foo", "bar", "baz"], "f*o")
will return true since the "*" matches the first "o" in foo


isMember(["foo", "bar", "baz"], "**")
will return false since there are no two-letter words in the array
*/

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
