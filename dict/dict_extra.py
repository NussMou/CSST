# key 必須是不可變的(immutable)
# 與hash有關，若地址相同值不同，hash 的 value 被裡面值的改變影響，可能會出錯
# 若地址不同，就會直接hash一個新的，不會有衝突或出錯的可能
# 結論 list 不可為 key

a = {}
l = [1,2,3]
a[l] = 1

print(a)
