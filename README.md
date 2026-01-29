# 📚 Student Course Management System

**Template-based Django Project**

---

## Loyihaning Maqsadi

Bu loyiha **oddiy o‘quv kurslari va talabalar tizimi** bo‘lib, universitet yoki o‘quv markazidagi real holatni soddalashtirilgan ko‘rinishda aks ettiradi.

**Muhim cheklovlar:**

* ❌ REST API yo‘q
* ❌ Django Rest Framework yo‘q
* ❌ Authentication yo‘q
* ✅ Faqat **Django + templates**
* ✅ Faqat **CRUD + basic logic**

---

## O‘rganiladigan Asosiy Ko‘nikmalar

Student quyidagilarni **aniq ko‘rsatib berishi shart**:

* Django project/app strukturasi
* `models.py` bilan ishlash
* `ForeignKey` munosabat
* HTML template rendering
* URL → View → Template flow
* Form orqali ma’lumot kiritish
* Business logic (hisoblash, cheklov)

---

## Loyiha Strukturasi

```
student_system/
├── core/                  # Project settings
├── courses/               # App: Kurslar
├── students/              # App: Studentlar
├── enrollments/           # App: Ro‘yxatdan o‘tish
├── templates/
│   ├── base.html
│   ├── courses/
│   ├── students/
│   └── enrollments/
├── db.sqlite3
└── manage.py
```

---

## Ma’lumotlar Bazasi Modellari

---

## 1️⃣ Course Model (`courses/models.py`)

O‘quv kurslari.

| Field          | Type           | Majburiy |
| -------------- | -------------- | -------- |
| title          | CharField(200) | ✅        |
| description    | TextField      | ❌        |
| duration_weeks | IntegerField   | ✅        |
| created_at     | DateTimeField  | auto     |

**Qoidalar:**

* `duration_weeks > 0`
* `__str__()` → course title
* Kurs o‘chirilsa, unga yozilgan studentlar bo‘lsa — **o‘chirish mumkin emas**

---

## 2️⃣ Student Model (`students/models.py`)

Talabalar.

| Field      | Type           | Majburiy   |
| ---------- | -------------- | ---------- |
| full_name  | CharField(150) | ✅          |
| email      | EmailField     | ✅ (unique) |
| age        | IntegerField   | ✅          |
| created_at | DateTimeField  | auto       |

**Qoidalar:**

* `age >= 16`
* `email` unique
* `__str__()` → full_name

---

## 3️⃣ Enrollment Model (`enrollments/models.py`)

Student → Kurs bog‘lanishi.

| Field       | Type                |
| ----------- | ------------------- |
| student     | ForeignKey(Student) |
| course      | ForeignKey(Course)  |
| enrolled_at | DateTimeField       |

**Qoidalar:**

* Bitta student **bitta kursga faqat 1 marta yozilishi mumkin**
* `unique_together = ('student', 'course')`

---

## 🌐 URL & VIEW TALABLARI (MUHIM)

### 🔹 Barcha URL’lar **aniq shu ko‘rinishda bo‘lishi shart**

---

## 📘 Courses Pages

### 1. Kurslar ro‘yxati

```
GET /courses/
```

**Ko‘rsatadi:**

* Kurs nomi
* Davomiyligi
* Studentlar soni
* “Detail”, “Edit”, “Delete” tugmalari

---

### 2. Kurs yaratish

```
GET  /courses/create/
POST /courses/create/
```

**Form:**

* title
* description
* duration_weeks

---

### 3. Kurs detail sahifasi

```
GET /courses/<id>/
```

**Ko‘rsatadi:**

* Kurs ma’lumotlari
* Shu kursga yozilgan studentlar ro‘yxati

---

### 4. Kursni tahrirlash

```
GET  /courses/<id>/edit/
POST /courses/<id>/edit/
```

---

### 5. Kursni o‘chirish

```
POST /courses/<id>/delete/
```

**Agar studentlar mavjud bo‘lsa:**

> “Bu kursga studentlar yozilgan. O‘chirish mumkin emas.”

---

## 👤 Students Pages

### 1. Studentlar ro‘yxati

```
GET /students/
```

**Filterlar:**

* `?min_age=18`
* `?search=ali`

---

### 2. Student yaratish

```
GET  /students/create/
POST /students/create/
```

---

### 3. Student detail

```
GET /students/<id>/
```

**Ko‘rsatadi:**

* Student ma’lumotlari
* Qaysi kurslarga yozilgan

---

### 4. Studentni o‘chirish

```
POST /students/<id>/delete/
```

---

## 🧾 Enrollment Pages

### 1. Studentni kursga yozish

```
GET  /enrollments/create/
POST /enrollments/create/
```

**Form:**

* student (select)
* course (select)

**Validatsiya:**

* Avval yozilgan bo‘lsa → error chiqadi

---

### 2. Barcha enrollments

```
GET /enrollments/
```

---

## 🧩 Template TALABLARI

* `base.html` bo‘lishi shart
* Har bir sahifa `extends base.html`
* Minimal styling (`table`, `form`, `button`)
* Error message’lar aniq ko‘rinishi kerak

---

## ✅ Baholash Mezoni (Exam Rubric)

| Criteria           | Ball    |
| ------------------ | ------- |
| Models to‘g‘ri     | 20      |
| URL & Views to‘liq | 25      |
| CRUD ishlashi      | 25      |
| Template logikasi  | 15      |
| Validatsiya        | 15      |
| **Jami**           | **100** |


