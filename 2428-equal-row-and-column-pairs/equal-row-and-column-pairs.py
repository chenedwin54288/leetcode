class Solution(object):
    def equalPairs(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        column_dict = {}
        for i in range(0, len(grid)):
            column = []
            for j in range(0, len(grid)):
                column.append(grid[j][i])
            column_dict[str(column)] = 1 + column_dict.get(str(column), 0)
        
        pair_count = 0
        for row in grid:
            pair_count += column_dict.get(str(row), 0)

        return pair_count
            
            



        