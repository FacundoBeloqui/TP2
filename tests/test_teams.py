from fastapi.testclient import TestClient
from unittest.mock import patch
from main import app

client = TestClient(app)


def test_obtener_todos_los_equipos_vacia():
    with patch("routes.teams.teams.lista_equipos", new=[]):
        response = client.get("/teams/?pagina=1")
        assert response.status_code == 404
        assert response.json() == {"detail": "No se encontraron equipos creados"}


def test_obtener_todos_los_equipos_pagina_existente():
    with patch(
        "routes.teams.teams.lista_equipos",
        new=[f"Equipo {i}" for i in range(1, 26)],
    ):
        response = client.get("/teams/?pagina=1")
        assert response.status_code == 200
        assert response.json() == [f"Equipo {i}" for i in range(1, 11)]


def test_obtener_todos_los_equipos_pagina_no_existente():
    with patch(
        "routes.teams.teams.lista_equipos",
        new=[f"Equipo {i}" for i in range(1, 26)],
    ):
        response = client.get("/teams/?pagina=4")
        assert response.status_code == 404
        assert response.json() == {"detail": "No se encontro la pagina solicitada"}


def test_obtener_todos_los_equipos_pagina_invalida():
    with patch(
        "routes.teams.teams.lista_equipos",
        new=[f"Equipo {i}" for i in range(1, 26)],
    ):
        response = client.get("/teams/?pagina=-1")
        assert response.status_code == 400
        assert response.json() == {
            "detail": "Error en el ingreso. La pagina debe ser un entero mayor a cero"
        }


def test_obtener_todos_los_equipos_pagina_con_diez():
    with patch(
        "routes.teams.teams.lista_equipos",
        new=[f"Equipo {i}" for i in range(1, 11)],
    ):
        response = client.get("/teams/?pagina=1")
        assert response.status_code == 200
        assert response.json() == [f"Equipo {i}" for i in range(1, 11)]
