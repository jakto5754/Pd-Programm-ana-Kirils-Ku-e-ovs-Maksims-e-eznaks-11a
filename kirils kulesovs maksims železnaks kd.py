name = input("Ievadiet savu vārdu: ")
print(f"Labdien, {name}!")
numbers = []

print("Ievadiet piecus skaitļus pa vienam: ")
for i in range(5):
    while True:
        try:
            number = float(input(f"Ievadiet skaitļus {i + 1}"))
            numbers.append(number)
            break
        except ValueError:
            print("Ludzu, ievadiet normalu skaitļu!")
        
print(f"Jūsu sākotnējais saraksts: {numbers}")

sorted_numbers = sorted(numbers)
print(f"Sakārtots saraksts: {sorted_numbers}")

average = sum(numbers) / len(numbers)
print(f"Vidējā vērtība: {average:.1f}")
