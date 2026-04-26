# OOP Coursework – Course Recommendation System

Tai yra objektinio programavimo kursinis darbas. Projekte kuriama paprasta kursų rekomendavimo sistema, kuri pagal vartotojo įvestą informaciją pasiūlo kelis tinkamiausius kursus.

Naudojamas ribotas kiekis kursų todėl galima išbandyti tik įvedant tam tikras profesijas kaip Project management, data science ir panašūs.

## Kaip paleisti

Projektą galima paleisti iš pagrindinio aplankalo:
per bash įvedant kodą
python main.py


Programa terminale paprašo įvesti:
- norimą rolę, pvz. `data scientist`, `web developer`, `project manager`
- biudžeto lygį
- kiek valandų per savaitę galima mokytis
- vieną turimą įgūdį
- pasirinkti rekomendavimo strategiją

Tada programa išveda rekomenduojamus kursus.

## Projekto struktūra

- `main.py` - pagrindinis programos paleidimo failas
- `models` - pagrindinės klasės, pvz. `Course`, `Skill`, `LearningProfile`
- `engine` - rekomendavimo logika ir strategijos
- `repository` - JSON failų nuskaitymas ir išsaugojimas
- `data` - kursų ir profilio duomenys
- `tests` - unit testai

## Pagrindinė idėja

Vartotojas įveda, kuo nori tapti arba ką nori mokytis. Sistema turi kursų sąrašą JSON faile ir pagal pasirinktą strategiją atrenka tinkamus kursus.

Yra dvi pagrindinės strategijos:

- `BasicRuleStrategy` - bendra rekomendacija pagal rolę, biudžetą, laiką ir kurso sudėtingumą.
- `SkillGapStrategy` - bando rasti, kokių įgūdžių vartotojui trūksta pagal pasirinktą rolę, ir rekomenduoja kursus tiems trūkstamiems įgūdžiams.

Pavyzdžiui, jei vartotojas nori tapti `data scientist`, bet jau moka `Python`, tai `SkillGapStrategy` labiau rekomenduos `SQL`, `Statistics`, `Machine Learning` ar panašius kursus.
Jei vartotojas nori tapti `data scientist` ir pasirenka basic recommendation, tai jam pasiūlys tuos pagrindinius kursus kurie jam leistų mokytis pagal jo pasirinktus kriterijus.

## OOP principai

Projekte naudojami keli objektinio programavimo principai:

- Inkapsuliacija - pvz. `_title`, `_price`, `_current_skills`.
- Paveldėjimas - `BasicRuleStrategy` ir `SkillGapStrategy` paveldi iš `RecommendationStrategy`.
- Polimorfizmas - abi strategijos turi metodą `generate_recommendations()`, bet veikia skirtingai.
- Kompozicija / agregacija - `LearningProfile` turi sąrašą `Skill` objektų.

## Design pattern

Projekte naudojamas **Strategy design pattern**.

`RecommendationEngine` pats nežino, kaip tiksliai skaičiuoti rekomendacijas. Jis gauna pasirinktą strategiją ir naudoja jos metodą `generate_recommendations()`.

Dėl to galima pakeisti rekomendavimo būdą neperrašant viso variklio.

## Failų naudojimas

Duomenys saugomi JSON failuose:

- `items.json` – kursų sąrašas
- `profiles.json` – vartotojo profilis

`CourseRepository` nuskaito kursus iš failo, o `ProfileRepository` išsaugo ir vėl užkrauna vartotojo profilį.

## Testai

Projekte yra keli paprasti `unittest` testai. Jie tikrina:

- ar `LearningProfile` metodai veikia
- ar kursai nuskaityti iš JSON
- ar profilis gali būti išsaugotas ir užkrautas

Testus galima paleisti per bash įvedant kodą
python -m unittest discover

## Rezultatas

Gavosi paprasta kursų rekomendavimo sistema. Ji leidžia sukurti vartotojo profilį, išsaugoti jį į failą, užkrauti kursų duomenis ir pateikti rekomendacijas pagal pasirinktą strategiją.

Sistema dar nėra tobula, bet ji parodo pagrindinę idėją ir objektinio programavimo principų naudojimą.