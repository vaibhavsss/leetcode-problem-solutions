class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()
        ans = []
        prev = ""
        for f in folder:
            # Only skip if f is a true subfolder
            if prev and f.startswith(prev) and f[len(prev)] == '/':
                continue
            ans.append(f)
            prev = f
        return ans
