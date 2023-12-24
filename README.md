# Blog-loyihasi
Oddiy django loyihasi

Ushbu loyihani kompyuteringizda qanday ishga tushirish bo'yicha bosqichma-bosqich buyruqlar

![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E)
![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)
![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white)
![Visual Studio Code](https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white)

## Ishlatilgan texnologiyalar
1. HTML
2. CSS
3. JavaScript
4. Python
5. Django


### Ishlatilgan asosiy modullar
1. Django==4.1.4
2. gunicorn==20.1.0
3. whitenoise==6.3.0



## Xususiyatlari
1. Foydalanuvchining autentifikatsiyasi va avtorizatsiyasi.
2. Kurslarni yaratish, boshqarish va nashr etish uchun o'qituvchilar uchun kurslarni boshqarish tizimi.
3. Boshqaruv panelida kurs va roʻyxatga olish statistikasi va boshqalarni koʻring.
4. Turli toifalar bilan kurslar katalogi
5. Mobil va planshet qurilmalari uchun sezgir dizayn



1)- Muhit yuklab oling Virtualenv

```
pip install virtualenv
```

2)- Virtualenv yarating

```
virtualenv venv
```

3)- Virtual muhitni faollashtirish

```
venv/Scripts/activate
```

4)- O'rnatish talablari agar kutubxonalar to'liq bo'lsa shart emas!

```
pip install -r requirements.txt
```
Eslatma: Birinchi marta o'rnatish uchun yuqoridagi buyruq talab qilinadi!

5)- Quyidagi buyruqlarni bajaring bu shart database uchun

```
python manage.py makemigrations
```
```
python manage.py migrate
```
Eslatma: Agar database ni debug da ishga tushursangiz bu majburiy!

6)- Administratorga kirish uchun createsuperuser yarating va agar yaratilmagan bo'lsa, ko'rsatmalarga rioya qiling:

Username: Xusanbek
Parol: 0071

```
python manage.py createsuperuser
```

7)- Statik fayllarni bitta joyda to'plang. Bu shart aks holda sayt css fayllarni o'qimaydi
```
python manage.py collectstatic
```
<br>

## Ishga tushurish

```
python manage.py runserver
```
Loyiha ishga tayyor uni ishga tushurish mumkin!
Eslatma: Agar qadamlar to'g'ri bajarilsa loyiha ishga tushadi!

<br>


## Loyihadan lavhalar

# https://creators-blog.onrender.com



## Kirish
**IT Creative** o'qituvchilarga talabalar uchun onlayn kurslarni yaratish va yuklash imkonini beruvchi elektron ta'lim platformasi. U kurslarni yaratish va boshqarish uchun qulay interfeysni taqdim etadi. Talabalar o'zlari tanlagan kurslarni ko'rib chiqishlari va ro'yxatdan o'tishlari mumkin. Skillmate, shuningdek, o'qituvchilarga kurslar tahlilini, masalan, ro'yxatga olishlarni ko'rish uchun asboblar panelini taklif qiladi. Python va Django bilan yaratilgan IT Creative veb-ishlab chiqish va xavfsizlik bo'yicha eng yaxshi amaliyotlarga amal qiladi.


## MUNDARIJA
  * [Kirish](#introduction)
  * [O'rnatish majburiy](#installed)
  * [Ishlatilgan texnologiyalar](#technologies-used)
  * [Xususiyatlari](#features)
  * [Website lavhalar](#screenshots)
  * [Xulosa](#conclusion)
