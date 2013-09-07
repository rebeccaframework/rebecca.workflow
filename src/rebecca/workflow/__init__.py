class Workflow(object):
    def __init__(self, name, attr="status"):
        self.name = name
        self.states = []
        self.transitions = []
        self.attr = attr

    def add_transition(self, name, from_state, to_state):
        transition = Transition(name, from_state, to_state)
        self.transitions.append(transition)

    def available_transitions(self, target):
        state = self.current_state(target)
        for trans in self.transitions:
            if trans.from_state == state:
                yield trans.name

    def add_state(self, name):
        state = State(name)
        self.states.append(state)

    def current_state(self, target):
        if not hasattr(target, self.attr):
            return None
        return getattr(target, self.attr)

    def initialize(self, target):
        setattr(target, self.attr, self.initial_state.name)

    @property
    def initial_state(self):
        return self.states[0]

    def to_state(self, target, state):
        c_state = self.current_state(target)
        for trans in self.transitions:
            if trans.from_state == c_state:
                if trans.to_state == state:
                    trans(target)
                    setattr(target, self.attr, trans.to_state)

    def update(self, values):
        self.states = []
        for state in values['states']:
            self.add_state(state)

        for trans in values['transitions']:
            self.add_transition(trans['name'], trans['from_state'], trans['to_state'])

class State(object):
    def __init__(self, name):
        self.name = name


class Transition(object):
    def __init__(self, name, from_state, to_state):
        self.name = name
        self.from_state = from_state
        self.to_state = to_state

    def __call__(self, target):
        pass