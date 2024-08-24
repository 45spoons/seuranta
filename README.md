# Opt-in kävijäseuranta

![tests](https://github.com/45spoons/seuranta/actions/workflows/tests.yml/badge.svg)

## Alustaminen

Vaatimukset:

- python >= 3.12.5
- verkkoyhteys tietotekniikkatila-Kattilan lähiverkkoon

```shell
git clone git@github.com:45spoons/seuranta.git
cd seuranta/
python3 -m venv .venv
source ./.venv/bin/activate
pip3 install -r requirements.txt
python3 ./main.py
```

## Tietokantamigraatiot

Jos olet tehnyt muutoksia tietokannan rakenteeseen, tulee luoda alembic:lla migraatio.
Tämän jälkeen sinun _tulee_ tarkistamalla ja muuttamalla luotua versiotiedostoa varmistua, että tulevat muutokset olisivat tarkoituksenmukaisia.

```shell
alembic revision --autogenerate -m "kuvaile tässä tekemääsi muutosta hyödyllisellä tavalla"
```

Muutoksen seurantaa pyörittävään tietokantaan saa ajamalla komento:

```shell
alembic upgrade head
```

## Projektin rakenne

```text
.
│   .gitignore
│   LICENSE
│   main.py
│   README.md
│   requirements.txt
├───.github
│   └───workflows
│           tests.yml
├───tests
│       __init__.py
│       test_seuranta_app.py
│       test_seuranta_db.py
│       test_lease_monitor.py
├───static
│   │   styles.css
│   │   Exo2-VariableFont_wght.ttf
│   └───images
│           favicon.png
│           favicon.svg
├───templates
│       base.html
│       index.html
│       name-form.html
└───src
        seuranta_app.py
        lease_monitor.py
        db.py
        __init__.py
```

## Kehitys

Tutustu vähintään lyhyesti conventional commits käytäntöön, mm. [tästä lunttilapusta](https://gist.github.com/Zekfad/f51cb06ac76e2457f11c80ed705c95a3).
