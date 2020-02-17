from collections import Counter
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    arr1 = arr[::-1]
    for i in range(len(arr1)):
        if arr1[i] != arr1[i+1]:
            print(arr1[i+1]);
            break;
