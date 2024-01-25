from argparse import ArgumentParser

parser = ArgumentParser()

parser.add_argument('--output', '-o', required=True, help='Text to print out to the console (Required)')

args = parser.parse_args()

print(args.output)