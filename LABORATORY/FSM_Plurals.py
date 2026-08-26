def make_plural(noun):
    if noun.endswith(('s', 'x', 'z', 'ch', 'sh')):
        return noun + 'es'
    elif noun.endswith('y') and noun[-2] not in 'aeiou':
        return noun[:-1] + 'ies'
    return noun + 's'

print("Plural of cat:", make_plural("cat"))
print("Plural of box:", make_plural("box"))
print("Plural of fly:", make_plural("fly"))