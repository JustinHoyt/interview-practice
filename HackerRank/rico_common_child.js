function max(list) {
  let best = 0;
  for (const item of list) {
    if (item > best) {
      best = item;
    }
  }
  return best;
}

const memo = {};
function commonChild(s1, s2) {
  const hash = `${s1}|${s2}`;
  if (memo[hash] !== undefined) return memo[hash];
  if (s1 === s2) return s1.length;
  if (s1.length <= 0) return 0;

  const options = [];
  for (let i1 = 0; i1 < s1.length; i1 += 1) {
    for (let i2 = 0; i2 < s2.length; i2 += 1) {
      const sub1 = s1.substring(0, i1) + s1.substring(i1 + 1, s1.length);
      const sub2 = s2.substring(0, i2) + s2.substring(i2 + 1, s2.length);

      options.push(commonChild(sub1, sub2));
    }
  }

  const result = max(options);
  memo[hash] = result;
  return result;
}

console.log(commonChild("shinchanshinchanshinchanshinchanshinchanshinchan", "noharaaanoharaaanoharaaanoharaaanoharaaanoharaaa"));
