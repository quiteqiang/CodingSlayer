def plusOne(digits: List[int]) -> List[int]:
    if digits[0] == 9 and len(digits) == 1:
        return [1, 0]

    if digits[-1] + 1 == 10:
        digits[-1] = 0
        for i in range(len(digits)-2, -1, -1):
            print(digits[i])
            if digits[i] + 1 == 10:
                digits[i] = 0
                if i==0:
                    digits.insert(0, 1)
            else:
                digits[i]+=1
                return digits
    else:
        digits[-1] += 1
        return digits


plusOne([9,9,9])