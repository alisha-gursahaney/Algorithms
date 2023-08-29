# Alisha Meena Gursahaney
# amg9zd

# Whiteboard collaboration with Addison Lowman
    # she helped explain to me how to use gb.ping instead of gb.board(playgame)

def playgame_dc(gb, left, right):
    # index of middle of array
    m = (left + right) // 2
    middle = gb.ping(m)
    subleft = gb.ping(m - 1)
    subright = gb.ping(m + 1)

    # Basecase
    answer = 2
    if(left == right):
        return left

    # base case to check if array size is 2
    # elif right == 1:
    #     if gb.ping(left) > gb.ping(right):
    #         return left
    #     else:
    #         return right
    # Divide

    else:
    # Conquer
        # then the middle is a trench
        if middle > subright and middle > subleft:
            return m

    # Combine
        # right side is larger, so recurse on right sublist
        elif subleft < subright:
            return playgame_dc(gb, m+1, right)

        # left side is larger, so recurse on left sublist
        else:
            return playgame_dc(gb, left, m)


