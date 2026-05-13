from week_5.python.task_meneger.utils import (
    show_menu, show_tesks,
    undone_tasks, done_tasks,
    high_prio, daily_summary)


def main():
    menu_printer = [
    None,
    show_tesks,
    undone_tasks,
    done_tasks,
    high_prio,
    daily_summary,
    show_menu,
    ]
    
    print(show_menu())

    user_choice = 6

    while user_choice != -1: 
        try:
            user_choice = int(input("enter your choice: "))
        except ValueError:
            print("please enter a numrical choice base on the menu")
        if 1 <= user_choice <= 6:
            print(menu_printer[user_choice]())
        else:
            user_choice = -1
            print("bye! see you soon...")

           

if __name__ == "__main__":
    main()