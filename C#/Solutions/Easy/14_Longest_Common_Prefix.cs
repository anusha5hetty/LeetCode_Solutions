

namespace Solutions.Easy
{
  internal class _14_Longest_Common_Prefix
  {
    public static string longestCommonPrefix(string[] strs)
    {
      if (strs.Length == 0)
        return "";
      else if (strs.Length == 1)
        return strs[0];

      var minLength = strs.Min(s => s.Length);
      var commonPrefix = "";

      for(int idx=0;idx<minLength;idx++)
      {
        for(int jdx=0; jdx< strs.Length - 1; jdx++ )
        {
          if (strs[jdx][idx] != strs[jdx+1][idx])
              return commonPrefix;
        }
        commonPrefix += strs[0][idx];
      }

      return commonPrefix;
    }
  }
}
