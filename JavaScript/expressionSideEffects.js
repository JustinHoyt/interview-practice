function vowels(str) {
	var matches;

	// pull out all the vowels
	if (str && (matches = str.match( /[aeiou]/g ))) {
		return matches;
	}
}

console.log(vowels( "Hello World" )); // ["e","o","o"]
