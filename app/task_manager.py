
def add_task(tasks, title):
    """Add a new task to the task list."""

    if not title.strip():
        raise ValueError("Task title cannot be empty.")

    task = {
        "id": len(tasks) + 1,
        "title": title.strip(),
        "completed": False
    }

    tasks.append(task)

    return task


def get_tasks(tasks):
    """Return all available tasks."""

    return tasks
