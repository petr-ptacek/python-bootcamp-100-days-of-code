# Functions with outputs
def format_name(f_name: str, l_name: str) -> str:
    if not f_name or not l_name:
        return ""

    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()

    return f"{formatted_f_name} {formatted_l_name}"


formatted_str = format_name("Petr", "PTACEK")

print(formatted_str)
