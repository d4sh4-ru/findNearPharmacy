from flask import Flask, request, jsonify
import csv
import math

app = Flask(__name__)

# Функция для вычисления расстояния между двумя точками (в километрах)
def haversine(lat1, lon1, lat2, lon2):
    R = 6371  # Радиус Земли в километрах
    lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = math.sin(dlat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return R * c

# Чтение данных из CSV
pharmacies = []
data_file = "data/pharmacyGEO.csv"
try:
    with open(data_file, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            pharmacies.append({
                "name": row["Name"],
                "lat": float(row["Latitude"]),
                "lon": float(row["Longitude"])
            })
except FileNotFoundError:
    print(f"Файл {data_file} не найден. Убедитесь, что файл существует.")

# API метод для поиска пяти ближайших аптек
@app.route('/nearest_pharmacies', methods=['GET'])
def nearest_pharmacies():
    try:
        lat = float(request.args.get('lat'))
        lon = float(request.args.get('lon'))
    except (TypeError, ValueError):
        return jsonify({"error": "Некорректные координаты. Укажите lat и lon как числа."}), 400

    if not pharmacies:
        return jsonify({"error": "Данные о аптеках отсутствуют."}), 500

    # Вычисляем расстояния до всех аптек
    distances = [
        {
            "name": p["name"],
            "lat": p["lat"],
            "lon": p["lon"],
            "distance": haversine(lat, lon, p["lat"], p["lon"])
        }
        for p in pharmacies
    ]

    # Убираем дубли по названию и сортируем по расстоянию
    unique_pharmacies = {}
    for entry in distances:
        if entry["name"] not in unique_pharmacies or unique_pharmacies[entry["name"]]["distance"] > entry["distance"]:
            unique_pharmacies[entry["name"]] = entry

    sorted_pharmacies = sorted(unique_pharmacies.values(), key=lambda x: x["distance"])[:5]

    # Формируем результат
    result = [
        {
            "name": p["name"],
            "latitude": p["lat"],
            "longitude": p["lon"],
            "distance_km": round(p["distance"], 2)
        }
        for p in sorted_pharmacies
    ]

    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
