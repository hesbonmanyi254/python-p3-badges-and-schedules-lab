# conference_badges.py

def batch_badge_creator(names):
    '''Create and return a list of badges for the given names.'''
    badges = []
    for name in names:
        badge = f"Hello, my name is {name}."
        badges.append(badge)
    return badges
