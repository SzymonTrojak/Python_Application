global_count = 0
def licznik_globalny():
    global global_count
    global_count += 1
    return global_count


__all__ = ['licznik_globalny']