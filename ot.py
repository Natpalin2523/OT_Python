a = int(50) # ot ชั่วโมงละ 50 บาท
print('---------------โปรแกรมคำนวณ OT-------------------')
try:
    salary = int(input('กรุณาป้อนเงินเดือนของคุณ: '))
    ot = int(input('จำนวนชั่วโมงที่ทำงานนอกเวลา: '))
except:
    print('กรุณากรอกข้อมูลเป็นตัวเลขเท่านั้น!!!!! ')
    salary = int(input('กรุณาป้อนเงินเดือนของคุณ: '))
    ot = (input('จำนวนชั่วโมงที่ทำงานนอกเวลา: '))

print('----------------Calculate--------------')
total_salary = (salary+(ot*a))
print(f'เงินเดือนของคุณ: {salary}  บาท' )
print(f'จำนวนชั่วโมงที่ทำงานนอกเวลา {ot}  ชั่วโมง ')
print('----------คำนวณ------------')
print('เงินเดือนทั้งหมดที่คุณจะได้รับ {} บาท' .format(total_salary))

