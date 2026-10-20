
def validate_task_title(title):
    if not isinstance(title, str):
        return False

    title = title.strip()

    if not title or len(title) > 100:
        return False

    return True
