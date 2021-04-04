def format_name(f_name, l_name):
  if f_name == "" or l_name == "":
    return "Your parameters are not valid."
  f_name = f_name.title()
  l_name = l_name.title()
  return f"{f_name} {l_name}"

print(format_name("NICK","sardel"))

