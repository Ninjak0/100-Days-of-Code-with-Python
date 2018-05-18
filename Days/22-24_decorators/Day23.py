from functools import wraps

def make_html(element):
    def tags_decorator(func):
        @wraps(element)
        def func_wrapper(*args, **kwargs):
            return f"<{element}>{func(*args, **kwargs)}</{element}>"
        return func_wrapper
    return tags_decorator

@make_html('p')
@make_html('strong')
def get_text(text="I code with PyBites"):
    return text

print(get_text())


