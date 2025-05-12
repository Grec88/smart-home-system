from flask import Flask, request, jsonify

app = Flask(__name__)

# Простой "ключ безопасности"
API_KEY = "12345"

# Хранилище задач в памяти (словари)
tasks = []
task_id_counter = 1

# Проверка API-ключа
def check_api_key():
    key = request.headers.get('Authorization')
    return key == API_KEY

# GET /tasks — получить все команды
@app.route('/tasks', methods=['GET'])
def get_tasks():
    if not check_api_key():
        return jsonify({"error": "Неверный API-ключ"}), 403
    return jsonify(tasks)

# POST /tasks — добавить команду
@app.route('/tasks', methods=['POST'])
def create_task():
    global task_id_counter
    if not check_api_key():
        return jsonify({"error": "Неверный API-ключ"}), 403
    data = request.get_json()
    task = {
        "id": task_id_counter,
        "device": data.get("device"),
        "command": data.get("command"),
        "time": data.get("time")
    }
    tasks.append(task)
    task_id_counter += 1
    return jsonify(task), 201

# DELETE /tasks/<id> — удалить команду
@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    if not check_api_key():
        return jsonify({"error": "Неверный API-ключ"}), 403
    global tasks
    tasks = [task for task in tasks if task["id"] != task_id]
    return jsonify({"message": "Команда удалена"}), 200

# Запуск приложения
if __name__ == '__main__':
    app.run(debug=True)
