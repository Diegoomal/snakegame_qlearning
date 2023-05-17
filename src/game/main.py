import numpy as np

from prog_params import ProgParams
from game import Game


if __name__ == "__main__":

    np.random.seed(42)

    flg_random_play = ProgParams().get_param_random_play()

    Game().run(random_play=flg_random_play)
