from graph import Graph
import copy

y = True
while (y):
    print("\n\t Work graph")
    print("1. creat empty graph")
    print("2. add node")
    print("3. add edge")
    print("4. remove node")
    print("5. remove edge")
    print("6. read json")
    print("7. write json")
    print("8. write console")
    print("9. write task")
    print("10. write exit")
    print("write items\n")
    n = int(input())

    if (n == 1):
        print("1.directed", "2.undirected")
        z = False
        x = input()
        if x == 1:
            z = True
        if x == 2:
            z = False
        g = Graph(z)
    elif (n == 2):
        print("Write node")
        a = input()
        g.add_Node(a)
    elif (n == 3):
        print("Write nodes")
        a = input()
        b = input()
        g.add_Edge(a, b)
    elif (n == 4):
        print("Write node")
        a = input()
        g.remove_Node(a)
    elif (n == 5):
        print("Write nodes")
        a = input()
        b = input()
        g.add_Edge(a, b)
    elif (n == 6):
        g.read_json()
    elif (n == 7):
        g.update_file()
    elif (n == 8):
        g.nice_print()
    elif (n == 9):
        print("task 1")
        print("write task")
        print("1", "2")
        x = int(input())
        if x == 1:
            (g.task1_la())
        if x == 2:
            (g.task2_la())

    elif (n == 10):
        print("exit")
        y = False
    else:
        print("ERROR")
