# Nearest Pharmacy API

Этот проект представляет собой API на основе Flask, который помогает найти пять ближайших аптек с уникальными названиями к указанным координатам.

## Функции

- Вычисление расстояний с использованием формулы Хаверсина.
- Чтение данных аптек из CSV-файла.
- Возврат до пяти ближайших уникальных аптек, отсортированных по расстоянию.

## Требования

- Python 3.8+
- Flask
- overpy

## Установка

1. Клонируйте этот репозиторий:
  
  ```bash
  git clone <repository_url>
  cd <repository_name>
  ```
  
2. Создайте и активируйте виртуальную среду:
  
  ```bash
  python -m venv venv
  source venv/bin/activate  # На Windows: venv\Scripts\activate
  ```
  
3. Установите зависимости:
  
  ```bash
  pip install -r requirements.txt
  ```
  
4. С помощью `savePharmacyGeo` выгрузите аптеки вашего города (или сразу всегом мира). CSV-файл использует следующую структуру:
  
  ```csv
  Name,Latitude,Longitude
  Pharmacy 1,58.5902,49.6723
  Pharmacy 2,58.5910,49.6700
  ```
  

## Использование

1. Запустите сервер Flask:
  
  ```bash
  python nearest_pharmacy_api.py
  ```
  
2. Доступ к API-конечной точке:
  
  - Конечная точка: `/nearest_pharmacies`
  - Метод: `GET`
  - Параметры запроса:
    - `lat`: Широта местоположения.
    - `lon`: Долгота местоположения.
3. Пример запроса:
  
  ```bash
  curl "http://127.0.0.1:5000/nearest_pharmacies?lat=58.5902&lon=49.6723"
  ```
  
4. Пример ответа:
  
  ```json
  [
      {
          "name": "Pharmacy 1",
          "latitude": 58.5901,
          "longitude": 49.6720,
          "distance_km": 0.25
      },
      {
          "name": "Pharmacy 2",
          "latitude": 58.5910,
          "longitude": 49.6700,
          "distance_km": 0.50
      }
  ]
  ```
  

## Структура файлов

```
.
├── nearest_pharmacy_api.py  # Основной скрипт API
├── data
│   └── pharmacyGEO.csv     # CSV-файл с данными аптек
└── README.md               # Документация проекта
```

## Лицензия

Этот проект лицензирован под лицензией MIT. Подробности см. в файле LICENSE.