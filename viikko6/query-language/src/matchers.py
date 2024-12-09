class QueryBuilder:
    def __init__(self):
        self._matchers = []
    
    def plays_in(self, team):
        self._matchers.append(PlaysIn(team))
        return self
    
    def has_at_least(self, value, attr):
        self._matchers.append(HasAtLeast(value, attr))
        return self
    
    def has_fewer_than(self, value, attr):
        self._matchers.append(HasFewerThan(value, attr))
        return self
    
    def build(self):
        return And(*self._matchers)


class And:
    def __init__(self, *matchers):
        self._matchers = matchers

    def test(self, player):
        for matcher in self._matchers:
            if not matcher.test(player):
                return False

        return True
    
class All:
    def test(self, player):
            return player
    
class Or:
    def __init__(self, *options):
        self._options=options

    def test(self, player):
        for option in self._options:
            if (self.option.test(player)):
                return player


class Not:
    def __init__(self, function):
        self._function = function

    def test(self, player):
            return not self._function.test(player)

class HasFewerThan:
    def __init__(self, value, attr):
        self._value = value
        self._attr = attr

    def test(self, player):
        player_value = getattr(player, self._attr)

        return player_value < self._value


class PlaysIn:
    def __init__(self, team):
        self._team = team

    def test(self, player):
        return player.team == self._team


class HasAtLeast:
    def __init__(self, value, attr):
        self._value = value
        self._attr = attr

    def test(self, player):
        player_value = getattr(player, self._attr)

        return player_value >= self._value
