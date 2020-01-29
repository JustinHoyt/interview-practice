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

const zip = (arr1, arr2) => arr1.map((ele, idx) => [ele, arr2[idx]]);

const charMatch = ([wordChar, queryChar]) => wordChar === queryChar || queryChar === "*";

const dictionary_wildcard = (words, query) => {
    return words.filter( word => word.length == query.length)
        .some(word => zip([...word], [...query]).every(charMatch));
};

const words = ["foo", "bar", "baz"];
console.log(dictionary_wildcard(words, "b*r"));
console.log(dictionary_wildcard(words, "baz*"));
