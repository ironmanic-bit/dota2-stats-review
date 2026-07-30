# 🎮 Dota 2 Stats Review

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10.6-blue?style=flat-square&logo=python" alt="Python">
  <img src="https://img.shields.io/badge/Flet-Latest-green?style=flat-square" alt="Flet">
  <img src="https://img.shields.io/badge/API-OpenDota-orange?style=flat-square" alt="OpenDota">
</p>

Приложение для просмотра статистики игроков в Dota 2 через открытое API OpenDota.

В процессе разработки я использовал ИИ как вспомогательный инструмент для обсуждения идей, поиска возможных решений и проверки отдельных участков кода. Все ключевые решения по архитектуре, доработке и развитию проекта принимались и реализовывались мной.

---

## 🔍 Что умеет

- Находить игрока по никнейму (планируется переработка поиска)
- Показывать последние матчи с деталями (дорабатывается) 
- Копировать ID профиля в один клик
- Переключать язык между английским и русским
- Приятные анимации и плавные переходы (дорабатывается)

---

## 🛠️ Стек/Библиотеки

- **Flet** — GUI-фреймворк
- **Python 3.10.6**
- **Asyncio** — для асинхронных запросов
- **Requests** — работа с API OpenDota
- **OpenDota API** — источник статистики

---

## 🚀 Запуск

```bash
# Клонируем
git clone https://github.com/ironmanic-bit/dota2-stats-review.git
cd dota2-stats-review

# Ставим зависимости
pip install -r requirements.txt

# Запускаем
flet run main.py
