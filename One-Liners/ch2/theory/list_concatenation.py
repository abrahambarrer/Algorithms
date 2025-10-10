# import matplotlib.pyplot as plt

def main():
    cardiac_cycle = [62, 60, 62, 64, 68, 77, 80, 76, 71, 66, 61, 60, 62]

    expected_cycles = cardiac_cycle[1:-2] * 10

    print(expected_cycles)

    # if plot
    # plt.plot(expected_cycles)

if __name__ == '__main__':
    main()