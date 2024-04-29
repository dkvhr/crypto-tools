from factordb.factordb import FactorDB

def factor(n):
    # Testing if we have the factors on FactorDB first
    f = FactorDB(n)
    f.connect()
    res = f.get_factor_list()
