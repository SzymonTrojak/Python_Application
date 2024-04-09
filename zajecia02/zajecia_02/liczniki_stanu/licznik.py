def licznik():
    count = 0
    
    def inkrementacja():
        nonlocal count
        count += 1
        return count
    
    return inkrementacja

__all__ = ['licznik']