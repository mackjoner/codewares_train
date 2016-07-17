"""
    Human readable duration format
    https://www.codewars.com/kata/human-readable-duration-format/python
"""


def format_duration(seconds):
    times = [("year", 365 * 24 * 60 * 60),
             ("day", 24 * 60 * 60),
             ("hour", 60 * 60),
             ("minute", 60),
             ("second", 1)]

    if not seconds:
        return "now"

    chunks = []
    for name, secs in times:
        qty = seconds // secs
        if qty:
            if qty > 1:
                name += "s"
            chunks.append(str(qty) + " " + name)

        seconds = seconds % secs

    return ', '.join(chunks[:-1]) + ' and ' + chunks[-1] if len(chunks) > 1 else chunks[0]


if __name__ == '__main__':
    print(format_duration(1) == "1 second")
    print(format_duration(62) == "1 minute and 2 seconds")
    print(format_duration(120) == "2 minutes")
    print(format_duration(3600) == "1 hour")
    print(format_duration(3662) == "1 hour, 1 minute and 2 seconds")
