from app.task_manager import add_task, complete_task, get_tasks


def test_add_task():
    tasks = []

    task = add_task(tasks, "Learn Python")

    assert task == {
        "id": 1,
        "title": "Learn Python",
        "completed": False
    }

    assert len(tasks) == 1


def test_add_task_removes_extra_spaces():
    tasks = []

    task = add_task(tasks, "  Learn Python  ")

    assert task["title"] == "Learn Python"


def test_add_task_rejects_empty_title():
    tasks = []

    try:
        add_task(tasks, "   ")
        assert False, "Expected ValueError for an empty task title"
    except ValueError as error:
        assert str(error) == "Task title cannot be empty."


def test_get_tasks():
    tasks = [
        {
            "id": 1,
            "title": "Learn Python",
            "completed": False
        }
    ]

    result = get_tasks(tasks)

    assert result == tasks

def test_complete_task():
    tasks = [
        {"id": 1, "title": "Learn Python", "completed": False}
    ]

    task = complete_task(tasks, 1)

    assert task["completed"] is True


def test_complete_task_with_invalid_id():
    tasks = []

    try:
        complete_task(tasks, 99)
        assert False, "Expected ValueError for an invalid task ID"
    except ValueError as error:
        assert str(error) == "Task not found."