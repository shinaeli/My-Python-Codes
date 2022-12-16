def subtract(x, y):
    try:
        return float(x) - float(y)
    except ValueError as e:
        return f'Invalid input: {e}.'