import yaml

class Action:
    def __init__(self, action):
        self.expect = action.get('expect')
        self.ignore = action.get('ignore', [])
        self.message = action.get('message')
        if 'time' in action:
            self.title = action.get('title', 'Timer')
            self.time = action.get('time')


class ActionsMapper:

    def __init__(self, config_file):
        self.actions = []
        with open(config_file, 'r') as stream:
            try:
                action_map = yaml.load(stream).items()
                for key,value in action_map:
                    print("DEBUG: %s=%s" % (key, value))
                    self.actions.append(Action(value))

            except yaml.YAMLError as exc:
                print(exc)

