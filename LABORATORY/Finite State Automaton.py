def ends_with_ab(s):
    state = 0
    for char in s:
        if state == 0:
            state = 1 if char == 'a' else 0
        elif state == 1:
            state = 2 if char == 'b' else 0
        elif state == 2:
            state = 1 if char == 'a' else 0
    return state == 2

print("xyzab ends with ab:", ends_with_ab("xyzab"))
print("xyza ends with ab:", ends_with_ab("xyza"))