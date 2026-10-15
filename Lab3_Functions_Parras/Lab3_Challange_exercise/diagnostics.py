
def monitor(func):
    def wrapper(value):
        print("Checking:", value)
        return func(value)
    return wrapper


@monitor
def check_reading(value):
    if not isinstance(value, (int, float)):
        raise ValueError("Invalid telemetry reading")

    if value >= 20:
        return "ABNORMAL"
    return "NORMAL"


def trace_abnormal(n):
    if n <= 0:
        return "Trace complete"
    return trace_abnormal(n - 1)

