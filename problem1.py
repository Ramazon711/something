# def majority_element(nums: list) -> int:
#     if len(nums) == 0:
#         return -1

#     hisob = {}
#     for son in nums:
#         if son in hisob:
#             hisob[son] = hisob[son] + 1
#         else:
#             hisob[son] = 1

#     eng_kop_son = -1
#     eng_kop_marta = 0
#     for son in hisob:
#         if hisob[son] > eng_kop_marta:
#             eng_kop_marta = hisob[son]
#             eng_kop_son = son

#     return eng_kop_son


# print(majority_element([2, 2, 1, 1, 1, 2, 2]))
# print(majority_element([3, 3, 4]))
# print(majority_element([1, 1, 2, 2, 2, 3]))
# print(majority_element([5, 5, 5, 1, 2]))
# print(majority_element([7]))
# print(majority_element([]))

# 2 - masala

def search_by_genre(cinema: list, genre: str) -> list:
    natija = []
    for film in cinema:
        if film["genre"] == genre:
            natija.append(film)
    return natija