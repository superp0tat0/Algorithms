import sys
sys.setrecursionlimit(40000) 
#Perform a DFS search amone G start at index
#Label them with ordering t and store the ordering in variable labels
def DFS(G, index, explored):
    global labels
    global t
    explored.add(index)
    
    #If it is a one way pointer, mark it as finished then go back
    if(index not in G.keys()):
        return;
    
    for j in G[index]:
        if(j not in explored):
            DFS(G, j, explored)
    t+=1
    labels[index] = t
    return explored;

#Reverse the graph G
def reverse(G):
    new_dic = {}
    for key in G.keys():
        for item in G[key]:
            new_dic.setdefault(item, []).append(key)

    return new_dic

#Count how many variables in one DFS call
def DFS_count(G,index, explored=[], count=1):
    explored.add(index)
    #If it is a one way pointer, mark it as finished then go back
    if(index not in G.keys()):
        return (count, explored)
    
    for j in G[index]:
        if(j not in explored):
            count += 1
            count = DFS_count(G, j, explored, count)[0]
    return (count, explored)

#Update the graph with map_list
def update(G, map_list):
    new_dic = {}
    for key in G.keys():
        for item in G[key]:
            new_dic.setdefault(map_list[key], []).append(map_list[item])
    
    return new_dic


if(__name__ == "__main__"):
    labels = {}
    t = 0
    test = {1:[7], 2:[5],3:[9],4:[1],5:[8],6:[3,8],7:[9,4],8:[2],9:[6]}

    #Calculate the ordering on the reversed version
    for i in range(9, 0, -1):
        if(i not in labels.keys()):
            DFS(test,i,set(labels.keys()))


    #Update based on the ordering updated G, then calculate the size of SCCs
    test_rev = update(reverse(test), labels)
    rev_explored = set()
    total_amount = []

    for i in range(9, 0, -1):
        if(i not in rev_explored):
            (amount, exp) = DFS_count(test_rev, i, rev_explored)
            total_amount.append(amount)
            rev_explored = rev_explored|exp

    print(total_amount)

    #Read the data into test
    test = {}
    with open('data.txt', 'r') as f:
        x = f.read().splitlines()
    for value in x:
        head = value.split(" ")[0]
        tail = value.split(" ")[1]
        test.setdefault(int(head), []).append(int(tail))


    labels = {}
    t = 0
    for i in range(875714, 0, -1):
        if(i not in labels.keys()):
            DFS(test,i,set(labels.keys()))
    #Update based on the ordering updated G, then calculate the size of SCCs
    test_rev = update(reverse(test), labels)
    rev_explored = set()
    total_amount = []

    print("Started")
    for i in range(875714, 0, -1):
        if(i not in rev_explored):
            (amount, exp) = DFS_count(test_rev, i, rev_explored)
            total_amount.append(amount)
            rev_explored = rev_explored|exp

    print(total_amount)
    print("Finished")