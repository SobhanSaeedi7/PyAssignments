def make_tree(tree_high=5, leaves='🐍'):
    for i in range(tree_high+1):
        if i == 0:
            print(tree_high*' ', '🌟')
        else:
            print((tree_high-i+1)*' ',i*'🐍')
    print((tree_high)*' ', '🚪')
    print('Merry Christmas')

make_tree()
