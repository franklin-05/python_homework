import logging

logger = logging.getLogger(__name__ + "_parameter_log")
logger.setLevel(logging.INFO)
logger.addHandler(logging.FileHandler("./decorator.log", "a"))


def logger_decorator(func):
    def wrapper(*args, **kwargs):
        pos_params = list(args) if args else "none"
        kw_params = kwargs if kwargs else "none"

        result = func(*args, **kwargs)

        logger.log(logging.INFO, f"function: {func.__name__}")
        logger.log(logging.INFO, f"positional parameters: {pos_params}")
        logger.log(logging.INFO, f"keyword parameters: {kw_params}")
        logger.log(logging.INFO, f"return: {result}")

        return result

    return wrapper


@logger_decorator
def hello_world():
    print("Hello, World!")


@logger_decorator
def check_args(*args):
    return True


@logger_decorator
def return_decorator(**kwargs):
    return logger_decorator


hello_world()
check_args(1, 2, 3)
return_decorator(a=1, b=2)

#task 2 
def type_converter(type_of_output):
    def decorator(func):
        def wrapper(*args, **kwargs):
            x = func(*args, **kwargs)
            return type_of_output(x)

        return wrapper

    return decorator


@type_converter(str)
def return_int():
    return 5


@type_converter(int)
def return_string():
    return "not a number"


y = return_int()
print(type(y).__name__)

try:
    y = return_string()
    print("shouldn't get here!")
except ValueError:
    print("can't convert that string to an integer!")

    