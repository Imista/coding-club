def max_container(heights_list):
    max_area = 0
    for i, height_a in enumerate(heights_list):
        width = 1
        for height_b in heights_list[i + 1:]:
            area = width * min(height_a, height_b)
            max_area = max(max_area, area)
            width += 1

    return max_area


if __name__ == "__main__":
    heights_list = [4, 3, 2, 1, 4]
    print(max_container(heights_list))
