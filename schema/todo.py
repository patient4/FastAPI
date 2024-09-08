def todoEntity(todo) -> dict:
    """
    Converts a Todo object to a dictionary.

    Args:
        todo (dict): A dictionary representing a Todo item with keys 'subject', 'title', and 'description'.

    Returns:
        dict: A dictionary with the 'subject', 'title', and 'description' fields from the input Todo item.
    """
    # Extract and return the relevant fields from the todo dictionary
    return {
        "subject": todo.get("subject"),
        "title": todo.get("title"),
        "description": todo.get("description")
    }

def todosEntity(todos) -> list:
    """
    Converts a list of Todo objects to a list of dictionaries.

    Args:
        todos (list): A list of dictionaries, each representing a Todo item.

    Returns:
        list: A list of dictionaries, each containing the 'subject', 'title', and 'description' fields from each Todo item.
    """
    # Convert each Todo object in the list to a dictionary using todoEntity
    return [todoEntity(todo) for todo in todos]
