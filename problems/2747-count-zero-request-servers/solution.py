from typing import List


class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
        logs.sort(key=lambda log: log[1])
        # Офлайн: обходим запросы по возрастанию времени, но ответ кладём на исходное место.
        order = sorted(range(len(queries)), key=queries.__getitem__)

        cnt = [0] * (n + 1)  # cnt[s] — сколько логов сервера s сейчас в окне
        active = 0           # сколько серверов имеют cnt > 0
        left = right = 0
        ans = [0] * len(queries)
        for qi in order:
            start, end = queries[qi] - x, queries[qi]
            # Правая граница: добавляем логи со временем <= end.
            while right < len(logs) and logs[right][1] <= end:
                server = logs[right][0]
                if cnt[server] == 0:
                    active += 1
                cnt[server] += 1
                right += 1
            # Левая граница: убираем логи со временем < start.
            while left < right and logs[left][1] < start:
                server = logs[left][0]
                cnt[server] -= 1
                if cnt[server] == 0:
                    active -= 1
                left += 1
            ans[qi] = n - active
        return ans


def brute(n, logs, x, queries):
    return [n - len({s for s, t in logs if q - x <= t <= q}) for q in queries]


if __name__ == "__main__":
    import random

    s = Solution()
    assert s.countServers(3, [[1, 3], [2, 6], [1, 5]], 5, [10, 11]) == [1, 2]
    assert s.countServers(3, [[2, 4], [2, 1], [1, 2], [3, 1]], 2, [3, 4]) == [0, 1]
    for _ in range(1000):
        n = random.randint(1, 5)
        logs = [[random.randint(1, n), random.randint(1, 15)] for _ in range(random.randint(1, 10))]
        x = random.randint(1, 5)
        queries = [random.randint(x + 1, 20) for _ in range(random.randint(1, 6))]
        assert s.countServers(n, [l[:] for l in logs], x, queries) == brute(n, logs, x, queries)
    print("OK")
