const intersection = (setA, setB) => new Set([...setA].filter(element => [...setB].includes(element)));

const intersectOthers = (_, i, sets) => {
    const otherSets = sets.filter((_, j) => i !== j);
    return otherSets.reduce((acc, set) => intersection(acc, set));
};

const setToExclude = (sets) => {
    const setIntersections = sets.map(intersectOthers);

    const {idx} = setIntersections.reduce((acc, set, i) => {
        return set.size > acc.size ? {idx: i, size: set.size} : acc;
    }, {idx: 0, size: 0});

    return idx;
};

sets = [new Set([1,2,3]), new Set([2,3,4]), new Set([4,5,6])];
console.log(setToExclude(sets));

