row1 = ['O','O','O']
row2 = ['O','O','O']
row3 = ['O','O','O']
map = row1,row2,row3

position = input("Digite uma coluna e uma linha: ")

vertical = int(position[0])
horizontal = int(position[1])

selected_row = map[vertical - 1]
selected_row[horizontal - 1] = 'X'

print(f"{row1}\n{row2}\n{row3}\n")
