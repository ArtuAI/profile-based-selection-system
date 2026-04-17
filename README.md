# OOP Coursework – Course Recommendation System

Šis projektas yra mano objektinio programavimo kursinis darbas.

Projekto idėja yra sukurti paprastą kursų rekomendacinę sistemą, kuri pagal vartotojo pateiktą informaciją galėtų pasiūlyti tinkamiausius kursus.

## Kaip veikia projektas

Vartotojas įveda savo informaciją, pavyzdžiui:
- kokią rolę nori pasiekti
- kiek laiko gali skirti mokymuisi
- koks yra jo biudžetas
- kokius įgūdžius jau turi

Tada sistema palygina šią informaciją su turimais kursais ir pateikia rekomendacijas.

## Projekto struktūra

- `data` – čia laikomi duomenys apie kursus
- `models` – pagrindinės projekto klasės
- `repository` – atsakinga už duomenų paėmimą
- `engine` – rekomendavimo logika
- `services` – pagalbinės funkcijos ir projekto dalių sujungimas
- `tests` – testai
- `main.py` – pagrindinis failas programos paleidimui

## OOP dalis

Šiame projekte naudojami objektinio programavimo principai, tokie kaip:
- inkapsuliacija
- paveldėjimas
- polimorfizmas
- agregacija / kompozicija

Taip pat šiame projekte naudojamas `Strategy` design pattern, kad būtų galima taikyti skirtingas rekomendavimo strategijas.