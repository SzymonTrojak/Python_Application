def licznik():
    count = 0
    
    def inkrementacja():
        nonlocal count
        count += 1
        return count
    
    return inkrementacja
global_count = 0
def licznik_globalny():
    global global_count
    global_count += 1
    return global_count

class Licznik:
    def __init__(self):
        self.count = 0
    
    def __call__(self):
        self.count += 1
        return self.count

def licznik_atrybut_funkcji():
    if not hasattr(licznik_atrybut_funkcji, 'count'):
        licznik_atrybut_funkcji.count = 0
    licznik_atrybut_funkcji.count += 1
    return licznik_atrybut_funkcji.count

__all__ = ['licznik', 'licznik_globalny', 'Licznik', 'licznik_atrybut_funkcji']