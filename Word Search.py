class Solution:
    def isWordExist(self, mat, word):
        n = len(mat)
        m = len(mat[0])
        
        # Direction vectors for Up, Down, Left, Right
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        # Ye function recursively word ko dhundhta hai
        def dfs(i, j, index):
            # Agar pura word match ho gaya
            if index == len(word):
                return True
            
            # Agar bounds ke bahar chale gaye ya character match nahi kiya
            if i < 0 or i >= n or j < 0 or j >= m or mat[i][j] != word[index]:
                return False

            # Current cell ko temporarily mark karte hain as visited
            temp = mat[i][j]
            mat[i][j] = "#"

            # Har direction mein search karte hain
            for dx, dy in directions:
                if dfs(i + dx, j + dy, index + 1):
                    return True

            # Backtrack karke original value wapas daal dete hain
            mat[i][j] = temp
            return False

        # Har cell se search start karte hain
        for i in range(n):
            for j in range(m):
                if mat[i][j] == word[0]:
                    if dfs(i, j, 0):
                        return True
                        
        return False
