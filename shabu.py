print('-----------------โปรแกรมคำนวณค่าชาบู---------------')
try:
    price = int(input('โปรดระบุราคาต่อหัว'))
    person = int(input('จำนวนคน'))
except:
    print('กรุณากรอกข้อมูลที่เป็นตัวเลขเท่านั้น!!')
    price = int(input('โปรดระบุราคาต่อหัว'))
    person = int(input('จำนวนคน'))

print('---------------Calculate------------------')
total_price = price*person
print (f'โปรดระบุราคาต่อหัว: {price}  บาท')
print (f'จำนวนคน: {person}  คน')
print ('จำนวนเงินที่ต้องจ่าย: {} บาท'.format(total_price))



