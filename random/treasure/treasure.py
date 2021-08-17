emoji1=['😀','😀','😃']
emoji2=['😁','😆','😅']
emoji3=['😂','🤣','😇']

emoji=[emoji1,emoji2,emoji3]

row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map=[row1,row2,row3]


print(f"{row1}\n{row2}\n{row3}\n")


num = input("enter a number between 1 1 and 3 3: ")

row_int = int(num[0]) - 1
column_int = int(num[1]) - 1

map[row_int][column_int] = emoji[row_int][column_int]
print(f"{map[0]}\n{map[1]}\n{map[2]}")



# print(num[0])