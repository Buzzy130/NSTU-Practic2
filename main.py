import io
import sys
import folium
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtCore import QUrl
from Transport_routing import Ui_MainWindow
import matplotlib.pyplot as plt
import numpy as np
import random
import time
from folium.plugins import MousePosition

# Method for finding feasible routes with tabu search
def find_feasible_routes(depot, locations, centroids, labels, Q, Q_delivery, time_windows, tabu_size=5):
    routes = []
    visited = set()

    for i, centroid in enumerate(centroids):
        route = [depot[0]]
        current_location = depot[0]
        current_capacity = Q
        current_time = 8  # Assume starting at 8 AM

        tabu_list = []

        while True:
            min_distance = float('inf')
            next_location = None
            next_index = None

            for j, location in enumerate(locations):
                if labels[j] != i or location in visited or location in tabu_list:
                    continue

                if Q_delivery[j] > current_capacity:
                    continue

                distance = np.linalg.norm(np.array(current_location) - np.array(location))
                travel_time = distance / 60  # Assume speed of 60 km/h
                arrival_time = current_time + travel_time

                # If the vehicle arrives early, it should wait
                if arrival_time < time_windows[j][0]:
                    arrival_time = time_windows[j][0]

                if time_windows[j][0] <= arrival_time <= time_windows[j][1] and distance < min_distance:
                    min_distance = distance
                    next_location = location
                    next_index = j

            if next_location is None:
                break

            route.append(next_location)
            visited.add(next_location)
            current_location = next_location
            current_capacity -= Q_delivery[next_index]
            travel_time = np.linalg.norm(np.array(route[-2]) - np.array(route[-1])) / 60  # Fixed travel time calculation
            current_time += travel_time

            # If the vehicle arrives early, it waits until the time window opens
            if current_time < time_windows[next_index][0]:
                current_time = time_windows[next_index][0]

            tabu_list.append(next_location)
            if len(tabu_list) > tabu_size:
                tabu_list.pop(0)

        if len(route) > 1:
            routes.append(route)

    remaining_locations = set(locations) - visited
    if remaining_locations:
        remaining_route = [depot[0]] + list(remaining_locations)
        routes.append(remaining_route)

    return routes

# Method for plotting routes
def plot_routes(depot, routes, locations, time_windows):
    depot_x, depot_y = depot[0][0], depot[0][1]
    route_xs = [[location[0] for location in route] for route in routes]
    route_ys = [[location[1] for location in route] for route in routes]

    plt.scatter(depot_x, depot_y, color='red', label='Depot')

    for route_x, route_y in zip(route_xs, route_ys):
        route_x.append(depot_x)
        route_y.append(depot_y)
        plt.plot(route_x, route_y, marker='o')

    for i, location in enumerate(locations):
        plt.text(location[0], location[1], f'{time_windows[i][0]}-{time_windows[i][1]}', fontsize=9, ha='right')

    plt.xlabel('X Coordinate')
    plt.ylabel('Y Coordinate')
    plt.title('Feasible Routes with Time Windows')
    plt.legend()
    plt.show()

# K-means++ clustering
def kmeans_plusplus(X, k, max_iters=100):
    centroids = [X[np.random.choice(range(len(X)))]]

    for _ in range(k - 1):
        distances = np.min(np.linalg.norm(X[:, np.newaxis] - centroids, axis=-1), axis=-1)
        probabilities = distances / np.sum(distances)
        new_centroid = X[np.random.choice(range(len(X)), p=probabilities)]
        centroids.append(new_centroid)

    for _ in range(max_iters):
        labels = np.argmin(np.linalg.norm(X[:, np.newaxis] - centroids, axis=-1), axis=-1)
        new_centroids = []
        for i in range(k):
            cluster_points = X[labels == i]
            new_centroids.append(np.mean(cluster_points, axis=0))

        if np.allclose(centroids, new_centroids):
            break

        centroids = new_centroids

    return centroids, labels

