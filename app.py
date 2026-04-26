from flask import Flask, render_template, request, redirect

app = Flask(__name__)

tasks = []

@app.route('/')
def home():
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add_task():
    task = request.form.get('task')
    priority = request.form.get('priority')

    if task:
        tasks.append({
            "task": task,
            "priority": priority,
            "status": "Pending"
        })
    return redirect('/')

@app.route('/toggle/<int:index>')
def toggle_status(index):
    if index < len(tasks):
        if tasks[index]["status"] == "Pending":
            tasks[index]["status"] = "Done"
        else:
            tasks[index]["status"] = "Pending"
    return redirect('/')

@app.route('/delete/<int:index>')
def delete_task(index):
    if index < len(tasks):
        tasks.pop(index)
    return redirect('/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)