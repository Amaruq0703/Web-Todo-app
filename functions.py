#custom functions
filename = 'todos.txt'

def get_todos(filepath = filename):
     """ Accesses text file with saved todo list"""
     with open(filepath, 'r') as file_local:
          todos_local = file_local.readlines()
     return todos_local


def write_todos(todos_arg, filepath = filename):
     """ Writes todos list in specified text file """
     with open(filepath, 'w') as file:
                file.writelines(todos_arg)

if __name__ == '__main__':
     print('running functions directly')

  
     