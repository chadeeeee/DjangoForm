from django.shortcuts import render, redirect

from myapp.models import Worker
from django.views.decorators.csrf import csrf_exempt

import sqlite3 as sq


# Create your views here.

base = sq.connect("data.sqlite3")
cur = base.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS userdata (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                email TEXT,
                message TEXT
            )""")


def index_page(request):
    text = 'Слава Україні!!'
    all_workers = Worker.objects.all()
    print(all_workers)

    return render(request, 'index.html', {'data': all_workers})


def onclick_function(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']

        # Ваш код обробки onclick з використанням отриманих даних
        print("Ім'я:", name)
        print("Email:", email)
        print("Текст:", message)

        base = sq.connect('data.sqlite3')
        cur = base.cursor()

        cur.execute('INSERT INTO userdata (name, email, message)'
                    'VALUES (?, ?, ?)',
                    (name, email, message))
        base.commit()

        context = {
            'name': name,
            'email': email,
            'message': message
        }

        return render(request, 'successful.html')
    else:
        return render(request, 'onclick.html')
