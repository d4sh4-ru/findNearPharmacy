import csv
import overpy

# Создаем объект API
api = overpy.Overpass()

# Запрос для поиска аптек в Кирове
query = """
[out:json];
area[name="Киров"]->.searchArea;
node["amenity"="pharmacy"](area.searchArea);
out body;
"""

# Выполнение запроса
result = api.query(query)

# Путь для сохранения CSV файла
output_file = "data/pharmacyGEO.csv"

# Убедимся, что директория существует
import os
os.makedirs(os.path.dirname(output_file), exist_ok=True)

# Запись данных в CSV
with open(output_file, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    # Заголовки
    writer.writerow(["Name", "Latitude", "Longitude"])

    for node in result.nodes:
        # Получаем название и координаты
        name = node.tags.get("name", "Unknown")
        lat = node.lat
        lon = node.lon

        # Проверка координат на принадлежность к Кирову (lat начинается с 58, lon с 49)
        if str(int(lat)).startswith("58") and str(int(lon)).startswith("49"):
            writer.writerow([name, lat, lon])

print(f"Данные сохранены в {output_file}")
