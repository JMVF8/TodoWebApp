defaultFilePath = "ToDos"

def getToDos(filePath = defaultFilePath):
    with open(filePath, "r") as file:
        toDoList = file.readlines()
    return toDoList

def setToDos(updatedToDos, filePath = defaultFilePath):
    with open(filePath, "w") as file:
        file.writelines(updatedToDos)