-- Table: public.soluciones

-- DROP TABLE IF EXISTS public.soluciones;

CREATE TABLE IF NOT EXISTS soluciones
(
    idsolucion serial primary key,
    numreinas int,
    cantidadsoluciones int,
    solucion varchar
)

