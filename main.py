from simple_image_download import simple_image_download as simp
import os

def save_images(query, folder_path, num_images=10):
    # Создаем папку для сохранения изображений, если она не существует
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

        # Используем simple_image_download для загрузки изображений
    response = simp.Downloader()
    response.download(keywords=query, limit=num_images)
    print("Изображения сохранены в папке", folder_path)


class PlantSensor:
    def __init__(self, sunlight, water, nutrients, temperature):
        self.sunlight = sunlight
        self.water = water
        self.nutrients = nutrients
        self.temperature = temperature

    def check_status(self):
        status = []
        if self.sunlight < 50:
            status.append("Не хватает солнечного света.")
        if self.water < 30:
            status.append("Не хватает воды.")
        if self.nutrients < 20:
            status.append("Не хватает питательных веществ.")
        if self.temperature < 15 or self.temperature > 30:
            status.append("Температура не подходит для роста растения.")
        return status

class VirtualMachine:
    def __init__(self):
        self.sunlight_tank = 100
        self.water_tank = 100
        self.nutrients_container = 100
        self.temperature_controller = 25

    def add_elements(self, status):
        for element in status:
            if "света" in element:
                self.sunlight_tank += 20
            elif "воды" in element:
                self.water_tank += 20
            elif "питательных веществ" in element:
                self.nutrients_container += 20
            elif "Температура" in element:
                if "ниже" in element:
                    self.temperature_controller += 5
                elif "выше" in element:
                    self.temperature_controller -= 5

# Пример использования виртуальной машины и сенсора
if __name__ == "__main__":
    query1 = "apple"  # Ваш запрос
    folder_path1 = "images"  # Папка для сохранения изображений
    num_images1 = 5  # Количество изображений для сохранения

    save_images(query1, folder_path1, num_images1)
    # Предположим, у нас есть растение с определенными потребностями
    spinach_needs = {
        "sunlight": 40,
        "water": 25,
        "nutrients": 15,
        "temperature": 0
    }

    # Создаем виртуальный сенсор для растения
    sensor = PlantSensor(**spinach_needs)

    # Проверяем состояние растения
    status = sensor.check_status()
    print("Состояние растения:", status)

    # Создаем виртуальную машину и добавляем недостающие элементы
    vm = VirtualMachine()
    vm.add_elements(status)

    # Проверяем обновленное состояние ресурсов
    print("Солнечный свет:", vm.sunlight_tank)
    print("Вода:", vm.water_tank)
    print("Питательные вещества:", vm.nutrients_container)
    print("Температура:", vm.temperature_controller)