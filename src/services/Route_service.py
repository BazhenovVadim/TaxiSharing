import zipfile
import os
from fastkml import kml
import networkx as nx
from geopy.distance import geodesic

def extract_kmz_to_kml(kmz_path, output_dir):
    with zipfile.ZipFile(kmz_path, 'r') as kmz:
        kmz.extractall(output_dir)


# Распаковка файла
kmz_file = r"C:\Users\Вадим\PycharmProjects\TaxiSharing\2024 хакатон.kmz"
output_folder = r"C:\Users\Вадим\PycharmProjects\TaxiSharing\Unpack_kmz"
extract_kmz_to_kml(kmz_file, output_folder)

print(f"KMZ файл распакован в папку: {output_folder}")


def parse_kml(file_path):
    with open(file_path, 'rt', encoding='utf-8') as file:
        kml_data = file.read()

        k = kml.KML()
        k.from_string(kml_data)
        coordinates = []

        # Проходим по всем элементам в KML
        for feature in k.features:  # Получаем верхний уровень
            if hasattr(feature, 'features'):  # Проверяем, есть ли вложенные элементы
                for subfeature in feature.features:  # Обрабатываем вложенные элементы
                    if hasattr(subfeature, 'geometry') and subfeature.geometry:
                        coords = list(subfeature.geometry.coords)
                        coordinates.extend(coords)

        return coordinates


# Укажите путь к KML файлу
kml_file = r"C:\Users\Вадим\PycharmProjects\TaxiSharing\Unpack_kmz\doc.kml"
river_coordinates = parse_kml(kml_file)

print(f"Извлечено {len(river_coordinates)} координат реки.")

def create_river_graph(river_coords):
    G = nx.Graph()

    # Добавляем координаты как узлы и соединяем последовательные точки
    for i in range(len(river_coords) - 1):
        point_a = river_coords[i]
        point_b = river_coords[i + 1]
        distance = geodesic(point_a, point_b).meters  # Расстояние между точками
        G.add_edge(point_a, point_b, weight=distance)

    return G

# Создаем граф реки
river_graph = create_river_graph(river_coordinates)

# Найдем маршрут от начальной до конечной точки
start_point = river_coordinates[0]  # Замените на вашу начальную точку
end_point = river_coordinates[-1]  # Замените на вашу конечную точку

shortest_path = nx.shortest_path(river_graph, source=start_point, target=end_point, weight='weight')
path_length = nx.shortest_path_length(river_graph, source=start_point, target=end_point, weight='weight')

print(f"Кратчайший путь: {shortest_path}")
print(f"Длина пути: {path_length} метров")