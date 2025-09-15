namespace Solutions.Medium;

public class _27_GroupAnagramsClass
{
  public static IList<IList<string>> GroupAnagrams(string[] strs)
  {
    var store = new Dictionary<string, IList<string>>();
    foreach (var item in strs)
    {
      var uniqueKey = new int[26];
      foreach(char ch in item)
      {
        uniqueKey[ch - 'a'] = 1;
      }

      var keyString = string.Join(",", uniqueKey);

      if (store.TryGetValue(keyString, out var existingGroup))
      {
        existingGroup.Add(item);
      }
      else
      {
        store[keyString] = new List<string> { item };
      }

    }
    return store.Values.ToList();

  }
}