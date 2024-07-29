class DefaultMap<K, V> extends Map<K, V> {
  constructor(private zero: () => V) {
    super();
  }

  override get(el: K): V {
    let val = super.get(el);
    if (val == null) this.set(el, this.zero());

    return super.get(el)!;
  }
}

type TripletStr = `${number},${number},${number}`;

function threeSum(nums: number[]): number[][] {
  nums.sort((a, b) => a - b);
  const resNums: number[] = [];
  let count = new DefaultMap<number, number>(() => 0);
  for (const val of nums) {
    if (count.get(val) >= 3) continue;

    count.set(val, count.get(val) + 1);
    resNums.push(val);
  }

  const valToIdxs = new DefaultMap<number, number[]>(() => []);
  resNums.forEach((v, i) => valToIdxs.get(v).push(i));

  function twoSum(target: number, skipIdx: number): Array<[number, number]> {
    const matches = Array<[number, number]>();

    for (const [i, num] of resNums.entries()) {
      if (i === skipIdx) continue;

      const complementVal = target - num + 0;
      const complementIdxs = valToIdxs.get(complementVal);
      if (complementIdxs.every((j) => j === i || j === skipIdx)) continue;

      matches.push([num, complementVal]);
    }

    return matches;
  }

  const matchSet = new Set<TripletStr>();
  const matchArr: number[][] = [];
  for (const [i, target] of resNums.entries()) {
    const twoSumMatches = twoSum(-target, i);

    for (const match of twoSumMatches) {
      match.push(target);
      match.sort((a, b) => a - b);
      const matchStr = match.join(",") as TripletStr;
      if (matchSet.has(matchStr)) continue;

      matchSet.add(matchStr);
      matchArr.push(match);
    }
  }

  return matchArr;
}

export { threeSum };
