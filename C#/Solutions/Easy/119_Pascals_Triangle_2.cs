
namespace Solutions.Easy
{
    class _119_Pascals_Triangle_2
    {
      public static int[] getRow(int rowIdx)
      {
        var prevRow = new int[] { 1 };
        var basicEntity = new int[] { 0 };
        for (int idx=0; idx<rowIdx; idx++)
        {
          var tempRow = basicEntity.Concat(prevRow).Concat(basicEntity).ToArray();
          prevRow = new int[prevRow.Length + 1];
          for(int jdx = 0; jdx < tempRow.Length-1; jdx++)
          {
            prevRow[jdx] = tempRow[jdx] + tempRow[jdx + 1];
          }
        }

        return prevRow;
    }
    }
}

