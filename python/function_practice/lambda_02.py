def circle_area(radius, print_format):
    area = 3.14 * (radius ** 2)
    print_format(area)

if __name__ == '__main__':
    circle_area(3, lambda x : print("결과값:", round(x, 1)))
    circle_area(3, lambda x : print("결과값:", round(x, 2)))