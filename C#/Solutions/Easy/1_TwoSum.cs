// https://leetcode.com/problems/two-sum/description/

namespace Solutions.Easy
{
  internal class _1_TwoSum
  {
    public int[] TwoSum(int[] nums, int target)
    {
      for (int idx = 0; idx < nums.Length; idx++)
      {
       for (int jdx = idx + 1; jdx < nums.Length; jdx++)
        {
          if (nums[idx] + nums[jdx] == target)
          {            
            return [idx, jdx];
          }
        }
      }

      return [-1, -1];
    }

    public int[] TwoSumBetter(int[] nums, int target)
    {
      //var indices = new int[2];
      var bingo = new Dictionary<int, int>();

      // In bingo dict we store the the number that is the other half of the number at a particular index
      // Eg: if target is 5 and nums[0] has 3, the other half of 3 is 2 (5-3). So on Bingo dict you store bingo[2] = 0. "bingo[other half] = index of the first half"
      bingo[target - nums[0]] = 0;

      for (int idx=1; idx<nums.Length; idx++)
      {
        if (bingo.ContainsKey(nums[idx]))
        {
          return [idx, bingo[nums[idx]]];
        }
        bingo[target - nums[idx]] = idx;
      }

      return [-1, -1];


    }
  }
}
