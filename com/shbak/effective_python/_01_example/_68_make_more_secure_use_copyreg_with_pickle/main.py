# pickle has a code that decode pickle
# pickle dumps current state
# state change (add or delete attribute etc)
# loads pickle
# assert object comparison -> that fail!!!
# make better
# use default attribute value and copyreg library to unpickle new version of object
# copyreg need helper function to pickle, copyreg is interceptor of pickle

import copyreg
import pickle

from termcolor import colored


class BetterGameState:
    test = 3

    def __init__(self, level=0, lives=4):  # , points=0, version=0):
        self.level = level
        self.lives = lives
        # self.points = points
        # self.version = version


def pickle_game_state(game_state):
    kwargs = game_state.__dict__
    return unpickle_game_state, (kwargs,)


def unpickle_game_state(kwargs):
    return BetterGameState(**kwargs)


def copyreg_pickle():
    copyreg.pickle(BetterGameState, pickle_game_state)


def pickle_gamestate():
    """ not auto make GameState attribute change(coding) when you want

    """
    state = BetterGameState()
    serialized = pickle.dumps(state)
    deserialized = pickle.loads(serialized)
    print(colored(f'serialized: {serialized}', 'green'))
    print(colored(f'deserialized.__dict__: {deserialized.__dict__}', 'green'))


_state_path = 'game_state.bin'


def dict_test(object):
    print(colored(f'object.__dict__: {object.__dict__}', 'green'))


def pickle_save_gamestate_file():
    state = BetterGameState()
    serialized = pickle.dumps(state)

    with open(_state_path, 'wb') as f:
        pickle.dump(state, f)
    print(colored(f'pickle load success...'))


def pickle_load_gamestate_file():
    with open(_state_path, 'rb') as f:
        state_after = pickle.load(f)

    print(colored(f'state_after: {state_after.__dict__}', 'green'))
    assert isinstance(state_after, BetterGameState)


if __name__ == '__main__':
    pickle_gamestate()
    pickle_save_gamestate_file()
    pickle_load_gamestate_file()
    obj = BetterGameState()
    dict_test(obj)
    print(colored(f'__dict__ did not return class instance ', 'yellow'))
