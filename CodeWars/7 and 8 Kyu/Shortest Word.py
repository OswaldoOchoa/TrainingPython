def find_short(s):
    lista = s.split()
    return len(min(lista, key=len))