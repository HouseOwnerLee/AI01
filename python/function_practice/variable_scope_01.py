pi = 3.1415

def circle_area_with_pi(r):
    # circle_area_with_pi의 local 영역
    pi = 3.14
    result = pi * (r ** 2)
    return result

def circle_area_without_pi(r):
    # circle_area_without_pi의 local 영역
    result = pi * (r ** 2)
    return result
def sum_areas():
    results = [circle_area_with_pi(3), circle_area_without_pi(3)]
    return sum(results)

def circle_area(r):
    result = 3.14 * (r ** 2)
    return result

if __name__ == '__main__':
    # radius = 3
    # area = circle_area(radius)
    # print("반지름: %d, 면적: %.2f" % (radius, area))

    print("PI:",pi)
    print("반지름:",3,"면적:",circle_area_with_pi(3))
    print("반지름:",3,"면적:",circle_area_without_pi(3))
    print(sum_areas())