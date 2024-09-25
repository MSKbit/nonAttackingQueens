

from coordenada import coordenada

arrSolucion = []
arrSolucionTemp = []

def obtenerResultados(numReinas):
    combinaciones = nonAttackingQueens(numReinas)
    strResultado = ''

    for index, solucion in  enumerate(arrSolucion):
        tempSol = 'Solución: ' + str(index+1)
        strResultado += tempSol + '\\n'

        for elem in solucion:
            tempString = 'Fila: ' + str(elem.fila) + ' | Columna: ' + str(elem.columna) +' '
            strResultado += tempString

        tempSol = '\\n\\n'
        strResultado += tempSol


    return strResultado, combinaciones





def nonAttackingQueens(n):
    blockedColumns = set()
    blockedUpDiagonals = set()
    blockedDownDiagonals = set()
    return getNumberOfNonAttackingQueenPlacements(0, blockedColumns, blockedUpDiagonals, blockedDownDiagonals, n)

def getNumberOfNonAttackingQueenPlacements(row, blockedColumns, blockedUpDiagonals, blockedDownDiagonals, boardSize):
    if row == boardSize:
        return 1

    validPlacements = 0
    for col in range(boardSize):
        if isNonAttackingPlacement(row, col, blockedColumns, blockedUpDiagonals, blockedDownDiagonals):
            placeQueen(row, col, blockedColumns, blockedUpDiagonals, blockedDownDiagonals)
            resultado = getNumberOfNonAttackingQueenPlacements(row+1, blockedColumns, blockedUpDiagonals, blockedDownDiagonals, boardSize)
            validPlacements += resultado
            if resultado>0 and len(arrSolucionTemp)==boardSize:
                arrSolucion.append(arrSolucionTemp.copy())
            removeQueen(row, col, blockedColumns, blockedUpDiagonals, blockedDownDiagonals)

    return validPlacements

def isNonAttackingPlacement(row, col, blockedColumns, blockedUpDiagonals, blockedDownDiagonals):
    if col in blockedColumns:
        return False
    
    if row + col in blockedUpDiagonals:
        return False
    
    if row - col in blockedDownDiagonals:
        return False
    
    return True


def placeQueen(row, col, blockedColumns, blockedUpDiagonals, blockedDownDiagonals):
    blockedColumns.add(col)
    blockedUpDiagonals.add(row+col)
    blockedDownDiagonals.add(row-col)
    arrSolucionTemp.append(coordenada(row,col))

def removeQueen(row, col, blockedColumns, blockedUpDiagonals, blockedDownDiagonals):
    blockedColumns.remove(col)
    blockedUpDiagonals.remove(row+col)
    blockedDownDiagonals.remove(row-col)
    arrSolucionTemp.pop()




