s
"""Helper functions for training"""

import datetime
import platform

from tqdm import tqdm


def name_experiment(prefix="", suffix=""):
    experiment_name = datetime.datetime.now().strftime('%b%d_%H-%M-%S_') + platform.node()
    if prefix is not None and prefix != '':
        experiment_name = prefix + '_' + experiment_name
    if suffix is not None and suffix != '':
        experiment_name = experiment_name + '_' + suffix
    return experiment_name


class Progressbar():
    """Progress Bar"""

    def __init__(self):
        self.p = None

    def __call__(self, iterable, length):
        self.p = tqdm(iterable, total=length)
        return self.p

    def say(self, **kwargs):
        if self.p is not None:
            self.p.set_postfix(**kwargs)
