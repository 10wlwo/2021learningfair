import turtle

def won() :
    turtle.penup()
    turtle.goto(-200,0)
    turtle.pendown()
    turtle.pensize(5)
    turtle.circle(70,360)

def sam() :
    turtle.penup()
    turtle.goto(-100,0)
    turtle.pendown()
    turtle.pensize(5)
    turtle.forward(150)
    turtle.left(120)
    turtle.forward(150)
    turtle.left(120)
    turtle.forward(150)
    turtle.left(120)
    

def sa() :
    turtle.penup()
    turtle.goto(100,0)
    turtle.pendown()
    turtle.pensize(5)
    turtle.forward(130)
    turtle.left(90)
    turtle.forward(130)
    turtle.left(90)
    turtle.forward(130)
    turtle.left(90)
    turtle.forward(130)
    turtle.left(90)



won()
sam()
sa()


print("○△□ 지금부터 도형 게임을 시작합니다. ○△□")
print()
name=input("참가자의 이름을 입력해주십시오.: ")
print()
qu=input("제 1라운드: 원, 삼각형, 사각형 중 넓이를 구하고 싶은 도형을 골라주십시오.: ")

if "원" in qu :
    r=eval(input("제 2라운드: 반지름의 길이를 입력해 주십시오.: "))
    print()
    print("-----------------------------------------------------------")
    print("[게임 통과!] 최종 우승자", name, "님은 최후의 1인이 되셨습니다.")
    print()
    print("방금 구한 원의 넓이만큼 상금을 드리겠습니다.")
    print("총 상금은", r*r*3.14, "입니다. 축하합니다.")

if "삼각형" in qu :
    l=eval(input("제 2라운드: 밑변의 길이를 입력해 주십시오.: "))
    h=eval(input("제 3라운드: 높이를 입력해 주십시오.: "))
    print()
    print("-----------------------------------------------------------")
    print("[게임 통과!] 최종 우승자", name, "님은 최후의 1인이 되셨습니다.")
    print()
    print("방금 구한 삼각형의 넓이만큼 상금을 드리겠습니다.")
    print("총 상금은", l*h/2, "입니다. 축하합니다.")

if "사각형" in qu :
    a=eval(input("제 2라운드: 가로의 길이를 입력해 주십시오.: "))
    b=eval(input("제 3라운드: 세로의 길이를 입력해 주십시오.: "))
    print()
    print("-----------------------------------------------------------")
    print("[게임 통과!] 최종 우승자", name, "님은 최후의 1인이 되셨습니다.")
    print()
    print("방금 구한 사각형의 넓이만큼 상금을 드리겠습니다.")
    print("총 상금은", a*b, "입니다. 축하합니다.")
    
          



