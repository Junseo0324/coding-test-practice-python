def solution(sizes):
    width = 0
    height = 0
    for w,h in sizes :
        w, h = max(w,h), min(w,h)
        width = max(width, w)
        height = max(height,h)
    
    return width * height

print(solution([[60, 50], [30, 70], [60, 30], [80, 40]]	))
        