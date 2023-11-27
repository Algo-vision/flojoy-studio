import { v4 as uuidv4 } from "uuid";
import { Leaf as NodeElement } from "@src/utils/ManifestLoader";
import { CtrlData } from "@src/types/node";

export const createNodeId = (nodeFunc: string) => `${nodeFunc}-${uuidv4()}`;

const firstMissingPositive = (nums: number[]): number => {
  let i = 0;
  const n = nums.length;

  while (i < n) {
    if (nums[i] < n && nums[nums[i]] !== nums[i]) {
      const tmp = nums[i];
      nums[i] = nums[tmp];
      nums[tmp] = tmp;
    } else {
      i++;
    }
  }

  for (let i = 0; i < n; i++) {
    if (nums[i] != i) {
      return i;
    }
  }
  return n;
};

export const createNodeLabel = (nodeFunc: string, takenLabels: string[][]) => {
  const nums = takenLabels.map((l) =>
    l[1] !== undefined ? parseInt(l[1]) : 0,
  );
  const availableNum = firstMissingPositive(nums);

  const nodeLabel = availableNum > 0 ? `${nodeFunc} ${availableNum}` : nodeFunc;

  return nodeLabel.replaceAll("_", " ");
};

export const ctrlsFromParams = (
  params: NodeElement["parameters"] | undefined,
  funcName: string,
): CtrlData => {
  if (!params) {
    return {};
  }

  return Object.fromEntries(
    Object.entries(params).map(([paramName, param]) => [
      paramName,
      {
        ...param,
        functionName: funcName,
        param: paramName,
        value: param.default ?? "",
      },
    ]),
  );
};