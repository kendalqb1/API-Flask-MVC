from app import app
from controllers import addTasks, deleteTask, getTasks, updateTask

@app.route('/tasks', methods = ['GET'])
def taskGet():
    return getTasks()

@app.route('/tasks', methods = ['POST'])
def taskPost():
    return addTasks()

@app.route('/tasks/<int:task_id>', methods = ['DELETE'])
def taskDelete(task_id):
    return deleteTask(task_id)

@app.route('/tasks/<int:task_id>', methods = ['PUT'])
def taskPut(task_id):
    return updateTask(task_id)