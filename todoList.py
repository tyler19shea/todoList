def show_menu():
    print('Input option')
    print('1.) View List')
    print('2.) Check off the list')
    print('3.) Add to the list')
    print('4.) Exit')

def viewList(lst):
    print('*****************')
    with open(lst, 'r') as file:
        file.seek(0)
        for id, line in enumerate(file, start=1):
            print(f'{id}: {line.strip()}')
    print('*****************')

def checkOff(lst):
    viewList(lst)
    check = input('Which item do you want to check off: ') + '\n'
    try:
        with open(lst, 'r') as file:
            file.seek(0)
            lines = file.readlines()
        with open(lst, 'w') as file:
            file.seek(0)
            if check not in lines:
                print('NO TASK WITH THAT NAME (check spaces)')
            for line in lines:
                if check != line:
                    file.write(line)    
    except FileNotFoundError:
        print(f'The file {lst} does not exist')

def addList(lst):
    while True:
        task = input('Input a task to complete (x to exit): ').lower()
        if task == 'x':
            break
        else:
            with open(lst, 'a') as file:
                file.write(task + '\n')
            another = input('Would you like to add another one (y/n): ').lower()
            if another == 'y':
                continue
            elif another == 'n':
                break
            else:
                print('Invalid input')

def main():
    todolist = './mytodo.txt'
    while True:
        show_menu()
        choice = int(input('Please select an option: '))
        if choice in [1, 2, 3]:
            if choice == 1:
                viewList(todolist)
            elif choice == 2:
                checkOff(todolist)
                viewList(todolist)
            elif choice == 3:
                addList(todolist)
        elif choice == 4:
            print('Goodbye. Thank you!')
            break
        else:
            print('Please provide valid input')

main()