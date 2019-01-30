print('Main menu\n\n'
      ''
      '0. Exit the program.\n'
      '1. Display the to-do list.\n'
      '2. Add item to to-do list.\n'
      '3. Remove item from to-do list.')

tasks_array = list()
val = int(input("Enter a choice: "))

while ( val  != 0 ):

        if (val == 1):
            print('To-do List:\n')
            if not(len(tasks_array) == 0):
              for x in range(len(tasks_array)):
                print(x,end="" +'. '+ tasks_array[x]+"\n")
               
        elif (val == 2):
            task = (input("Add Task: "))
            tasks_array.append(task)
            print("The task \""+task+"\" has been added.")
        elif (val == 3):
            if (len(tasks_array) == 0):
                print("The list is empty, nothing to delete.")
            else:
                for x in range(len(tasks_array)):
                    print(x,end="" +'. '+ tasks_array[x]+"\n")
                val = int(input("which task you want to delete: "))
                while (val > len(tasks_array) or (val < 0)):
                    print("task does not exit")
                    val = int(input("which task you want to delete: "))
                else:
                    print("The task \"" + tasks_array[val] +  "\" has been deleted")
                    tasks_array.remove(tasks_array[val])
        else:
            print("Invalid option")


        print('Main menu\n\n'
              ''
              '0. Exit the program.\n'
              '1. Display the to-do list.\n'
              '2. Add item to to-do list.\n'
              '3. Remove item from to-do list.')
        val = int(input("Enter a choice: "))

