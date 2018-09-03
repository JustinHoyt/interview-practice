function range(n) {
  let list = [];
  for (let i = 0; i < n; i += 1) {
    list.push(i);
  }
  return list;
}

/**
 * @param {{[denomination: number]: number}} set
 * @return {string}
 */
function hashSet(set) {
  return Object.entries(set)
    .sort((a, b) => a[0] - b[0])
    .map(([denomination, count]) => `${denomination}_${count}`)
    .join(',');
}

/**
 *
 * @param {number} money
 * @param {number[]} denominations
 */
function coin(money, denominations) {
  let memo = {};
  /**
   *
   * @param {number} amount
   * @return {{[hash: string]: {[denomination: number]: number}}}
   */
  function _coin(amount) {
    if (memo[amount]) return memo[amount];
    if (amount <= 0) return { [hashSet({})]: {} };

    /**
     * @type {{[hash: string]: {[denomination: number]: number}}}
     */
    let options = {};
    for (const denomination of denominations) {
      if (denomination > amount) continue;

      const waysToSplitRest = _coin(amount - denomination);
      if (!waysToSplitRest) return undefined;

      const waysToSplit = Object.values(waysToSplitRest)
        .map(way => ({
          ...way,
          [denomination]: (way[denomination] || 0) + 1,
        }))
        .reduce((waysToSplit, way) => {
          waysToSplit[hashSet(way)] = way;
          return waysToSplit;


        }, {});

      options = {
        ...options,
        ...waysToSplit,
      };
    }

    const value = Object.values(options).length <= 0 ? undefined : options;
    memo[amount] = value;
    return value;
  }

  const result = _coin(money) || {};

  // const readableOutput = Object.values(result)
  //   .map((wayToSplit, index) => {
  //     const splitOutput = Object.entries(wayToSplit)
  //       .map(([denomination, count]) =>
  //         range(count)
  //           .map(() => `${denomination}¢`)
  //           .join(', '),
  //       )
  //       .join(', ');

  //     return `${index + 1}. ${splitOutput}`;
  //   })
  //   .join('\n');
  // console.log(readableOutput);


  return Object.keys(result).length;
}

const money = 1000;
const denominations = [1, 3, 5, 10, 15, 20, 25, 26, 27, 30, 40, 50, 60, 70];
const ways = coin(money, denominations);
console.log(`Ways to make ${money}¢: ${ways} way(s)`);
