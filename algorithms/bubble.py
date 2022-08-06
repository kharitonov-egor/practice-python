def main():
    a = []

    n = int(input())

    for i in range(n):
        a.append(int(input()))
        
    for i in range(len(a)):
        for j in range(i+1,len(a)):
            if a[i] > a[j]:
                a[i],a[j] = a[j],a[i]

    print(a)

if __name__ == "__main__":
    main()
