import csv

import bs4
import requests


def ziskej_parsovanou_odpoved(url: str) -> bs4.BeautifulSoup:
    """
    Získej rozdělenou odpověď na požadavek typu GET.
    """
    return bs4.BeautifulSoup(requests.get(url).text, features="html.parser")


def vyber_jen_tr_tagy(soup: bs4.BeautifulSoup) -> bs4.element.ResultSet:
    """
    Ze zdrojového kódu stránky vyber všechny tagy "tr".
    """
    return soup.find_all("tr")


def rozdel_zahlavi_a_transakce(all_tr: bs4.element.ResultSet) -> tuple:
    """
    Vrať z tagů "tr" pouze záhlaví a informace ke všem transakcím.
    """
    header_tag, *transactions = all_tr[2:]
    header: list = header_tag.get_text().splitlines()[1:]
    return header, transactions


def projdi_vsechny_td_tagy(transactions: list) -> list:
  """
  Vrať seznam, který obsahuje slovníky s detaily každé transakce.
  """
  return [
          ziskej_hodnoty_z_radku(
              transaction.find_all("td"),
              0, 1, 2, 3, 4, 5, 6, 7, 8
          )
          for transaction in transactions
  ]


def ziskej_hodnoty_z_radku(soup, *index_) -> dict:
    """
    Vrať slovník, který namapuje klíče a uloží jejich hodnoty.
    """
    payment_details: dict = {}

    for index in index_:
        payment_details[namapuj_index_na_hodnotu(index)] = soup[index].text.strip()

    return payment_details


def namapuj_index_na_hodnotu(index: int) -> str:
    """
    Indexy a jejich význam:
    0 - datum,
    1 - castka,
    2 - typ,
    3 - nazev protiuctu,
    4 - zprava,
    5 - ks,
    6 - vs,
    7 - ss,
    8 - poznamka
    """
    return {
        0: 'datum',
        1: 'castka',
        2: 'typ',
        3: 'nazev protiuctu',
        4: 'zprava',
        5: 'ks',
        6: 'vs',
        7: 'ss',
        8: 'poznamka'
    }.get(index)


if __name__ == "__main__":
    url: str = "https://ib.fio.cz/ib/transparent?a=2801322199&f=01.10.2021&t=08.02.2022"
    odpoved = ziskej_parsovanou_odpoved(url)
    zahlavi, transakce = rozdel_zahlavi_a_transakce(vyber_jen_tr_tagy(odpoved))
    results = projdi_vsechny_td_tagy(transakce)

    from pprint import pprint
    pprint(results)

