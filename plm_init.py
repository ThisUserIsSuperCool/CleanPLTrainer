# simple code to show how to utilize incorporate task_plm with method_plm

class taskA:
    def __init__(self):
        super().__init__()
        print('init A')
    
    def a(self):
        print('hi, A')
    
    @classmethod
    def name(cls):
        return 'taskA'

class methodB:
    def __init__(self):
        super().__init__()
        print('init B')
    
    def b(self):
        print('hi, B')
    
    @classmethod
    def name(cls):
        return 'methodB'

def task_method_class(task,method, attr={}):
    """
    create a class with task and method as parent.

    inheritance order: task -> method, i.e. task is the parent of method.
    """
    parent = (task, method)
    cls_name = '_'.join([p.name() for p in parent][::-1])
    return type(cls_name, parent, attr)

obj = task_method_class(
    task=taskA,
    method=methodB,
)() 