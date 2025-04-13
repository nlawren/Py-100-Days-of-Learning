# Task 75 - Docstrings


def format_name(f_name, l_name):
    """Function to take a first and last name and return a title case version of both."""
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"


formatted_name = format_name("AnGeLa", "YU")

print(f"The title case formatted name is {formatted_name}")
