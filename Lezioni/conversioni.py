def eur_to_usd(prezzo: float, tasso: float = 1.10) -> float:
    r"""
    Preso in input il prezzo in EUR e il tasso di cambio, lo converte in USD 
    e ritorna tale valore.

    Parameters:

    prezzo (float): il prezzo in euro.
    tasso (float): il tasso di cambio da EUR in USD.

    Returns:
    (float): il prezzo in dollari.
    """
    return prezzo * tasso

def usd_to_eur(prezzo: float, tasso: float = 0.91) -> float:
    r"""
    Preso in input il prezzo in USD e il tasso di cambio, lo converte in EUR 
    e ritorna tale valore.

    Parameters:

    prezzo (float): il prezzo in dollari.
    tasso (float): il tasso di cambio da USD in EUR.

    Returns:
    (float): il prezzo in euro.
    """
    return prezzo * tasso