import argparse


class ProgParams:

    def __init__(self):

        # Criação do objeto ArgumentParser
        parser = argparse.ArgumentParser(
            description="Just an example",
            formatter_class=argparse.ArgumentDefaultsHelpFormatter
            )

        # Adição dos argumentos opcionais
        parser.add_argument(
            "-rp", "--random-play", action='store_true', help="random play")

        self.args = parser.parse_args()

    def print_args(self):
        print("vars(args):\n", vars(self.args))

    def get_param_random_play(self):
        _rp = self.args.random_play
        return False if _rp is None or _rp is False else True
