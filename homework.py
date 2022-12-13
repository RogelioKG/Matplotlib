from typing import Callable
import pylab as pl

def Riemann_Sum(func: Callable, interval: tuple, piece: int = 100, *, rule: str) -> float:
    start, end = interval
    dx = (end - start) / piece
    total = 0

    if rule == "left":
        for _ in range(piece):
            total += func(start) * dx
            start += dx
    elif rule == "right":
        for _ in range(piece):
            total += func(start + dx) * dx
            start += dx
    elif rule == "mid":
        for _ in range(piece):
            total += func(start + 0.5*dx) * dx
            start += dx
    elif rule == "trapezoid":
        for _ in range(piece):
            total += (func(start) + func(start + dx)) * dx / 2
            start += dx

    return total

def Rectangle_Formula(func: Callable, interval: tuple, piece: int = 100) -> float:
    start, end = interval
    dx = (end - start) / piece
    return dx * sum(func(start + (i+0.5)*dx) for i in range(piece))

def Trapezoid_Formula(func: Callable, interval: tuple, piece: int = 100) -> float:
    start, end = interval
    dx = (end - start) / piece
    return (1/2) * dx * (func(start) + sum(2*func(start + i*dx) for i in range(1, piece)) + func(end))

def Simpson_Formula(func: Callable, interval: tuple, piece: int = 100) -> float:
    start, end = interval
    h = (end - start) / (2 * piece)
    return (1/3) * h * (func(start) + sum(4*func(start + i*h) if i%2 else 2*func(start + i*h) for i in range(1, 2*piece)) + func(end))


def f(x: float) -> float:
    return (7 ** pl.cos(x)) * pl.sin(x)


interval = (0, pl.pi/2)
real_value = 3.083390054
print(f"數學積分     : {real_value:.9f}")


print("迴圈求積:")
# 矩形積分
mid = Riemann_Sum(f, interval, rule="mid")
print(f"矩形積分     : {mid:.9f}  誤差: {abs(real_value-mid)}")
# 上矩形積分
right = Riemann_Sum(f, interval, rule="right")
print(f"上矩形積分   : {right:.9f}  誤差: {abs(real_value-right)}")
# 下矩形積分
left = Riemann_Sum(f, interval, rule="left")
print(f"下矩形積分   : {left:.9f}  誤差: {abs(real_value-left)}")
# 梯形積分
trapezoid = Riemann_Sum(f, interval, rule="trapezoid")
print(f"梯形積分     : {trapezoid:.9f}  誤差: {abs(real_value-trapezoid)}")


print("公式求積:")
# 矩形求積法
R = Rectangle_Formula(f, interval)
print(f"矩形積分法   : {R:.9f}  誤差: {abs(real_value-R)}")
# 梯形積分法
T = Trapezoid_Formula(f, interval)
print(f"梯形積分法   : {T:.9f}  誤差: {abs(real_value-T)}")
# Simpson積分
S = Simpson_Formula(f, interval)
print(f"Simpson積分法: {S:.9f}  誤差: {abs(real_value-S)}")
