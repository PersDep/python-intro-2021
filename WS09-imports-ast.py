import os
from ast import literal_eval

os.chdir('..')

# data = eval(input())
# data = literal_eval(input())
# print(data)
# print(type(data))

file = open("bstree_with_mean.py")
# print(file.read())
# for line in file:
#     eval(line)
file.close()

# import sys
# sys.path.append('..')
# print(sys.path)
# import bstree_with_mean
#
# tree = bstree_with_mean.BinarySearchTree()
# tree.insert(100)
# tree.insert(7)
# tree.insert(1000)
# tree.insert(10000)
# tree.insert(-100)
# print(tree)
# print()
# print(tree.mean())
# tree.delete(5)
# print(tree)
# print()
# print(tree.mean())

# import world
#
# print(world)
#
# print(world.africa)
#
# # print(world.europe)
#
# from world import europe
#
# print(world.europe)
#
# print(europe.greece)
#
# # print(world.europe.sweden)
#
# # print(europe.spain)
#
# import world.europe.spain
#
# print(europe.spain)
#
# from world.europe import sweden
#
# print(sweden)
#
# # print(world.africa.zimbabwe)
#
# from world.africa import zimbabwe
#
# print(zimbabwe)
#
# from world import africa
#
# print(africa.zimbabwe)
