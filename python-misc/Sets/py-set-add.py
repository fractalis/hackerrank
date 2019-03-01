if __name__ == '__main__':
    countries = set()
    n = int(input())
    for _ in range(n):
        country = input()
        countries.add(country)
    print(len(countries))
