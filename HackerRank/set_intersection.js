const intersection = (setA, setB) => new Set([...setA].filter(element => [...setB].includes(element)));

const intersectOthers = (_, i, sets) => {
    const otherSets = sets.filter((_, j) => i !== j);
    return otherSets.reduce((acc, set) => intersection(acc, set));
};

const setToExcludeBruteForce = (sets) => {
    const setIntersections = sets.map(intersectOthers);

    const {idx} = setIntersections.reduce((acc, set, i) => {
        return set.size > acc.size ? {idx: i, size: set.size} : acc;
    }, {idx: 0, size: 0});

    return idx;
};


const setToExclude = (sets) => {
    const lastIdx = sets.length - 1

    const leftMemo = {};
    sets.reduce((acc, set, i) => leftMemo[i] = (intersection(acc, set)), sets[0]);
    const rightMemo = {};
    [...sets].reverse().reduce(
        (acc, set, i) => rightMemo[lastIdx - i] = (intersection(acc, set)
    ), sets[0]);

    const intersectSizes = sets.map((_, i) => {
        if(i === 0) return rightMemo[0].size;
        if(i === lastIdx) return leftMemo[lastIdx].size;
        return intersection(leftMemo[i-1], rightMemo[i+1]).size;
    });

    const {idx} = intersectSizes.reduce((acc, size, i) => {
        return size > acc.size ? {idx: i, size} : acc;
    }, {idx: 0, size: 0});

    return idx;
};


sets = [new Set([1,2,3,4,5,6]), new Set([2,3,4,6]), new Set([4,5,6]), new Set([2,4,5,6])];
console.log(setToExclude(sets));
