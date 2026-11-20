def records_to_dicts(records: list[tuple[str, str, str, int, float]]) -> list[dict[str, str | int | float]] :
    LOG_COLUMNS = ("timestamp", "method", "endpoint", "status", "latency_ms")

    dict_records = list(map(lambda row: dict(zip(LOG_COLUMNS, row)),records))

    return dict_records


def get_error_logs(logs: list[dict[str, str | int | float]]) -> list[dict[str, str | int | float]]:

    error_logs = list(filter(lambda l : l["status"] >= 400,logs))

    return error_logs







def calculate_avg_latency(logs: list[dict[str, str | int | float]]) -> float:

    if not logs:
        return 0.0

    latency_values = list(map(lambda d : d["latency_ms"], logs))

    return round(sum(latency_values) / len(latency_values),2)

d = [('2026-11-19T09:00:01', 'GET', '/api/v1/health', 200, 12.4), ('2026-11-19T09:01:15', 'POST', '/api/v1/login', 200, 145.0), ('2026-11-19T09:02:30', 'POST', '/api/v1/login', 401, 88.2), ('2026-11-19T09:03:10', 'GET', '/api/v1/users', 200, 310.5), ('2026-11-19T09:05:00', 'GET', '/api/v1/orders', 500, 640.8), ('2026-11-19T09:06:22', 'PUT', '/api/v1/users', 200, 190.0), ('2026-11-19T09:07:45', 'GET', '/api/v1/products', 200, 95.3), ('2026-11-19T09:08:12', 'DELETE', '/api/v1/orders', 403, 42.1), ('2026-11-19T09:10:18', 'GET', '/api/v1/reports', 200, 480.2), ('2026-11-19T09:11:05', 'POST', '/api/v1/orders', 201, 215.6)]

dict_vals = records_to_dicts(d)
info = get_error_logs(dict_vals)
print(info)
print("\n")
print(calculate_avg_latency(dict_vals))