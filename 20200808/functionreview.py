# def mean4(mw, sk, yc, jl):
#     sum = mw + sk + yc +jl
#     return sum/4
#
# print( mean4(3, 8, mean4(1,3,2,6), 9))

def teemoDies (damage):
    teemoHealth = 500
    if (teemoHealth > damage):
        return "alive"
    else :
        return "dead"

damage = input("type the damage you dealth to teemo! ")
damage = int(damage)
print(teemoDies(damage))
