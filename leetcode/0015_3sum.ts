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

type Triplet = [number, number, number];
type TripletStr = `${number},${number},${number}`;

export function threeSum(nums: number[]): number[][] {
  const valToIdxs = new DefaultMap<number, number[]>(() => []);
  nums.forEach((v, i) => valToIdxs.get(v).push(i));

  function twoSum(target: number, skipIdx: number): Array<[number, number]> {
    const matches = Array<[number, number]>();

    for (const [i, num] of nums.entries()) {
      const complementVal = target - num;
      const complementIdxs = valToIdxs.get(complementVal);

      if (i === skipIdx) continue;
      if (complementIdxs == null) continue;

      if (
        complementIdxs.every(
          (compIdx) => compIdx === i || compIdx === skipIdx,
        )
      ) continue;

      matches.push([num, complementVal]);
    }

    return matches;
  }

  const matches = new Set<TripletStr>();
  const matchesArr: number[][] = [];
  for (const [i, target] of nums.entries()) {
    const twoSumMatches = twoSum(-target, i);

    for (const match of twoSumMatches) {
      match.push(target);
      match.sort((a, b) => a - b);
      const matchStr = match.join(",") as TripletStr;
      if (matches.has(matchStr)) continue;

      matches.add(matchStr);
      matchesArr.push(match);
    }
  }

  return matchesArr;
}
