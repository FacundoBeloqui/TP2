from typing import List, Dict, Optional

from pydantic import BaseModel
from sqlmodel import Field, SQLModel, Relationship


class PokemonBase(SQLModel):
    identificador: str
    altura: int
    peso: int
    experiencia_base: int
    imagen: str
    tipo: list[str]
    grupo_de_huevo: str
    estadisticas: dict
    habilidades: list[str]
    evoluciones_inmediatas: list


class Pokemon(PokemonBase, table=True):
    id: int = Field(primary_key=True)
    id_especie: int


class PokemonCreate(PokemonBase):
    pass


class Movimiento(SQLModel, table=True):
    id: int = Field(primary_key=True)
    nombre: str
    generacion: int
    tipo: str
    poder: str
    accuracy: str
    pp: str
    generacion: int
    categoria: str
    efecto: str
    pokemones_subida_nivel: List[str]
    pokemones_tm: List[str]
    pokemones_grupo_huevo: List[str]


class PokemonTeamCreate(SQLModel):
    id: int
    nombre: str
    movimientos: List[Optional[int]]
    naturaleza_id: int
    stats: dict

class TeamBase(SQLModel):
    generacion: int
    nombre: str
    pokemones: List[PokemonTeamCreate] = Relationship(back_populates="team")

class TeamDataCreate(TeamBase, table=True):
    id: int = Field(primary_key=True)
    # nombre: str
    # generacion: int
    # pokemones: List[PokemonTeamCreate]

# class TeamCreate(TeamBase):
#     pass


class Naturaleza(SQLModel, table=True):
    id: int = Field(primary_key=True)
    nombre: str
    stat_decreciente: str
    stat_creciente: str
    id_gusto_preferido: int
    id_gusto_menos_preferido: int
    indice_juego: int


class Teams(BaseModel):
    id: int
    nombre: str
    pokemones: List[str]


class Movimientomoves(BaseModel):
    id: int
    nombre: str
    nivel: Optional[int] = None
    es_evolucionado: bool = False


class Pokemonmoves(BaseModel):
    id: int
    nombre: str
    tipos: List[int]


class Evolucion(BaseModel):
    id_pokemon_base: int
    id_pokemon_evolucionado: int


class DatosMovimiento(BaseModel):
    movimientos: Dict[int, Movimiento]


class PokemonTeam(BaseModel):
    id: int
    nombre: str
    movimiento_1: Optional[int]
    movimiento_2: Optional[int]
    movimiento_3: Optional[int]
    movimiento_4: Optional[int]
    naturaleza_id: int
    stats: dict


class Team(BaseModel):
    id: int
    generacion: int
    nombre: str
    pokemon_1: Optional[PokemonTeam]
    pokemon_2: Optional[PokemonTeam]
    pokemon_3: Optional[PokemonTeam]
    pokemon_4: Optional[PokemonTeam]
    pokemon_5: Optional[PokemonTeam]
    pokemon_6: Optional[PokemonTeam]


lista_equipos: List[TeamDataCreate] = [
    {
        "id": 1,
        "nombre": "Equipo A",
        "generacion": 1,
        "pokemones": [
            {
                "id": 1,
                "nombre": "Pikachu",
                "movimientos": [1, 2],
                "naturaleza_id": 1,
                "stats": {},
            }
        ],
    },
    {
        "id": 2,
        "nombre": "Equipo B",
        "generacion": 2,
        "pokemones": [
            {
                "id": 2,
                "nombre": "Charmander",
                "movimientos": [2],
                "naturaleza_id": 1,
                "stats": {},
            }
        ],
    },
]

# lista_equipos: List[TeamDataCreate] = []