from fastapi.testclient import TestClient
from main import app
from db import lista_naturalezas
import pytest
from routes.teams.teams import lista_equipos


client = TestClient(app)


@pytest.fixture(autouse=True)
def reset_lista_equipos():
    global lista_equipos
    lista_equipos.clear()  # Reiniciar la lista antes de cada prueba
    yield
    lista_equipos.clear()  # Limpia después de la prueba


def test_no_hay_equipos():
    response = client.get("/teams")
    assert response.status_code == 404
    assert response.json() == {"detail": "No se encontraron equipos creados"}


def test_pagina_invalida_cero():
    lista_equipos.extend(
        [
            "Equipo 1",
            "Equipo 2",
            "Equipo 3",
            "Equipo 4",
            "Equipo 5",
            "Equipo 6",
            "Equipo 7",
            "Equipo 8",
            "Equipo 9",
            "Equipo 10",
            "Equipo 11",
        ]
    )
    response = client.get("/teams", params={"pagina": 0})
    assert response.status_code == 400
    assert response.json() == {
        "detail": "Error en el ingreso. La pagina debe ser un entero mayor a cero"
    }


def test_pagina_invalida_menor_que_uno():
    lista_equipos.extend(
        [
            "Equipo 1",
            "Equipo 2",
            "Equipo 3",
            "Equipo 4",
            "Equipo 5",
            "Equipo 6",
            "Equipo 7",
            "Equipo 8",
            "Equipo 9",
            "Equipo 10",
            "Equipo 11",
        ]
    )
    response = client.get("/teams", params={"pagina": -21})
    assert response.status_code == 400
    assert response.json() == {
        "detail": "Error en el ingreso. La pagina debe ser un entero mayor a cero"
    }


def test_pagina_no_encontrada():
    global lista_equipos
    lista_equipos.extend(["Equipo 1", "Equipo 2"])  # Solo 2 equipos para esta prueba
    response = client.get("/teams", params={"pagina": 2})  # No hay suficientes equipos
    assert response.status_code == 404
    assert response.json() == {"detail": "No se encontro la pagina solicitada"}


def test_obtener_equipos_pagina_1():
    global lista_equipos
    lista_equipos.extend(
        [
            "Equipo 1",
            "Equipo 2",
            "Equipo 3",
            "Equipo 4",
            "Equipo 5",
            "Equipo 6",
            "Equipo 7",
            "Equipo 8",
            "Equipo 9",
            "Equipo 10",
            "Equipo 11",
        ]
    )  # Agregamos 11 equipos para la prueba
    response = client.get("/teams", params={"pagina": 1})
    assert response.status_code == 200
    assert (
        response.json() == lista_equipos[:10]
    )  # Debería devolver los primeros 10 equipos


def test_obtener_equipos_pagina_2():
    global lista_equipos
    lista_equipos.extend(
        [
            "Equipo 1",
            "Equipo 2",
            "Equipo 3",
            "Equipo 4",
            "Equipo 5",
            "Equipo 6",
            "Equipo 7",
            "Equipo 8",
            "Equipo 9",
            "Equipo 10",
            "Equipo 11",
        ]
    )
    response = client.get("/teams", params={"pagina": 2})
    assert response.status_code == 200
    assert response.json() == lista_equipos[10:]  # Debería devolver el último equipo


def test_pagina_excesiva():
    global lista_equipos
    lista_equipos.extend(
        [
            "Equipo 1",
            "Equipo 2",
            "Equipo 3",
            "Equipo 4",
            "Equipo 5",
            "Equipo 6",
            "Equipo 7",
            "Equipo 8",
            "Equipo 9",
            "Equipo 10",
            "Equipo 11",
        ]
    )
    response = client.get("/teams", params={"pagina": 3})  # Pagina que no existe
    assert response.status_code == 404
    assert response.json() == {"detail": "No se encontro la pagina solicitada"}


def test_leer_naturalezas():
    response = client.get("/teams/nature")
    assert response.status_code == 200
    content = response.json()
    assert isinstance(content, list)
    if lista_naturalezas:
        assert len(content) == len(lista_naturalezas)
        primera_naturaleza = content[0]
        assert primera_naturaleza["id"] == lista_naturalezas[0].id
        assert primera_naturaleza["nombre"] == lista_naturalezas[0].nombre
        assert (
            primera_naturaleza["stat_decreciente"]
            == lista_naturalezas[0].stat_decreciente
        )
        assert (
            primera_naturaleza["stat_creciente"] == lista_naturalezas[0].stat_creciente
        )
        assert (
            primera_naturaleza["id_gusto_preferido"]
            == lista_naturalezas[0].id_gusto_preferido
        )
        assert (
            primera_naturaleza["id_gusto_menos_preferido"]
            == lista_naturalezas[0].id_gusto_menos_preferido
        )
        assert primera_naturaleza["indice_juego"] == lista_naturalezas[0].indice_juego
