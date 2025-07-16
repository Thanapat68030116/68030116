import math

a = float(input("กรอกความยาวด้าน a: "))
b = float(input("กรอกความยาวด้าน b: "))
c = float(input("กรอกความยาวด้าน c: "))

if a + b > c and a + c > b and b + c > a:
    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    print(f"พื้นที่ของสามเหลี่ยมคือ {area:.2f}")
else:
    print("ไม่สามารถสร้างสามเหลี่ยมจากด้านที่ระบุได้")