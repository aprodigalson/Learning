import xlwt


# write data ,make it horizontal left
def horizontal_left(x, y, d, t):
    align = xlwt.Alignment()
    align.horz = xlwt.Alignment.HORZ_LEFT
    style = xlwt.XFStyle()
    style.alignment = align
    t.write(x, y, d, style)

# write data ,make it horizontal right
def horizontal_left(x, y, d, t):
    align = xlwt.Alignment()
    align.horz = xlwt.Alignment.HORZ_RIGHT
    style = xlwt.XFStyle()
    style.alignment = align
    t.write(x, y, d, style)


# demo 14
def txt_to_xls():
    with open('student.txt', 'r', encoding='utf-8') as f:
        data = f.read()
    _student = eval(data)
    student = list()
    for i in range(1, 4):
        info = _student[str(i)]
        student.append(i)
        student.extend(info)
    row = len(_student) / len(student)
    file = xlwt.Workbook()
    table = file.add_sheet('student')
    for i in range(len(student)):
        if not i % 5:
            horizontal_left(i // 5, i % 5, student[i], table)
        else:
            table.write(i // 5, i % 5, student[i])
    file.save('student.xls')


# demo 15
def txt_to_xls1():
    with open('city.txt') as file:
        data = file.read()
    _city = eval(data)
    print(_city)
    city = _city
    file = xlwt.Workbook()
    table = file.add_sheet('city')
    for index, item in enumerate(city.items()):
        table.write(index, 0, item[0])
        table.write(index, 1, item[1])
    file.save("city.xls")


# demo 16
def txt_to_xls2():
    with open('numbers.txt') as file:
        data = file.read()
    _number = eval(data)
    print(_number)
    number = _number
    file = xlwt.Workbook()
    table = file.add_sheet('numbers')
    for index, item in enumerate(number):
        table.write(index, 0, item[0])
        table.write(index, 1, item[1])
        table.write(index, 2, item[2])
    file.save("numbers.xls")


txt_to_xls2()
