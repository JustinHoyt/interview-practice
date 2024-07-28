import { describe, expect, it } from "bun:test";
import { threeSum } from "./0015_3sum";

const sort = (arr: number[]) => arr.sort((a, b) => a - b);

describe("3 sum", () => {
  it("should find single match", () => {
    expect(
      threeSum([1, -2, -3, 1]).map(sort),
    ).toEqual(
      [[1, 1, -2]].map(sort),
    );
  });

  it("should use subtractive form for fours and nines", () => {
    expect(
      threeSum([-1, 0, 1, 2, -1, -4]).map(sort),
    ).toEqual(
      [[-1, 0, 1], [-1, -1, 2]].map(sort),
    );
  });
});
