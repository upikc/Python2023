def find_largest_index(s, chars):
    indices = [s.find(char) for char in chars]
    valid_indices = [index for index in indices if index != -1]
    return max(valid_indices) if valid_indices else -1

string = "Это пример строки с разными символами."
characters = ["п", "с", "р"]
print(string[11])
print(string[12])
print(string[13])
largest_index = find_largest_index(string, characters)
print(f"Наибольший индекс символов {characters} в строке: {largest_index}")