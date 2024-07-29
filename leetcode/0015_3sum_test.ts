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

  it("should find multiple matches", () => {
    expect(
      threeSum([-1, 0, 1, 2, -1, -4, -1, 0, 1, 2, -1, -4]).map(sort),
    ).toEqual(
      [[-4, 2, 2], [-1, -1, 2], [-1, 0, 1]].map(sort),
    );
  });

  it("should pass speed test", () => {
    expect(
      threeSum(Array(3000).fill(0)),
    ).toEqual(
      [[0, 0, 0]],
    );
  });
});
