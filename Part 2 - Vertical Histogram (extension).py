progress_count = 0
trailer_count = 0
retriever_count = 0
excluded_count = 0

statuses = ["Module retriever", "Exclude", "Progress (module trailer)", "Progress"]

input_progressions = []

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


def draw_histogram(shape):

    if shape == 'horizontal':
        print('\n-----------------------------------------------------------------')
        print('Horizontal Histogram')
        print('{:12s} : {:s}'.format('Progress ' + str(progress_count), get_stars(progress_count)))
        print('{:12s} : {:s}'.format('Trailer ' + str(trailer_count), get_stars(trailer_count)))
        print('{:12s} : {:s}'.format('Retriever ' + str(retriever_count), get_stars(retriever_count)))
        print('{:12s} : {:s}'.format('Excluded ' + str(excluded_count), get_stars(excluded_count)))
        print('\n' + str(get_total_outcomes()) + ' outcomes in total.')
        print('-----------------------------------------------------------------')

    else:
        # https://stackoverflow.com/questions/43563672/python-plotting-a-histogram-downward
        print('\n Progress   Trailing   Retriever   Excluded')
        status_counts = (progress_count, trailer_count, retriever_count, excluded_count);
        remaining = status_counts
        while any(remaining):
            print(''.join('     *     ' if i else '           ' for i in remaining))
            remaining = [i - 1 if i else 0 for i in remaining]
        print('\n' + str(get_total_outcomes()) + ' outcomes in total.')
        print('\n')


def get_stars(count):
    stars = ''
    for x in range(count):
        stars += '*'
    return stars


def get_total_outcomes():
    return retriever_count + progress_count + excluded_count + trailer_count

while True:
    pass_credit = get_credit_int('pass')
    defer_credit = get_credit_int('defer')
    fail_credit = get_credit_int('fail')
    check_sum()

    if pass_credit == 120:
        print(statuses[3])
        input_progressions.append(
            statuses[3] + ' - ' + ', '.join((str(pass_credit), str(defer_credit), str(fail_credit)))
        )
        progress_count += 1
    else:
        for key, value in progressionOutcomes.items():

            if (pass_credit, defer_credit, fail_credit) in value:
                print(key)
                input_progressions.append(
                    key + ' - ' + ', '.join((str(pass_credit), str(defer_credit), str(fail_credit)))
                )
                if key == statuses[0]:
                    retriever_count += 1

                elif key == statuses[1]:
                    excluded_count += 1

                else:
                    trailer_count += 1

                break

    processMore = input(
        "Would you like to enter another set of data?\nEnter 'y' for yes or 'q' to quit and view results:"
    )

    if processMore == 'q':
        break

draw_histogram('horizontal')
draw_histogram('vertical')
