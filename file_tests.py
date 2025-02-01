from HW_30 import JsonFile, TxtFile, CsvFile

if __name__ == "__main__":
    # Тесты для JsonFile
    json_file = JsonFile("test.json")
    json_file.write({"name": "Vadim Kozlov", "age": 35})
    print(f"Данные из JSON файла: {json_file.read()}")
    json_file.append({"city": "Penza"})
    print(f"Данные после добавления в JSON файл: {json_file.read()}")

    # Тесты для TxtFile
    txt_file = TxtFile("test.txt")
    txt_file.write("Hello, world!")
    print(f"Данные из TXT файла: {txt_file.read()}")
    txt_file.append("\nThis is a new line.")
    print(f"Данные после добавления в TXT файл: {txt_file.read()}")

    # Тесты для CsvFile
    csv_file = CsvFile("test.csv")
    csv_file.write([["Name", "Age"], ["Alla", "25"], ["Sergey", "30"]])
    print(f"Данные из CSV файла: {csv_file.read()}")
    csv_file.append([["Margo", "35"]])
    print(f"Данные после добавления в CSV файл: {csv_file.read()}")