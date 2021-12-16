#!/usr/bin/env python3

from datetime import datetime
import sys


WEEKDAYS = {"CA":["dilluns", "dimarts", "dimecres", "dijous", "divendres", "dissabte", "diumenge"],
        "CZ":["pondělí", "úterý", "středa", "čtvrtek", "pátek", "sobota", "neděle"],
        "DE":["montag", "dienstag", "mittwoch", "donnerstag", "freitag", "samstag", "sonntag"],
        "DK":["mandag", "tirsdag", "onsdag", "torsdag", "fredag", "lørdag", "søndag"],
        "EN":["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"],
        "ES":["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"],
        "FI":["maanantai", "tiistai", "keskiviikko", "torstai", "perjantai", "lauantai", "sunnuntai"],
        "FR":["lundi", "mardi", "mercredi", "jeudi", "vendredi", "samedi", "dimanche"],
        "IS":["mánudagur", "þriðjudagur", "miðvikudagur", "fimmtudagur", "föstudagur", "laugardagur", "sunnudagur"],
        "GR":["δευτέρα", "τρίτη", "τετάρτη", "πέμπτη", "παρασκευή", "σάββατο", "κυριακή"],
        "HU":["hétfő", "kedd", "szerda", "csütörtök", "péntek", "szombat", "vasárnap"],
        "IT":["lunedì", "martedì", "mercoledì", "giovedì", "venerdì", "sabato", "domenica"],
        "NL":["maandag", "dinsdag", "woensdag", "donderdag", "vrijdag", "zaterdag", "zondag"],
        "VI":["thứ hai", "thứ ba", "thứ tư", "thứ năm", "thứ sáu", "thứ bảy", "chủ nhật"],
        "PL":["poniedziałek", "wtorek", "środa", "czwartek", "piątek", "sobota", "niedziela"],
        "RO":["luni", "marţi", "miercuri", "joi", "vineri", "sâmbătă", "duminică"],
        "RU":["понедельник", "вторник", "среда", "четверг", "пятница", "суббота", "воскресенье"],
        "SE":["måndag", "tisdag", "onsdag", "torsdag", "fredag", "lördag", "söndag"],
        "SI":["ponedeljek", "torek", "sreda", "četrtek", "petek", "sobota", "nedelja"],
        "SK":["pondelok", "utorok", "streda", "štvrtok", "piatok", "sobota", "nedeľa"]
        }


def weekday(date: str, language: str) -> str:
    if not language in WEEKDAYS:
        return "INVALID_LANGUAGE"

    date_format = "%Y-%m-%d"

    try:
        dash_index = date.index("-")
    except ValueError:
        return "INVALID_DATE"

    if dash_index == 2:
        date_format = "%d-%m-%Y"
    try:
        day_index = datetime.strptime(date, date_format).date().weekday()
    except ValueError:
        return "INVALID_DATE"

    return WEEKDAYS[language][day_index]


def main() -> int:
    cases = int(sys.stdin.readline().rstrip())
    for i in range(cases):
        line = sys.stdin.readline().rstrip()
        date, language = line.split(":")
        print("Case #{}: {}".format(str(i + 1), weekday(date, language)))
    return 0


if __name__ == '__main__':
    sys.exit(main())
