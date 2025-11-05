import math
from datetime import datetime

# 1. Создайте словарь email
email = {
    "subject": " Weekend plans ",
    "from": "  katya_yan@yandex.ru ",
    "to": "  friend@mail.ru ",
    "body": "\tHey!\nLet's go hiking this weekend.\nBring snacks!\n"
}

# 2. Добавьте дату отправки
email["date"] = send_data = datetime.now().strftime("%Y-%m-%d")

# 3. Нормализуйте e-mail адреса отправителя и получателя: приведите к нижнему регистру и уберите пробелы по краям
email["from"] = email["from"].strip().lower()
email["to"] = email["to"].strip().lower()

# 4. Извлеките логин и домен отправителя
login = email["from"].split('@')[0]
domain = email["from"].split('@')[1]

# 5. Создайте сокращённую версию текста:
email["short_body"] = email["body"][0:10] + "..."

# 6. Списки доменов:
# Личные:
personal_domains = ['gmail.com','list.ru', 'yahoo.com','outlook.com','hotmail.com',
                    'icloud.com','yandex.ru','mail.ru','bk.ru','inbox.ru']
# Корпоративные:
corporate_domains = ['company.ru','corporation.com','university.edu','organization.org', 'business.net']

personal_domains = list(set(personal_domains))
corporate_domains = list(set(corporate_domains))

# 7. Проверьте, что в списке личных и корпоративных доменов нет пересечений:
intersection = set(personal_domains) & set(corporate_domains)

# 8. Проверьте «корпоративность» отправителя:
sender_domain = email["from"].split("@")[1]
is_corporate = sender_domain in corporate_domains

# 9. Соберите «чистый» текст сообщения
email["clean_body"] = email["body"].replace("\t", " " ).replace("\n", " " )

# 10. Сформируйте текст отправленного письма
email["sent_text"] = f'''Кому: {email["to"]}, от {email["from"]} 
Тема: {email["subject"]}, дата {email["date"]} {email["clean_body"]}'''

# 11. Рассчитайте количество страниц печати
pages = (len(email["sent_text"]) + 499) // 500

# 12. Проверьте пустоту темы и тела письма:
is_subject_empty = not email["subject"].strip()
is_body_empty = not email["body"].strip()

# 13. Создайте «маску» e-mail отправителя: первые 2 символа логина + "***@" + домен
email["masked_from"] = login[0:2] + "***@" + domain

# 14. Удалите из списка личных доменов
personal_domains.remove("list.ru")
personal_domains.remove("bk.ru")

print(email)
print(is_corporate, is_subject_empty, is_body_empty, pages)