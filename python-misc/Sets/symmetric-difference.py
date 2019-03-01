if __name__ == '__main__':
    m = int(input())
    m_arr = set(map(int, input().split()))
    n = int(input())
    n_arr = set(map(int, input().split()))

    s_diff = m_arr.difference(n_arr).union(n_arr.difference(m_arr))

    for i in s_diff: print(i)
