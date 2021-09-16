import argparse

def Main():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest='command')
    subparsers.required= True

    status_parser = subparsers.add_parser('status',
                                          help='Show status')
    status_parser.add_argument('-f', '--force',
                           action='store_true')

    checkout_parser = subparsers.add_parser('checkout',
                                            help='show checkout')
    checkout_parser.add_argument('-v','--verbose',
                             action='count')

    args=parser.parse_args()
if __name__ == '__main__':
    Main()