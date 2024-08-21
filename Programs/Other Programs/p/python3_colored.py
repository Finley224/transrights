# This program uses ANSI escape codes to color the word trans the trans flag colors.
# Define the escape codes the program uses
blue = "\033[34;49m"
magenta = "\033[35;49m"
white = "\033[37;49m"
resetColors = "\033[39;49m"

# Format the output string with colors using a f-string
# https://docs.python.org/3/tutorial/inputoutput.html#tut-f-strings
output = f"{blue}T{magenta}r{white}a{magenta}n{blue}s{resetColors} Rights"

print(output)