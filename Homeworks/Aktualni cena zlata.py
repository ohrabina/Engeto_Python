"""
Cile ulohy:
1. odeslat pozadavek na zadane 'url' a ziskat html,
2. parsovat html, at muzeme jednoduse vyhledat potrebne elementy,
3. pomoci vhodne metody vyhledat element obsahujici hledanou informaci o cene,
4. podle aktualniho casu a data ulozit ziskanou informaci (napr. slovnik),
5. pokud soubor neexistuje, chci soubor vytvorit se zahlavim a prvni informaci,
6. pokud soubor existuje, chci pripojit cenu nakonec a bez zahlavi.
"""
import os
import csv
from datetime import datetime

import requests
from bs4 import BeautifulSoup


def main() -> None:
    url = "https://markets.businessinsider.com/commodities/gold-price"
    date_format = "%d.%m.%Y %H:%M"
    price = get_gold_price(url, date_format)
    save_data_as_csv_file(
        {
            "time": datetime.now().strftime("%d.%m.%y-%H:%M:%S"),
            "price": price
        },
        "gold_price.csv"
    )


def get_gold_price(url: str, date: str) -> str:
    """
    Funkce odesila pozadavek 'get' na zadanou adresu 'url'.
    Naslednou odpoved parsuje pomoci knihovny 'bs4' a rozdeli text v elementu,
    podle ceny a zbytku dat.

    :return: str
    """
    response = requests.get(url)
    parsed_soup = BeautifulSoup(response.content)
    gold_price, *rest = parsed_soup.find(
        'div',
        {'class': 'price-section__values'}
    ).get_text().split()

    return gold_price


def save_data_as_csv_file(data: dict, filename: str) -> None:
    """
    Pokud neexistuje soubor v 'filename' vytvor jej, vloz zahlavi a 'data'.
    Pokd existuje soubor v 'filename' otevri jej a nakonec pridej 'data'.

    :return: None
    """
    mode = "w" if filename not in os.listdir() else "a"

    with open(filename, mode) as csv_file:
        header = data.keys()
        reader = csv.DictReader(csv_file)
        writer = csv.DictWriter(csv_file, fieldnames=header)

        if mode == "w":
            writer.writeheader()
        writer.writerow(data)


if __name__ == "__main__":
    main()
