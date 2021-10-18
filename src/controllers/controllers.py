from flask import jsonify, request
import random, string
from models.tasks import tasks

def getTasks():
    return jsonify( {'tasks': tasks} )

def addTasks():
    new_task = {
        'id': generateID(),
        'title': request.json['title'],
        'description': request.json['description']
    }
    tasks.append(new_task)
    return jsonify( {'tasks': tasks} )

def deleteTask(task_id):
    taskFound = [ task for task in tasks if task['id'] == task_id ]
    if len(taskFound) > 0:
        tasks.remove(taskFound[0])
        return ({
            'message': 'Task Remove',
            'tasks': tasks
        })
    return ({ 'message': 'Task not found' })

def updateTask(task_id):
    taskFound = [ task for task in tasks if task['id'] == task_id ]
    if len(taskFound) > 0:
        taskFound[0]['title'] = request.json['title']
        taskFound[0]['description'] = request.json['description']
        return ({
            'message': 'Task Update',
            'task': taskFound[0]
        })
    return ({ 'message': 'Task not found' }) 

def generateID():
    length = 6
    return ''.join(random.choice(string.ascii_uppercase) for i in range(length))