# Plot K-means++ clustering
def plot_kmeans_plusplus(locations, centroids, labels, depot):
    clusters = [[] for _ in range(len(centroids))]

    for i, label in enumerate(labels):
        clusters[label].append(locations[i])

    for i, cluster in enumerate(clusters):
        x = [point[0] for point in cluster]
        y = [point[1] for point in cluster]
        plt.scatter(x, y, marker='.', label=f'Cluster {i + 1}')

    x_centroids = [centroid[0] for centroid in centroids]
    y_centroids = [centroid[1] for centroid in centroids]
    plt.scatter(x_centroids, y_centroids, color='black', marker='x', label='Centroids')
    plt.scatter(depot[0][0], depot[0][1], c="blue")

    plt.xlabel('X-coordinate')
    plt.ylabel('Y-coordinate')
    plt.title('K-means++ Clustering')
    plt.legend()
    plt.show()

# Reading delivery and depot data
K = 0
Q = 0
depot = []
locations = []
Q_delivery = []
time_windows = []

# Read data from 'Колличество транспорта.txt'
with open('Колличество транспорта.txt', 'r') as file:
    K = int(file.readline().strip())

# Read data from 'Грузоподьемность.txt'
with open('Грузоподьемность.txt', 'r') as file:
    Q = int(file.readline().strip())

# Read data from 'координаты точки депо.txt'
with open('координаты точки депо.txt', 'r') as file:
    line = file.readline().strip()
    depot = [tuple(map(float, line.split(',')))]

# Read data from 'Координаты адресов доставки.txt'
with open('Координаты адресов доставки.txt', 'r') as file:
    lines = file.readlines()
    locations = [tuple(map(float, line.strip().split(','))) for line in lines]

# Read data from 'вес груза для доставки.txt'
with open('вес груза для доставки.txt', 'r') as file:
    Q_delivery = [int(line.strip()) for line in file.readlines()]

# Read data from 'время для доставки.txt'
with open('время для доставки.txt', 'r') as file:
    lines = file.readlines()
    time_windows = [tuple(map(int, tw.strip().split(','))) for tw in lines]

# Output data from files for tests
print("K =", K)
print("Q =", Q)
print("depot =", depot)
print("locations =", locations)
print("Q_delivery =", Q_delivery)
print("time_windows =", time_windows)

# Clustering and plotting
centroids1, labels1 = kmeans_plusplus(np.array(locations), K)
#plot_kmeans_plusplus(locations, centroids1, labels1, np.array(depot))

# Find feasible routes
start1 = time.time()
routes = find_feasible_routes(depot, locations, centroids1, labels1, Q, Q_delivery, time_windows)
# Save routes to an array
all_routes = []
for i, route in enumerate(routes):
    all_routes.append(route)
    print(f"Route {i+1}: {route}")
end1 = time.time()
print(f"Time taken: {(end1 - start1) * 1000:.03f}ms")

len_routes = len(routes)
routes_first = routes[:-1]
#plot_routes(depot, routes_first, locations, time_windows)
#plot_routes(depot, routes, locations, time_windows)

flag = 0

while flag != 1:
    if K >= len_routes:
        flag = 1
    else:
        last_element = routes[-1]
        last_element = last_element[1:]

        weights_dict = dict(zip(locations, Q_delivery))
        Q_delivery1 = [weights_dict[point] for point in last_element]

        if len(last_element) >= K:
            centroids2, labels2 = kmeans_plusplus(np.array(last_element), K)
        else:
            last_element_x = [point[0] for point in last_element]
            last_element_y = [point[1] for point in last_element]
            depot_x = [point[0] for point in depot]
            depot_y = [point[1] for point in depot]

            for i in range(len(last_element)):
                plt.plot([depot_x[0], last_element_x[i]], [depot_y[0], last_element_y[i]], '-o', label=f'Route {i + 1}')

            plt.legend()
            plt.xlabel('X')
            plt.ylabel('Y')
            plt.show()
            break

        #plot_kmeans_plusplus(last_element, centroids2, labels2, np.array(depot))

        routes = find_feasible_routes(depot, last_element, centroids2, labels2, Q, Q_delivery1, time_windows)
        len_routes = len(routes)
        routes_first = routes[:-1]
        #plot_routes(depot, routes_first, locations, time_windows)
        #plot_routes(depot, routes, locations, time_windows)

