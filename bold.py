def to_bold(text):
  """Converts a given string to bold text using ANSI escape codes."""
  BOLD_START = "\033[1m"
  BOLD_END = "\033[0m"
  return f"{BOLD_START}{text}{BOLD_END}"

# Example usage:
normal_text = "This is normal text."
bold_text = to_bold("This is bold text.")
combined_text = f"Here is some {to_bold('important')} information."

print(normal_text)
print(bold_text)
print(combined_text)