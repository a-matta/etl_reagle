from datetime import date

import pandas as pd
import pytest

from pipeline.etl import SimpleTransformer


@pytest.fixture
def transformer():
    return SimpleTransformer()


@pytest.fixture
def sample_df():
    data = {
        "id": [15811, 15891, 158360],
        "ammattiala": ["Opettaja", "Kirjanpitäjä", "Palomies"],
        "tyotehtava": [
            "Luokanopettaja alkuopetukseen, Martinlaakson koulu",
            "Projektikoordinaattori varhaiskasvatuksen ohjausjärjestelmätukitiimiin",
            "Päätoiminen tuntiopettaja, automaalari, Vantaan ammattiopisto Varia",
        ],
        "tyoavain": [
            "https://vantaa.rekrytointi.com/paikat/?o=A_RJ&jgid=1&jid=15879",
            "https://vantaa.rekrytointi.com/paikat/?o=A_RJ&jgid=1&jid=15841",
            "https://vantaa.rekrytointi.com/paikat/?o=A_RJ&jgid=1&jid=15792",
        ],
        "osoite": ["Mannerheimintie 13, 00100 Helsinki", "Limingantie 18, 90570 Oulu", "Rautatienkatu 3, 20500 Turku"],
        "haku_paattyy_pvm": ["2024-11-04", "2024-10-04", "2024-09-04"],
        "x": ["22.4285719360", "22.6283185307", "22.7298341650"],
        "y": ["60.3928475163", "60.1472583690", "60.4815162342"],
        "linkki": [
            "https://vantaa.rekrytointi.com/paikat/?o=A_RJ&jgid=1&jid=15879",
            "https://vantaa.rekrytointi.com/paikat/?o=A_RJ&jgid=1&jid=15841",
            "https://vantaa.rekrytointi.com/paikat/?o=A_RJ&jgid=1&jid=15792",
        ],
    }
    return pd.DataFrame(data)


def test_rename_columns(transformer, sample_df):
    transformed_df = transformer.transform(sample_df)
    assert list(transformed_df.columns) == list(transformer.rename_schema.values())


def test_transform_dates(transformer, sample_df):
    transformed_df = transformer.transform(sample_df)
    assert isinstance(transformed_df["application_end_date"][0], date)


def test_handle_invalid_date(transformer, sample_df):
    df_invalid_date = sample_df.copy()
    df_invalid_date["haku_paattyy_pvm"][0] = "invalid_date"
    with pytest.raises(ValueError):
        transformer.transform(df_invalid_date)
