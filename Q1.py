# 如下代码用于判断奇偶数
numbers = [12, 37, 5, 42, 8, 3];
even = [];
odd = [];
while len(numbers) > 0:
    number = numbers.pop()
    if(number % 2 == 0):
        even.append(number)
    else:
        odd.append(number)
print( "even: ", even)
print("odd: ", odd)