# Define the depot variable
coord_depot = "54.959098, 82.936980"

# Create a map with Folium and save it to a BytesIO object
map = folium.Map(
    location=(55, 83),
    zoom_start=13,
    title='Golden Gate Bridge'
)

# Add depot marker
folium.Marker(
    location=[54.959098, 82.936980],
    tooltip=f"depot",
    popup=f"{coord_depot}",
    icon=folium.Icon(icon="cloud"),
).add_to(map)

# Add delivery markers
for location, weight in zip(locations, Q_delivery):
    folium.Marker(
        location=location,
        tooltip="Delivery",
        popup=f"Location: {location}, Weight: {weight}",
        icon=folium.Icon(color="red", icon="info-sign"),
    ).add_to(map)

# Add initial routes
def random_color():
    return "#{:06x}".format(random.randint(0, 0xFFFFFF))
for route in all_routes:
    color = random_color()
    folium.PolyLine(route, color=color, weight=2.5, opacity=1).add_to(map)


# Add JavaScript code for handling click events and displaying coordinates
click_js = '''
Координаты уточнять отдельно
'''

map.add_child(folium.ClickForMarker(popup=click_js))

data = io.BytesIO()
map.save(data, close_file=False)
data.seek(0)  # Reset the file pointer to the beginning



    # You can now use these variables in your application

class ExpenseTracker(QMainWindow):
    def __init__(self):
        super(ExpenseTracker, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Find the container in the interface
        container = self.ui.webEngineContainer

        # Create an instance of QWebEngineView
        self.webView = QWebEngineView()

        # Set the layout for the container
        layout = QVBoxLayout(container)
        layout.addWidget(self.webView)

        # Load the HTML map data
        self.webView.setHtml(data.getvalue().decode())

        self.ui.pushButton.clicked.connect(self.collect_data)

        self.ui.pushButton_2.clicked.connect(self.collect_data2)

        self.ui.pushButton_3.clicked.connect(self.collect_data3)

        self.ui.pushButton_4.clicked.connect(self.collect_data4)

    def collect_data(self):
        # Get data from line edits
        route_number = self.ui.lineEdit.text()
        driver_name = self.ui.lineEdit_2.text()
        car_number = self.ui.lineEdit_3.text()

        # Print collected data to verify (optional)
        print(f"Route Number: {route_number}, Driver Name: {driver_name}, Car Number: {car_number}")
        with open('время для доставки.txt', 'a') as file:
            file.write(f'\n{car_number}')

        with open('вес груза для доставки.txt', 'a') as file:
            file.write(f'\n{driver_name}')

        with open('Координаты адресов доставки.txt', 'a') as file:
            file.write(f'\n{route_number}')

    def collect_data2(self):
        car_value = self.ui.lineEdit_4.text()
        print(f"car_value: {car_value}")
        with open('Колличество транспорта.txt', 'w') as file:
            file.write(f'{car_value}\n')

    def collect_data3(self):
        Q = self.ui.lineEdit_5.text()
        print(f"Q: {Q}")
        with open('Грузоподьемность.txt', 'w') as file:
            file.write('{Q}\n')

    def collect_data4(self):
        depot = self.ui.lineEdit_6.text()
        print(f"depot: {depot}")
        with open('координаты точки депо.txt', 'w') as file:
            file.write(f'{depot}\n')

if __name__ == "__main__":
    app = QApplication.instance()  # Check if an instance already exists
    if app is None:  # Create QApplication if it does not exist
        app = QApplication(sys.argv)
    window = ExpenseTracker()
    window.show()
    sys.exit(app.exec())
