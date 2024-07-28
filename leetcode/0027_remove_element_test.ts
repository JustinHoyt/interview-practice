import { describe, expect, it } from "bun:test";
import { removeElement } from "./0027_remove_element";

const numSort = (a: number, b: number) => a - b;
describe("Remove element", () => {
  it("should remove front values", () => {
    const actual: number[] = [1, 1, 1, 1, 3, 6, 6, 6];
    const expected: number[] = [3, 6, 6, 6];

    const len = removeElement(actual, 1);

    expect(len).toEqual(expected.length);
    expect(
      actual.slice(0, expected.length).sort(numSort),
    ).toEqual(expected.sort(numSort));
  });

  it("should remove end values", () => {
    const actual: number[] = [1, 1, 1, 1, 3, 6, 6, 6];
    const expected: number[] = [1, 1, 1, 1, 3];

    const len = removeElement(actual, 6);

    expect(len).toEqual(expected.length);
    expect(
      actual.slice(0, expected.length).sort(numSort),
    ).toEqual(expected.sort(numSort));
  });
});
