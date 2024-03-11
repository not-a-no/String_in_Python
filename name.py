name = "ada lovelace"

#A method is an actions that Python can perform on a piece of data
print(name.title())
print(name.upper())
print(name.lower())

#f-strings, f is for format
first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
print(full_name)

message = f"Hello, {full_name.title()}"
print(message)

#Adding Whitespace to Strings with Tabs or Newlines
print("Python")
print("\tPython")
print("Languages:\nPythong\n\tC\n\t\tJavaScript")

#Stripping Whitespace
#To ensure that no whitespace exists at the right side of a string
favorite_language = 'python '
print(favorite_language.rstrip())
#left side
favorite_language = ' python'
print(favorite_language.lstrip())
#both
favorite_language = ' python '
print(favorite_language.strip())

#Removing Prefixes
nostarch_url = 'https://nostarch.com'
print(nostarch_url.removeprefix('https://'))