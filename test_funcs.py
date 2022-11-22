import requests
import socket
import re


def get_status_code() -> int:
    """Получить status code ответа на запрос."""
    response = requests.get('https://sstmk.ru/')
    return response.status_code


def get_ip_adress() -> str:
    """Узнать ip адрес сайта по имени хоста."""
    ip_adress = socket.gethostbyname('www.sstmk.ru')
    return ip_adress


def get_phone() -> str:
    """Получить номер телефона компании в правильном формате"""
    response = requests.get('https://sstmk.ru/')
    context = response.content
    context = context.decode('utf-8')
    context_lst = context.replace(' ', '')
    phone_pattern = r'^\+\d\(\d*\)[\d*\-]{7,9}|^\(\d*\)[\d*\-]{7,9}|\d\(\d*\)[\d*\-]{7,9}'
    phones = re.findall(phone_pattern, context_lst)
    phone = phones[0].replace('8', '+7')
    return phone


if __name__ == '__main__':
    print(get_status_code())
    print(get_ip_adress())
    print(get_phone())
