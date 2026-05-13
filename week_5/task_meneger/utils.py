from tasks import TASKS


def show_menu():
    return """
    =========================================
    || for prsenting all tasks enter 1: \n
    || for amount of not done tasks enter 2: \n
    || for amount of complited tasks enter 3: \n
    || for high priority tasks enter 4: \n
    || for day summary enter 5: \n
    || see menu agein enter 6: \n
    || for exit enter any other number: \n
    =========================================
    """


def show_tesks():
    all_tasks = ''
    lst_size = len(TASKS['name'])
    for i in range(lst_size):
        all_tasks += f"[{i}] task name: {TASKS['name'][i]}. \t"
        all_tasks += f"priority: {TASKS['priority'][i] }. \t"
        all_tasks += "status: completed.\n" if TASKS['done'][i] else "status: not completed.\n"
    return all_tasks


def done_tasks():
    return sum(TASKS["done"])


def undone_tasks():
    return len(TASKS["done"]) - done_tasks()


def high_prio():
    count = 0
    for i in range(len(TASKS['name'])):
        if TASKS['priority'][i] == 'high':
            count += 1
    return count


def daily_summary():
    return f"""
    --------------------
    | Total tasks: {len(TASKS['name'])}\n
    | Not done tasks: {undone_tasks()}\n 
    | Completed tesks: {done_tasks()}\n
    | High priority: {high_prio()}\n
     --------------------
    """

