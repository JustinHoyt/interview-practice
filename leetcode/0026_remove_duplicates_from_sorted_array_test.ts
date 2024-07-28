import { describe, expect, it } from "bun:test";
import { removeDuplicates } from "./0026_remove_duplicates_from_sorted_array";

describe("Remove duplicates from sorted array test", () => {
  it("should return empty array", () => {
    const actual: number[] = [];
    const expected: number[] = [];

    const len = removeDuplicates(actual);

    expect(len).toEqual(expected.length);
    expect(actual.slice(0, expected.length)).toEqual(expected);
  });

  it("should return single array", () => {
    const actual: number[] = [1];
    const expected: number[] = [1];

    const len = removeDuplicates(actual);

    expect(len).toEqual(expected.length);
    expect(actual.slice(0, expected.length)).toEqual(expected);
  });

  it("should remove duplicates from small array", () => {
    const actual: number[] = [1, 1, 2];
    const expected: number[] = [1, 2];

    const len = removeDuplicates(actual);

    expect(len).toEqual(expected.length);
    expect(actual.slice(0, expected.length)).toEqual(expected);
  });

  it("should remove duplicates from beginning", () => {
    const actual: number[] = [1, 1, 2, 3, 4];
    const expected: number[] = [1, 2, 3, 4];

    const len = removeDuplicates(actual);

    expect(len).toEqual(expected.length);
    expect(actual.slice(0, expected.length)).toEqual(expected);
  });

  it("should remove duplicates from end", () => {
    const actual: number[] = [1, 2, 3, 4, 4];
    const expected: number[] = [1, 2, 3, 4];

    const len = removeDuplicates(actual);

    expect(len).toEqual(expected.length);
    expect(actual.slice(0, expected.length)).toEqual(expected);
  });

  it("should remove long chain of duplicates", () => {
    const actual: number[] = [1, 1, 1, 1, 3, 6];
    const expected: number[] = [1, 3, 6];

    const len = removeDuplicates(actual);

    expect(len).toEqual(expected.length);
    expect(actual.slice(0, expected.length)).toEqual(expected);
  });

  it("should remove multiple sets of duplicates 1", () => {
    const actual: number[] = [1, 1, 1, 1, 3, 6, 6, 6];
    const expected: number[] = [1, 3, 6];

    const len = removeDuplicates(actual);

    expect(len).toEqual(expected.length);
    expect(actual.slice(0, expected.length)).toEqual(expected);
  });

  it("should remove multiple sets of duplicates 2", () => {
    const actual: number[] = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4];
    const expected: number[] = [0, 1, 2, 3, 4];

    const len = removeDuplicates(actual);

    expect(len).toEqual(expected.length);
    expect(actual.slice(0, expected.length)).toEqual(expected);
  });

  it("should remove multiple sets of duplicates 3", () => {
    const actual: number[] = [0, 0, 0, 1, 1, 2, 3, 4, 4];
    const expected: number[] = [0, 1, 2, 3, 4];

    const len = removeDuplicates(actual);

    expect(len).toEqual(expected.length);
    expect(actual.slice(0, expected.length)).toEqual(expected);
  });
});
