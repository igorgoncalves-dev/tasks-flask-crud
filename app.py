from flask import Flask, json, jsonify, request
from models.task import Task

app = Flask(__name__)
    
tasks = []
task_id_control = 1

@app.route('/tasks', methods=["POST"])
def create_task():
    global task_id_control # Define o uso da variável global

    data = request.get_json()

    new_task = Task(id=task_id_control, title=data["title"], description=data.get("description", ""))
    task_id_control += 1 # Incrementa o contador
    tasks.append(new_task)

    return jsonify({"message": "Nova tarefa criada com sucesso", "id": new_task.id})

@app.route('/tasks', methods=["GET"])
def get_tasks():
    
    task_list = [task.to_dict() for task in tasks]

    # Método verboso
    """
    task_list = []
    for task in tasks:
        print(task.to_dict())
        task_list.append(task.to_dict()) 
    """

    output = {
        "tasks": task_list,
        "total_tasks": len(task_list)
    }


    return jsonify(output)

@app.route('/tasks/<int:id>', methods=["GET"])
def get_task(id):
    task = None

    for task in tasks:
        if task.id == id:
            return jsonify(task.to_dict())
        
    return jsonify({"message": "Task não identificada"}), 404

@app.route('/tasks/<int:id>', methods=["PUT"])
def update_task(id):
    task = None

    for t in tasks:
        if t.id == id:
            task = t
            break


    if task == None:    
        return jsonify({"message": "Não foi possível alterar a task solicitada"}), 404
    
    data = request.get_json()
    
    task.title = data["title"]
    task.description = data["description"]
    task.completed = data["completed"]

    return jsonify({"message": "Tarefa atualizada com sucesso"})


@app.route('/tasks/<int:id>', methods=["DELETE"])
def delete_task(id):

    task = None

    for t in tasks:
        if t.id == id:
            task = t
            break

    if task == None:
        return jsonify({"message": "Task não encontrada"}), 404
    
    tasks.remove(task)

    return jsonify({"message": "Task removida com sucesso"})

if __name__ == "__main__":
    app.run(debug=True)