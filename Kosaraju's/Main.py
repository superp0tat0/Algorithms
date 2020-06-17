from queue import LifoQueue
#Perform a DFS search amone G start at index
#Label them with ordering t and store the ordering in variable labels
def DFS(G, index, explored):
    global labels
    global t
    
    stack = LifoQueue(maxsize = 999999)# This stack track the DFS process
    order_stack = LifoQueue(maxsize = 999999)# This stack track the DFS ordering
    
    stack.put(index) #add element to stack
    order_stack.put(index)
    
    while(stack.empty() == False):
        current_index = stack.get()
        explored.add(current_index) #Visited
        all_neighbor_visited = True #Assume all beighbors of current index explored
        
        if(current_index in G.keys()): #This is a live node, with childrens
            for neighbor in G[current_index]:
                if(neighbor not in explored):
                    stack.put(neighbor)
                    order_stack.put(neighbor)
                    all_neighbor_visited = False
            
        if(all_neighbor_visited):
            t += 1
            labels[order_stack.get()] = t
    
    while(order_stack.empty() == False):
        t += 1
        labels[order_stack.get()] = t

    return explored;

#Reverse the graph G
def reverse(G):
    new_dic = {}
    for key in G.keys():
        for item in G[key]:
            new_dic.setdefault(item, []).append(key)

    return new_dic

#Count how many variables in one DFS call
def DFS_count(G, index, explored):
    
    original_size = len(explored)
    stack = LifoQueue(maxsize = 999999)# This stack track the DFS process
    stack.put(index) #add element to stack
    
    while(stack.empty() == False):
        current_index = stack.get()
        explored.add(current_index) #Visited
        
        if(current_index in G.keys()): #This is a live node, with childrens
            for neighbor in G[current_index]:
                if(neighbor not in explored):
                    stack.put(neighbor)

    return (len(explored) - original_size, explored)

#Update the graph with map_list
def update(G, map_list):
    new_dic = {}
    for key in G.keys():
        for item in G[key]:
            new_dic.setdefault(map_list[key], []).append(map_list[item])
    
    return new_dic

labels = {}
t = 0

#Test cases
#test = {1:[7], 2:[5],3:[9],4:[1],5:[8],6:[8,3],7:[9,4],8:[2],9:[6]} pass
#test = {1:[4], 2:[8],3:[6],4:[7],5:[2],6:[9],7:[1],8:[5,6],9:[7,3]} pass
#test = {1:[2], 2:[6,3,4],3:[1,4],4:[5],5:[4],6:[5,7],7:[6,8],8:[5,7]} pass
#test = {1:[2], 2:[3],3:[1,4],4:[],5:[4],6:[4,7],7:[8],8:[6]} pass
#test = {1:[2], 2:[3],3:[1,4],4:[3,6],5:[4],6:[4,7],7:[8],8:[6]} pass
test = {1:[2], 2:[3,4,5],3:[6],4:[5,7],5:[2,6,7],6:[3,8],7:[8,10],8:[7], 9:[7],10:[9,11],11:[12],12:[10]} #pass

#Calculate the ordering on the reversed version
for i in range(12, 0, -1):
    if(i not in labels.keys()):
        DFS(test,i, set(labels.keys()))
print(labels)

#Update based on the ordering updated G, then calculate the size of SCCs
test_rev = update(reverse(test), labels)
print(test_rev)
rev_explored = set()
total_amount = []


for i in range(12, 0, -1):
    if(i not in rev_explored):
        (amount, new_explored) = DFS_count(test_rev, i, rev_explored)
        total_amount.append(amount)
        rev_explored = new_explored

print(total_amount)

#Read the data into test
test = {}
with open('data.txt', 'r') as f:
    x = f.read().splitlines()
for value in x:
    head = value.split(" ")[0]
    tail = value.split(" ")[1]
    test.setdefault(int(head), []).append(int(tail))
print(test[100])

labels = {}
t = 0
test_rev = reverse(test)
print("Finished reversing the process")
#Calculate the ordering on the reversed version
for i in range(875714, 0, -1):
    if(i not in labels.keys()):
        DFS(test_rev,i, set(labels.keys()))
    if(i % 10000 == 1):
        print(i)

#Update based on the ordering updated G, then calculate the size of SCCs
test_new = update(test_rev, labels)
rev_explored = set()
total_amount = []
print("finished updating")

for i in range(875714, 0, -1):
    if(i not in rev_explored):
        (amount, new_explored) = DFS_count(test_new, i, rev_explored)
        total_amount.append(amount)
        rev_explored = new_explored
    if(i % 10000 == 1):
        print(i)

print(total_amount)