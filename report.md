# Report – Course Recommendation System

## 1. Introduction

Šis projektas yra objektinio programavimo kursinis darbas. Projekto idėja yra sukurti paprastą kursų rekomendavimo sistemą, kuri pagal vartotojo įvestą informaciją pasiūlo tinkamus mokymosi kursus.

Programa veikia per terminalą. Vartotojas įveda norimą rolę, biudžeto lygį, kiek valandų per savaitę gali mokytis ir vieną turimą įgūdį. Tada sistema pagal pasirinktą strategiją pateikia kursų rekomendacijas.

Projektas nėra pilna reali rekomendacinė sistema ar AI modelis. Tai yra labiau prototipas, kuris parodo kaip galima naudoti objektinį programavimą, klases, paveldėjimą, polimorfizmą, failų skaitymą ir rašymą.

## 2. Body / Analysis

### Projekto struktūra

Projektas padalintas į kelias pagrindines dalis.

main.py yra pagrindinis failas, kuris paleidžia programą. Jame vartotojas įveda duomenis ir pasirenka rekomendavimo strategiją.

models aplanke yra pagrindinės klasės, tokios kaip Course, Skill, LearningProfile ir CourseRecommendation. Šios klasės reprezentuoja pagrindinius programos objektus.

repository aplanke yra klasės, kurios atsakingos už duomenų nuskaitymą ir išsaugojimą. CourseRepository nuskaito kursus iš JSON failo, o ProfileRepository išsaugo ir užkrauna vartotojo profilį.

engine aplanke yra rekomendavimo logika. Ten yra RecommendationEngine ir kelios rekomendavimo strategijos.

data aplanke saugomi JSON failai su kursais ir vartotojo profiliu.

tests aplanke yra paprasti unit testai.

### Kaip veikia programa

Programa pirmiausia paklausia, kokią rekomendavimo strategiją naudoti. Yra dvi strategijos: BasicRuleStrategy ir SkillGapStrategy.

Tada vartotojas įveda savo informaciją. Pagal šią informaciją sukuriamas LearningProfile objektas. Profilis išsaugomas į profiles.json, o kursai nuskaitomi iš items.json.

Tada RecommendationEngine gauna pasirinktą strategiją ir naudoja ją rekomendacijoms sugeneruoti.

BasicRuleStrategy veikia kaip bendresnė taisyklių strategija. Ji žiūri į vartotojo norimą rolę, biudžetą, mokymosi laiką ir kurso sudėtingumą.

SkillGapStrategy veikia šiek tiek kitaip. Ji bando palyginti vartotojo turimus įgūdžius su tais įgūdžiais, kurie reikalingi norimai rolei. Tada ji rekomenduoja kursus pagal tai, ko vartotojui dar trūksta.

### OOP principai

#### Inkapsuliacija

Projekte naudojami atributai su apatiniu brūkšniu, pavyzdžiui _title, _price, _target_role ir _current_skills.

Tai parodo, kad šie atributai priklauso klasei ir neturėtų būti tiesiogiai keičiami iš išorės. Projekte jie vis tiek kartais naudojami tiesiogiai, nes projektas yra paprastas ir pradedančiojo lygio.

#### Paveldėjimas

Paveldėjimas naudojamas rekomendavimo strategijose.

BasicRuleStrategy ir SkillGapStrategy paveldi iš RecommendationStrategy. Tai reiškia, kad abi strategijos turi bendrą pagrindą, bet gali turėti skirtingą rekomendavimo logiką.

#### Polimorfizmas

Polimorfizmas matomas per metodą generate_recommendations().

Abi strategijos turi tokį patį metodą, bet jo veikimas skiriasi.

BasicRuleStrategy rekomenduoja kursus pagal rolę, biudžetą, laiką ir sudėtingumą.

SkillGapStrategy bando pažiūrėti, kokių įgūdžių vartotojui trūksta pagal norimą rolę, ir tada rekomenduoja kursus pagal trūkstamus įgūdžius.

#### Kompozicija / agregacija

LearningProfile turi sąrašą Skill objektų. Tai reiškia, kad vartotojo profilis susideda iš kitų objektų.

Pavyzdžiui, vartotojas gali turėti įgūdį Python, kuris yra atskiras Skill objektas.

### Design pattern

Projekte naudojamas Strategy design pattern.

Šis šablonas pasirinktas todėl, kad rekomendavimo sistema gali turėti kelis skirtingus rekomendavimo būdus. Vietoj to, kad visa logika būtų vienoje vietoje, kiekviena strategija turi savo klasę.

RecommendationEngine gauna strategiją ir iškviečia jos metodą generate_recommendations().

Dėl to galima pakeisti rekomendavimo būdą nekeičiant viso rekomendavimo variklio.

### File input / output

Projekte naudojami JSON failai.

items.json saugo kursų sąrašą. Iš šio failo CourseRepository nuskaito kursus ir sukuria Course objektus.

profiles.json saugo vartotojo profilį. ProfileRepository gali išsaugoti profilį ir vėliau jį vėl užkrauti.

Tai leidžia programai ne tik laikyti duomenis atmintyje, bet ir išsaugoti juos faile.

### Testavimas

Projektui parašyti keli paprasti unittest testai.

Testai tikrina, ar galima pridėti įgūdį į LearningProfile, ar LearningProfile gali rasti turimą įgūdį, ar kursai nuskaitomi iš JSON failo, ir ar profilis gali būti išsaugotas bei užkrautas.

Testus galima paleisti su komanda:

python -m unittest discover

Testai nėra labai sudėtingi, bet jie patikrina pagrindines projekto dalis.

## 3. Results

Sukurta paprasta terminalinė kursų rekomendavimo sistema. Programa leidžia vartotojui įvesti savo mokymosi tikslą ir gauti kursų rekomendacijas.

Sistema turi dvi rekomendavimo strategijas. Paprasta strategija rekomenduoja pagal bendras taisykles, o SkillGapStrategy bando rekomenduoti kursus pagal trūkstamus įgūdžius.

Taip pat įgyvendintas duomenų nuskaitymas iš JSON failų, vartotojo profilio išsaugojimas, objektinio programavimo principai ir paprasti unit testai.

Pavyzdžiui, jei vartotojas įveda data scientist ir jau moka Python, tada SkillGapStrategy gali rekomenduoti kitus reikalingus įgūdžius, tokius kaip SQL, Statistics, Machine Learning ar panašius kursus.

## 4. Conclusions

Šio projekto metu buvo sukurtas paprastas OOP principais paremtas kursų rekomendavimo prototipas. Projektas padėjo geriau suprasti, kaip klasės gali būti atskirtos pagal atsakomybes ir kaip galima naudoti Strategy design pattern.

Manau, kad svarbiausia projekto dalis yra ne pati rekomendavimo logika, bet tai, kad sistema turi aiškų karkasą. Ateityje tokią sistemą būtų galima plėsti ir naudoti sudėtingesnį rekomendavimo algoritmą.

Galimi patobulinimai ateityje būtų leisti vartotojui įvesti daugiau nei vieną įgūdį, saugoti daugiau vartotojų profilių, pridėti tikresnį teksto supratimą pagal laisvą vartotojo įvestį, naudoti duomenų bazę vietoj JSON failų ir pridėti feedback funkciją, kad vartotojas galėtų pasakyti, ar rekomendacija buvo naudinga.

Dabartinė versija nėra tobula, bet ji atitinka pagrindinę kursinio darbo idėją ir parodo objektinio programavimo principų naudojimą praktiniame projekte.
