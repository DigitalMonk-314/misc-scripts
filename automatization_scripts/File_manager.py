import sys
num = int(input('Введите порядковый номер: '))
smile = input("Введите смайл: ")
lines = sys.stdin.readlines()
mod_lines = [line.strip() for line in lines if line.strip()]
numbered_lines = []

for line in mod_lines:
    if num > 100:
        num = 1
    numbered_lines.append(f'#{str(num)}. {line}{smile}\n')
    num += 1

with open('Stepic-Next_list1.txt', 'w', encoding='utf-8') as file:
    file.writelines(numbered_lines)

with open('Stepic-Next_list1.txt', 'r', encoding='utf-8') as file:
    print('=== Итоговый файл ===')
    print(file.read())





