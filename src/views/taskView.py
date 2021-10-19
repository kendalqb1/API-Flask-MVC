from app import app
from controllers.taskController import addTasks, deleteTask, getTasks, updateTask

@app.route('/')
def mainPage():
    return '<h1>App Flask</h1>'

@app.route('/tasks', methods = ['GET'])
def taskGet():
    return getTasks()

@app.route('/tasks', methods = ['POST'])
def taskPost():
    return addTasks()

@app.route('/tasks/<string:task_id>', methods = ['DELETE'])
def taskDelete(task_id):
    return deleteTask(task_id)

@app.route('/tasks/<string:task_id>', methods = ['PUT'])
def taskPut(task_id):
    return updateTask(task_id)