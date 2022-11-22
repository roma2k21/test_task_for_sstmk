import requests
import socket
import re


def test_status():
    """Проверить код ответа."""
    response = requests.get('https://sstmk.ru/')
    assert response.status_code == 200, (
        'Код ответа не 200')


def test_ip_adress():
    """Проверить ip адрес."""
    ip_adress = socket.gethostbyname('www.sstmk.ru')
    assert ip_adress == '46.30.42.27', (
        'ip адрес не соответствует ожидаемому'
    )


def test_phone_format():
    """Проверить формат номера телефона компании."""
    phone_pattern = r'^\+\d\(\d*\)[\d*\-]{7,9}|^\(\d*\)[\d*\-]{7,9}'
    response = requests.get('https://sstmk.ru/')
    context = response.content
    context = context.decode('utf-8')
    context_lst = context.replace(' ', '')
    phones = re.findall(phone_pattern, context_lst)
    assert phones, (
        'Некорректный формат номера телефона'
    )
