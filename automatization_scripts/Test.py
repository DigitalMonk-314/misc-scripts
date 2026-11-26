def transform(words):
    lst = []
    for word in words:
        res = word.strip('\n')
        end_res = res.strip('\t')
        lst.append(end_res)
    return lst

with open(input(), 'r', encoding='UTF-8') as file:
    result = file.readlines()
    print(transform(result))
#Ну так и почему он не меняется?
