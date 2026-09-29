# Fichier : fonction.py


def addition(a: float, b: float) -> float:
    return a + b


def soustraction(a: float, b: float) -> float:
    return a - b


def multiplication(a: float, b: float) -> float:
    return a * b


def division(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("Division par zéro impossible")
    return a / b