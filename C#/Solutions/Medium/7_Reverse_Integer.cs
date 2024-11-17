// https://leetcode.com/problems/reverse-integer/

namespace Solutions.Medium
{
  internal class _7_Reverse_Integer
  {
    public static int Reverse(int x)
    {
      var longRev = 0L;
      bool is_neg = x < 0;
      while (x % 10 != x)
      {
        longRev = (longRev * 10) + (x % 10);
        if (longRev < Int32.MinValue || longRev > Int32.MaxValue)
        {
          return 0;
        }
        x /= 10;

      }

      return (int)longRev;
    }
  }
}
