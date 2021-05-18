import json
import os


def get_env(env):
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../env/", f"{env}_env.json")
    with open(path) as f:
        return json.load(f)


class EnvStarter:
    def __init__(self, env="test"):
        self.env = get_env(env)
