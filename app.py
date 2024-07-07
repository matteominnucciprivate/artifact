from flask import Flask, render_template, request, redirect
from datetime import datetime

app = Flask(__name__)

# Example data structure for tasks
tasks = []

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        content = request.form.get("content")
        if content:
            tasks.append({"id": len(tasks) + 1, "content": content, "date_created": datetime.now()})
        return redirect("/")
    return render_template("update.html", tasks=tasks)

@app.route("/delete/<int:id>")
def delete(id):
    global tasks
    tasks = [task for task in tasks if task["id"] != id]
    return redirect("/")

@app.route("/update/<int:id>", methods=["GET", "POST"])
def update(id):
    task = next((task for task in tasks if task["id"] == id), None)
    if request.method == "POST":
        content = request.form.get("content")
        if content:
            task["content"] = content
        return redirect("/")
    return render_template("update.html", task=task)

if __name__ == "__main__":
    app.run(debug=True)
    
import os
print("Current Working Directory:", os.getcwd())
print("Template Path:", os.path.join(os.getcwd(), 'templates', 'update.html'))