def licznik_atrybut_funkcji():
    if not hasattr(licznik_atrybut_funkcji, 'count'):
        licznik_atrybut_funkcji.count = 0
    licznik_atrybut_funkcji.count += 1
    return licznik_atrybut_funkcji.count

__all__ = ['licznik_atrybut_funkcji']