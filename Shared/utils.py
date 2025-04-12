def mean_average(data, mean_width):
    new_array = []
    mean_width = int(mean_width)
    half_width = int(mean_width / 2)

    # 원래코드
    # for _ in range(half_width):
    #     new_array.append(0)

    for idx, _ in enumerate(data):
        if idx < half_width:
            # 원래코드: continue
            newValue = data[idx]
            new_array.append(newValue)
        elif idx > len(data) - (half_width + 1):
            # 원래코드: continue
            newValue = data[idx]
            new_array.append(newValue)
        else:
            newValue = sum(data[idx - half_width : idx + half_width + 1]) / mean_width
            new_array.append(newValue)

    # 원래코드
    # for _ in range(half_width):
    #     new_array.append(0)

    return new_array
