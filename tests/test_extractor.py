from typing import Any
from unittest.mock import Mock, patch

import pandas as pd
import pytest

from pipeline.etl import SimpleExtractor


@pytest.fixture
def mock_response():
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = [
        {
            "id": 15839,
            "organisaatio": "Kasvatus ja oppiminen, Varhaiskasvatus",
            "ammattiala": "Hallinto-, esimies- ja asiantuntijatyö",
            "tyotehtava": "Varhaiskasvatuspäällikkö",
            "tyoavain": "https://vantaa.rekrytointi.com/paikat/?o=A_RJ&jgid=1&jid=15839",
            "osoite": "Silkkitehtaantie 5C, 01300 Vantaa",
            "haku_paattyy_pvm": "2024-12-05",
            "x": 25.036196681892456,
            "y": 60.28870816893006,
            "linkki": "https://vantaa.rekrytointi.com/paikat/?o=A_RJ&jgid=1&jid=15839",
        },
    ]
    return mock_response


@patch("requests.get")
def test_extract(mock_get, mock_response: Any):
    mock_get.return_value = mock_response
    extractor = SimpleExtractor("https://dummy.com")
    df = extractor.extract()

    assert isinstance(df, pd.DataFrame)
    print(df.shape)
    print(df.columns.tolist())
    assert df.shape == (1, 10)
    assert df.columns.tolist() == [
        "id",
        "organisaatio",
        "ammattiala",
        "tyotehtava",
        "tyoavain",
        "osoite",
        "haku_paattyy_pvm",
        "x",
        "y",
        "linkki",
    ]
