def oddCells(m: int, n: int, indices: List[List[int]]) -> int:
    # Initialize arrays to track increments for rows and columns
    row = [0] * m
    col = [0] * n
    for r, c in indices:
        row[r] += 1
        col[c] += 1
    
    odd_rows = sum(r % 2 for r in row)
    odd_cols = sum(c % 2 for c in col)
    
    # Total odd cells = (odd rows * even cols) + (even rows * odd cols)
    even_rows = m - odd_rows
    even_cols = n - odd_cols
    return odd_rows * even_cols + even_rows * odd_cols