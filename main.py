from graph import Graph

y = True
print("\n\t You need to initialize the graph")
while y:
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

    if n == 1:
        print("1.directed", "2.undirected")
        z = False
        x = input()
        if x == 1:
            z = True
        if x == 2:
            z = False
        g = Graph(z)
    elif n == 2:
        print("Write node")
        a = input()
        g.add_Node(a)
        print("Write weight")
        x = input()
        g.add_Weight(a, x)
    elif n == 3:
        print("Write nodes")
        a = input()
        b = input()
        g.add_Edge(a, b)
    elif n == 4:
        print("Write node")
        a = input()
        g.remove_Node(a)
    elif n == 5:
        print("Write nodes")
        a = input()
        b = input()
        g.remove_Edge(a, b)
    elif n == 6:
        g.read_json()
    elif n == 7:
        g.update_file()
    elif n == 8:
        g.nice_print()
    elif n == 9:
        print("1. write component (dfs)")
        print("2. write min cicle (bfs)")
        x = int(input())
        if x == 1:
            g.print_comp_Task5()
        elif x == 2:
            print("Write node")
            z = str(input())
            print(g.bfs(z))
        else:
            print("exit to menu")

    elif n == 10:
        print("exit")
        y = False
    else:
        print("ERROR")
