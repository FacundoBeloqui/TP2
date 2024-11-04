from sqlmodel import Field, SQLModel, Relationship, JSON
from typing import List, Dict, Optional
import sqlalchemy as sa

"""
class PokemonSubidaNivel(SQLModel, table=True):
    id: int = Field(primary_key=True)
    nombre: str
    movimiento_id: int = Field(foreign_key="movimiento.id")
    movimiento: "Movimiento" = Relationship(back_populates="pokemones_subida_nivel")


class PokemonTM(SQLModel, table=True):
    id: int = Field(primary_key=True)
    nombre: str
    movimiento_id: int = Field(foreign_key="movimiento.id")
    movimiento: "Movimiento" = Relationship(back_populates="pokemones_tm")


class PokemonGrupoHuevo(SQLModel, table=True):
    id: int = Field(primary_key=True)
    nombre: str
    movimiento_id: int = Field(foreign_key="movimiento.id")
    movimiento: "Movimiento" = Relationship(back_populates="pokemones_grupo_huevo")
"""


class Naturaleza(SQLModel, table=True):
    id: int = Field(primary_key=True)
    nombre: str
    stat_decreciente: str
    stat_creciente: str
    id_gusto_preferido: int
    id_gusto_menos_preferido: int
    indice_juego: int
    integrantes: List["Integrante"] = Relationship(back_populates="naturaleza")


class PokemonBase(SQLModel):
    identificador: str
    altura: int
    peso: int
    experiencia_base: int
    imagen: str
    grupo_de_huevo: str


class Pokemon(PokemonBase, table=True):
    id: int = Field(primary_key=True)
    id_especie: int
    integrantes: List["Integrante"] = Relationship(back_populates="pokemon")
    habilidades: Optional[List[str]] = Field(default=None, sa_column=sa.Column(JSON))
    evoluciones_inmediatas: Optional[List[str]] = Field(
        default=None, sa_column=sa.Column(JSON)
    )
    tipo: Optional[List[str]] = Field(default=None, sa_column=sa.Column(JSON))
    estadisticas: Optional[Dict[str, int]] = Field(
        default=None, sa_column=sa.Column(JSON)
    )


class PokemonCreate(PokemonBase):
    pass


class IntegranteMovimiento(SQLModel, table=True):
    integrante_id: int = Field(
        nullable=False, foreign_key="integrante.nombre", primary_key=True
    )
    movimiento_id: int = Field(
        nullable=False, foreign_key="movimiento.id", primary_key=True
    )


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

    pokemones_subida_nivel: Optional[List[str]] = Field(
        default=None, sa_column=sa.Column(JSON)
    )
    pokemones_tm: Optional[List[str]] = Field(default=None, sa_column=sa.Column(JSON))
    pokemones_grupo_huevo: Optional[List[str]] = Field(
        default=None, sa_column=sa.Column(JSON)
    )
    integrantes: List["Integrante"] = Relationship(
        back_populates="movimientos",
        link_model=IntegranteMovimiento,
    )


class Integrante(SQLModel, table=True):

    nombre: str = Field(primary_key=True, nullable=False)
    id_equipo: int
    id_pokemon: Optional[int] = Field(default=None, foreign_key="pokemon.id")
    pokemon: Pokemon = Relationship(back_populates="integrantes")
    id_naturaleza: Optional[int] = Field(default=None, foreign_key="naturaleza.id")
    naturaleza: Optional[Naturaleza] = Relationship(back_populates="integrantes")
    movimientos: List[Movimiento] = Relationship(
        back_populates="integrantes",
        link_model=IntegranteMovimiento,
    )