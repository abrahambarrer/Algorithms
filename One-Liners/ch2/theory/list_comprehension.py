def main():
    employees = {'Alice': 100000,
                 'Bob': 99817,
                 'Carol': 122908,
                 'Frank': 88123,
                 'Eve': 93121}

    # [expression + structure]
    lst = [(key, val) for key, val in employees.items() if val >= 100000]

    print(lst)

if __name__ == '__main__':
    main()