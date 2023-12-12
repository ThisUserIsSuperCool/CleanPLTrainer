"""
Simple code to show how to incorporate task_plm with method_plm

Aim:
obj = task_method_class(
    task=taskA,
    method=methodB,
)(param_to_pass)
"""

class base:
    def __init__(self):
        super().__init__()
        print('init base')

class taskA(base):
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
    """
    parent = (method, task)
    cls_name = '_'.join([p.name() for p in parent])

    name_attr = dict(name=lambda self: cls_name)
    attr.update(name_attr)
    
    return type(cls_name, parent, attr)

obj = task_method_class(
    task=taskA,
    method=methodB,
)() 

print(obj.name())
print(obj.__class__.__bases__)
print(obj.__class__.__name__)