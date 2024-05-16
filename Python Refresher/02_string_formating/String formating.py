name = "Bob"
greeting = f"Hello, {name}"

print(greeting)

name = "Rolf"

print(f"Hello, {name}")

#Template sttings with .format()

name = "Bob"
greeting = "Hello, {}" # Curly bracers will be replaced with the param inside .format()
with_name = greeting.format(name)
with_name_two = greeting.format('Rolf')
print(with_name)
print(with_name_two)

# USING LONGER PHRASES
longer_phrase = "Hello, {}. Today is {}"

formatted = longer_phrase.format("Ralf", "Monday")
print(formatted)
