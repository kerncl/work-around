import argparse


def positive_int(n):  # custom type
    try:
        v = int(n)
    except ValueError:
        raise argparse.ArgumentTypeError('Expected integer')
    if v <= 0:
        raise argparse.ArgumentTypeError('Expected positive integer')
    return v


def fib(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a


def Main():
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group()
    # Required input
    parser.add_argument("num",
                        help="This fibonacci number you wish to calculate",
                        type=positive_int)  # custom type#
    # optional [--<keyword>]
    # 1. read input
    parser.add_argument('-o', '--output', type=str,
                        metavar='file',
                        default='fibnonancci.txt',
                        help='Output resutl to a file (default: %(default)s)'
                        )
    # 2. Boolean
    parser.add_argument('-b', '--boolean',
                        help="it is boolean toogle '-t' to turn on",
                        action='store_true')
    # 3. Append
    parser.add_argument('-a', '--append',
                        metavar='list',
                        action='append',
                        help='Append the list')
    # 4. Choice
    parser.add_argument('-c', '--choice',
                        help='Choice one of the choice in the list',
                        choices=('choice1', 'choice2', 'choice3'))
    ##group## (Either one option can be happen)
    group.add_argument('-v', '--verbose',
                       help='Display log in console',
                       action='store_true')
    group.add_argument('-q', '--quiet',
                       help='Display final result in console',
                       action='store_true')

    args = parser.parse_args()

    result = fib(args.num)
    print('Boolean:' + str(args.boolean))
    if args.append:
        print('Append:' + str(args.append))
    if args.choice:
        print('Choice:' + str(args.choice))
    if args.verbose:
        print("The " + str(args.num) + "th fib number is " + str(result))
    elif args.quiet:
        print(result)
    else:
        print('Fib(' + str(args.num) + ') =' + str(result))

    if args.output != '':
        with open(args.output, 'a') as f:
            f.write(str(result) + '\n')


if __name__ == '__main__':
    Main()
