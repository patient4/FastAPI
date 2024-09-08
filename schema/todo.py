def todoEntity(todo) -> dict:
    return {
        "subject": todo["subject"],
        "title": todo["title"],
        "description": todo["description"]
    }

def todosEntity(todos) -> list:
    return [todoEntity(todo) for todo in todos]