import statistics

def main():

    stat = [20, 50, 50, 58]

    print(Average(stat))


def Average(stat):

    return statistics.mean(stat)


main()