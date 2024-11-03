using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Solutions.Medium
{
  internal class _11_Container_With_Most_Water
  {
    public static int maxArea(int[] height)
    {
      int mostWater=0, water=0, firstIdx = 0;
      int lastIdx = height.Length - 1;
      while (firstIdx < lastIdx)
      {
        int gap = lastIdx - firstIdx;
        if (height[firstIdx] < height[lastIdx])
        {
          water = gap * height[firstIdx++]; // firstIdx is incremented after the current value is used with height. Equivalent to height[firstIdx]; firstIdx++;
        }
        else
        {
          water = gap * height[lastIdx--];
        }

        if(mostWater < water)
        {
          mostWater = water;
        }

      }
      return mostWater;
    }
  }
}
