const zip = (arr1, arr2) => arr1.map((k, i) => [k, arr2[i]]);

const dictionary_wildcard = (words, query) => {
    const filteredWords = words.filter( word => word.length == query.length);

    return filteredWords.reduce( (isMatchInArray, word) => {
        zipped_query_word = zip(Array.from(query), Array.from(word));

        const matched = zipped_query_word.reduce( (isMatchedSoFar, [queryChar, wordChar]) => {
            return isMatchedSoFar && (queryChar === wordChar || queryChar === "*");
        }, true);

        return matched || isMatchInArray;
    }, false);
}


const words = ["foo", "bar", "baz"];
console.log(dictionary_wildcard(words, "b*r"));
console.log(dictionary_wildcard(words, "baz*"));
