def merge_intervals(intervals):
    if not intervals:
        return []

    intervals.sort()
    merged = []
    current_start, current_end = intervals[0]

    for start, end in intervals[1:]:
        if start <= current_end:
            current_end = max(current_end, end)
        else:
            merged.append((current_start, current_end))
            current_start, current_end = start, end

    merged.append((current_start, current_end))

    return merged


intervals_list = [(1, 3), (2, 6), (8, 10)]

result = merge_intervals(intervals_list)
print(result)
