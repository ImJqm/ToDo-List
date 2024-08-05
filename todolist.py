import sys
todolist = []
with open('todolist.txt','r') as ra:
    i = ra.readlines()
    for line in i:
        if ("\n" in line):
            newline = line.rstrip("\n")
            todolist.append(newline[2:])
        else:
            todolist.append(line[2:])
#print(todolist)
print("---Current ToDo List---")
with open('todolist.txt','r') as reader:
    print(reader.read()) 
print()

with open('todolist.txt','r') as f:
    line_count =0
    for line in f:
        line_count+=1
while (True):
    try:
        print()
        decsicsion = int(input("What would you like to do?\n\n1)Print current ToDo List\n2)Add an item\n3)Remove an item\n4)Exit\n"))
        print()
        if (decsicsion ==1):
            print()
            print("---Current ToDo List---")
            with open('todolist.txt','r') as r:
                print(r.read())
            print()
            continue
        elif (decsicsion == 2): 
            print()
            item = input("Input the task you would like to add:")
            if (item in todolist):
                print()
                print("Item Already In List!")
                print()
                continue
            todolist.append(item)
            with open('todolist.txt','w') as w:
                for item1 in todolist:
                    w.write(str(todolist.index(item1)+1)+")" + item1+"\n")
            print()
            print(f'{item} added to TodoList')
            
            #print(todolist)
            continue
        elif (decsicsion==3):
            print()
            rmv = int(input("What is the number of the item you would like to remove?: "))
            todolist.remove(todolist[rmv-1])
            with open('todolist.txt','w') as writing:
                for lin in todolist:
                    writing.write(str(todolist.index(lin)+1)+")" + lin+"\n")
            print()
            print(f'Item #{rmv} removed from ToDo List')
            print()
        elif (decsicsion==4):
            sys.exit(0)
    except ValueError:
        print("Not a valid option")

