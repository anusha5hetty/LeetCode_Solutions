
namespace Solutions.Easy
{
  internal class _28_Find_The_First_String_Occurance
  {
    public static int StrStr(string haystack, string needle)
    {
      for(int idx=0; idx < haystack.Length; idx++)
      {
        if (haystack[idx] == needle[0] && SubstringExists(haystack, idx, needle))
        {
          return idx+1;
        }
      }
      return -1;
    }

    private static bool SubstringExists(string haystack, int haystackIdx, string needle)
    {
      for (int idx = 0; idx < needle.Length; idx++)
      {
        if(haystack[haystackIdx] != needle[idx])
          return false;
        haystackIdx++;
      }
      return true;
    }
  }
}
