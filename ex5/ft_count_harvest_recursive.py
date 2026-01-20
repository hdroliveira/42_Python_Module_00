def ft_count_harvest_recursive():

    total_days = int(input("Days until harvest: "))

    helper(1, total_days)


def helper(current_day, final_day):

    if current_day > final_day:
        print("Harvest time!")
        return

    print("Day", current_day)

    helper(current_day + 1, final_day)
