# Домашнее задание по теме "Обзор сторонних библиотек Python".
# Ознакомление с использованием сторонних библиотек в Python и применить их в различных задачах.

import requests
import numpy as np
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup

# Этап 1: Сбор данных

url = 'https://www.statista.com/statistics/272014/global-social-networks-ranked-by-number-of-users/'

try:
    response = requests.get(url)
    response.raise_for_status()
except requests.RequestException as e:
    print(f'Ошибка при запросе данных: {e}')
    exit()

soup = BeautifulSoup(response.content, 'html.parser')

table = soup.find('table', {'class': 'table'})

platforms = []
users = []

for row in table.find_all('tr')[1:]:  # Skip the header row
    columns = row.find_all('td')

    # Ensure we have both platform name and user count
    if len(columns) >= 2:
        platform = columns[0].text.strip()
        user_text = columns[1].text.strip()

        # Remove commas and convert to float
        user_count = float(user_text.replace(',', ''))

        platforms.append(platform)
        users.append(user_count)
    else:
        print(f'Пропущена строка с неполными данными: {row}')

# Этап 2: Анализ данных
total_users = np.sum(users)
average_users = np.mean(users)

# Этап 3: Визуализация данных
plt.figure(figsize=(12, 6))
plt.bar(platforms, users)
plt.xlabel('Социальная сеть')
plt.ylabel('Количество пользователей (млн)')
plt.title('Количество пользователей в социальных сетях по всему миру')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

# Вывод результатов
print('------------------------------')
print('Анализ данных о социальных сетях:')
print('------------------------------')
print(f'Общее количество пользователей: {total_users} млн.')
print(f'Среднее количество пользователей: {average_users:.2f} млн.')
print('------------------------------')