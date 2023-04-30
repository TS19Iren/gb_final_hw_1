import argparse


class ArgumentParser:
    def __init__(self):
        self.parser = argparse.ArgumentParser(description='Notes CLI')
        self.parser.add_argument('command', choices=['add', 'read', 'update', 'delete'], help='Command to execute')
        self.parser.add_argument('--title', help='Note title')
        self.parser.add_argument('--body', help='Note body')
        self.parser.add_argument('--id', type=int, help='Note ID')
        self.parser.add_argument('--date', help='Date to filter notes by (YYYY-MM-DD)')

    def parse_args(self):
        return self.parser.parse_args()
