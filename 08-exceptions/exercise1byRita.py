items = [13, 'string', 2.45, 0, "e", True, False, [], {'key': 3}, ()]
collected_errors = []

for i in items:
    try:
        result = 10 / i
    except (TypeError, ZeroDivisionError) as e:
        result = 0
        collected_errors.append(e)

    print(result)

for err in collected_errors:
    print(f'- {err}')