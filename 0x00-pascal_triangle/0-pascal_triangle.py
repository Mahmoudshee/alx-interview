def pascal_triangle(n):
    """
    Generates Pascal's triangle of size n.

    Args:
        n (int): Number of rows in Pascal's triangle.

    Returns:
        list: List of lists representing Pascal's triangle.

    """
    triangle = []

    if n <= 0:
        return triangle

    for i in range(n):
        row = [1] * (i + 1)
        if i >= 2:
            prev_row = triangle[i - 1]
            for j in range(1, i):
                row[j] = prev_row[j - 1] + prev_row[j]
        triangle.append(row)

    return triangle

