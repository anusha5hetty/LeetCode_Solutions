using System;
using System.Collections;
using System.Collections.Generic;
using System.Collections.ObjectModel;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Solutions.Easy  
{
  internal class _20__ValidParentheses
  {
    private static Dictionary<string, string> mappings = new Dictionary<string, string>() { { "(",")" }, { "{","}" }, { "[", "]" } };
    private IReadOnlyDictionary<string, string> readonlyDict = new ReadOnlyDictionary<string, string>(mappings);

    public bool isValid(string s)
    {
      var stack = new Stack();
      foreach(char x in s)
      {
        var strX = x.ToString();
        if (readonlyDict.ContainsKey(strX))
          stack.Push(strX);

        else if (stack.Count == 0 || (!strX.Equals(readonlyDict[stack.Pop().ToString()])))
            return false;
      }

      return stack.Count == 0;
    }
  }
}
