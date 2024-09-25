from vectoresNReinas import obtenerResultados
from db import createConnection, getQuerySelect, getQueryInsert
#reinas-env\Scripts\activate

def main(numReinas):
    final = None
    conn = createConnection()
    query = getQuerySelect('soluciones', 'numreinas', numReinas)
    exe = conn.execute(query)
    result = exe.fetchall()
    if len(result) <= 0:
        combinaciones, numResultados = obtenerResultados(numReinas)
        query = getQueryInsert('soluciones', numreinas=numReinas, cantidadsoluciones=numResultados, solucion=combinaciones )
        try:
            exe = conn.execute(query)
            tmp = conn.commit()
        except Exception as e:
            print('Error al insertar en DB. ' + e)
            conn.rollback()
        
        final = (combinaciones, numResultados)

    else:
       
        final = (result[0].t[-1], result[0].t[-2])


    conn.close()
    return final

