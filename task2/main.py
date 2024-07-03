# main.py

from pymongo import MongoClient

# Підключення до MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client['cat_database']
collection = db['cats']

# Створення документа
def create_cat(name, age, features):
    cat = {
        "name": name,
        "age": age,
        "features": features
    }
    collection.insert_one(cat)
    print(f"Кіт {name} доданий.")

# Читання документів
def read_all_cats():
    cats = collection.find()
    for cat in cats:
        print(cat)

def read_cat_by_name(name):
    cat = collection.find_one({"name": name})
    if cat:
        print(cat)
    else:
        print(f"Кіт з ім'ям {name} не знайдений.")

# Оновлення документів
def update_cat_age(name, new_age):
    result = collection.update_one({"name": name}, {"$set": {"age": new_age}})
    if result.matched_count > 0:
        print(f"Вік кота {name} оновлено до {new_age}.")
    else:
        print(f"Кіт з ім'ям {name} не знайдений.")

def add_feature_to_cat(name, feature):
    result = collection.update_one({"name": name}, {"$push": {"features": feature}})
    if result.matched_count > 0:
        print(f"Характеристика '{feature}' додана до кота {name}.")
    else:
        print(f"Кіт з ім'ям {name} не знайдений.")

# Видалення документів
def delete_cat_by_name(name):
    result = collection.delete_one({"name": name})
    if result.deleted_count > 0:
        print(f"Кіт з ім'ям {name} видалений.")
    else:
        print(f"Кіт з ім'ям {name} не знайдений.")

def delete_all_cats():
    result = collection.delete_many({})
    print(f"Всі коти видалені. Видалено {result.deleted_count} записів.")

if __name__ == '__main__':
    # Приклади використання функцій
    create_cat("barsik", 3, ["ходить в капці", "дає себе гладити", "рудий"])
    read_all_cats()
    read_cat_by_name("barsik")
    update_cat_age("barsik", 4)
    add_feature_to_cat("barsik", "любит гратися з м'ячем")
    delete_cat_by_name("barsik")
    delete_all_cats()