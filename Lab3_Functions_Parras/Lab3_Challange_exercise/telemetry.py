
def generate_telemetry(LAST_NAME, SEED_NUM, FAVORITE_ARTIST):
    base = len(LAST_NAME) + SEED_NUM + len(FAVORITE_ARTIST)

    for i in range(1, 11):
        if i == 5:
            yield "INVALID"
        else:
            yield (base + i * 4) % 31


