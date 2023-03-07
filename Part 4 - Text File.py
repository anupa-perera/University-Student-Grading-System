statuses = ["Module retriever", "Exclude", "Progress (module trailer)", "Progress"]

progressionOutcomes = {
    # "Module retriever"
    statuses[0]: ((80, 40, 0), (80, 20, 20), (60, 60, 0), (60, 40, 20),
                  (60, 20, 40), (60, 0, 60), (40, 80, 0), (40, 60, 20),
                  (40, 40, 40), (40, 20, 60), (20, 100, 0), (20, 80, 20),
                  (20, 60, 40), (20, 40, 60), (0, 120, 0), (0, 100, 20),
                  (0, 80, 40), (0, 60, 60)),
    # "Exclude"
    statuses[1]: ((40, 0, 80), (20, 20, 80), (20, 0, 100), (0, 40, 80), (0, 20, 100), (0, 0, 120)),
    # "Progress (module trailer)"
    statuses[2]: ((100, 20, 0), (100, 0, 20)),
    # "Progress"
    statuses[3]: (120, 0, 0)
}


def get_credit_int(credit_type):
    while True:
        try:
            value = int(input('Please enter your credits at ' + credit_type + ' :'))
            allowed_values = (0, 20, 40, 60, 80, 100, 120)
            if value not in allowed_values:
                print("Out of range")
            else:
                break
        except ValueError:
            print("Integer required")

    return value


def check_sum():
    while True:
        global pass_credit, defer_credit, fail_credit
        if pass_credit + defer_credit + fail_credit != 120:
            print('Total incorrect')
            pass_credit = get_credit_int('pass')
            defer_credit = get_credit_int('defer')
            fail_credit = get_credit_int('fail')
        else:
            break


def print_input_progression():
    # https://realpython.com/read-write-files-python/#appending-to-a-file

    with open('input_progression.txt', 'r') as reader:
        line = reader.readline()
        while line != '':
            print(line, end='')
            line = reader.readline()


def reset_file():
    storage_file = open("input_progression.txt", "w")
    storage_file.close()


reset_file()

while True:
    pass_credit = get_credit_int('pass')
    defer_credit = get_credit_int('defer')
    fail_credit = get_credit_int('fail')
    check_sum()
    with open('input_progression.txt', 'a') as writer:
        if pass_credit == 120:
            print(statuses[3])
            writer.write(
                statuses[3] + ' - ' + ', '.join((str(pass_credit), str(defer_credit), str(fail_credit))) + '\n')

        else:
            for key, value in progressionOutcomes.items():

                if (pass_credit, defer_credit, fail_credit) in value:
                    print(key)
                    writer.write(
                        key + ' - ' + ', '.join((str(pass_credit), str(defer_credit), str(fail_credit))) + '\n')
                    break

    processMore = input(
        "Would you like to enter another set of data?\nEnter 'y' for yes or 'q' to quit and view results:"
    )

    if processMore == 'q':
        break

print_input_progression()
