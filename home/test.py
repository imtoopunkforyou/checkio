def left_join(phrases: tuple) -> str:
    new_str = phrases.split(',')
    return new_str

print(left_join(("bright aright", "ok")))