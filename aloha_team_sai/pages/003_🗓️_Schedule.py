import os
from typing import List

import pandas as pd
import streamlit as st

from metrics.meta import meta_info
from data.SchedulePage import ScheduleElement

DIR_PATH = 'pages/'


def get_filenames() -> List[str]:
    """
    Ruft die Dateinamen im Verzeichnis DIR_PATH ab und gibt sie in sortierter Reihenfolge zurück.
    """
    directory = DIR_PATH
    files = os.listdir(directory)
    return sorted(files)


def extract_information(files: List[str]) -> List[tuple]:
    """
    Extrahiert das Datum und den Titel aus einer Liste von Dateinamen und gibt eine Liste von Tupeln zurück,
    wobei jedes Tupel das Datum und den Titel einer Datei enthält.
    """
    data = []
    for file in files:
        if not file[:2] == "00":
            title = " ".join(file.split("-")[1:]).split(".")[0].replace("_", " ").strip()
            date = " ".join(file.split("_")[1:3]).strip()
            data.append((date, title))
    return data


def show_table(data: List[tuple]) -> None:
    """
    Erstellt eine Pandas-Tabelle aus einer Liste von Tupeln und zeigt sie in Streamlit an.
    """
    df = pd.DataFrame(data, columns=["Datum", "Tagesplan"])
    df.set_index("Datum", inplace=True)
    st.table(df)


def main() -> None:
    """
    Ruft die Dateinamen ab, extrahiert das Datum und den Titel aus den Dateinamen und zeigt sie in einer Tabelle in Streamlit an.
    """
    meta_info()
    intro = ScheduleElement(text_path="texts/schedule_intro.md")
    intro.show()
    
    files = get_filenames()
    data = extract_information(files=files)
    show_table(data=data)
    


if __name__ == "__main__":
    main()

