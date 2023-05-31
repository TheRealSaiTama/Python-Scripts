from randfacts import get_fact

#fact = randfacts.get_fact()

print("Fact of the moment:",get_fact(filter_enabled=False))
print("Stay Silent with these facts:",get_fact(only_unsafe=True))