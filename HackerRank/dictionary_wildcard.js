/*
 You are given an array of words and a string query. You must return true or false
 depending on whether the array of words match the query or not. A query may contain
 the wildcard character "*" which can match with any character at that spot.

Examples:
isMember(["foo", "bar", "baz"], "f*o")
will return true since the "*" matches the first "o" in foo


function dictionary_wildcard(words, query) {
    return words.filter(word => word.length == query.length)
                .some(word => wordsMatch(List(word), List(query)));
}

isMember(["foo", "bar", "baz"], "**")
will return false since there are no two-letter words in the array
*/
const R = require('ramda');

function dictionary_wildcard(words, query) {
    const wordsMatch = R.curry((matcher, word1, word2) => R.compose(R.map(matcher), R.zip(word1, word2)));

    const charMatcher = ([wordChar, queryChar]) => wordChar === queryChar || queryChar === "*";
    const queryMatches = wordsMatch(charMatcher, query);

    return R.compose(R.any(queryMatches), R.filter(word => word.length == query.length))(words);
}

const words = ["foo", "bar", "baz"];
console.log(dictionary_wildcard(words, "b*r"));
console.log(dictionary_wildcard(words, "baz*"));