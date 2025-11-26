import random


def main():
    totalGames = 100000
    results = simulateGames(totalGames)

    for combination, count in sorted(results.items(),
                                     key=lambda x: -x[1]):
        percent = (count / totalGames) * 100
        print(f"{combination:20s}: {count:8d}  ({percent:6.4f}%)")


def simulateGames(gameCount):
    combinations = {
        "Royal Flush": 0,
        "Straight Flush": 0,
        "Four of a Kind": 0,
        "Full House": 0,
        "Flush": 0,
        "Straight": 0,
        "Three of a Kind": 0,
        "Two Pair": 0,
        "One Pair": 0,
        "High Card": 0
    }

    for _ in range(gameCount):
        hand = drawUniqueValues(52, 5)
        combo = detectCombination(hand)
        combinations[combo] += 1

    return combinations


def drawUniqueValues(poolSize, drawCount):
    pool = list(range(poolSize))
    results = []

    for i in range(drawCount):
        index = random.randint(0, poolSize - 1 - i)
        results.append(pool[index])
        pool[index], pool[poolSize - 1 - i] = (pool[poolSize - 1 - i], pool[index])
    return results


def getRanks(hand):
    return [card % 13 for card in hand]


def getSuits(hand):
    return [card // 13 for card in hand]


def countRanks(hand):
    counts = {}
    for rank in getRanks(hand):
        counts[rank] = counts.get(rank, 0) + 1
    return counts


def isPair(hand):
    return list(countRanks(hand).values()).count(2) == 1


def isTwoPair(hand):
    return list(countRanks(hand).values()).count(2) == 2


def isThreeOfKind(hand):
    return 3 in countRanks(hand).values()


def isFourOfKind(hand):
    return 4 in countRanks(hand).values()


def isFullHouse(hand):
    values = countRanks(hand).values()
    return 3 in values and 2 in values


def isFlush(hand):
    suits = getSuits(hand)
    return len(set(suits)) == 1


def isStraight(hand):
    ranks = sorted(getRanks(hand))

    #ternärerOperator
    return True if ranks == [0, 1, 2, 3, 12] \
        else all(ranks[i] + 1 == ranks[i + 1] for i in range(4))


def isStraightFlush(hand):
    return isStraight(hand) and isFlush(hand)


def isRoyalFlush(hand):
    ranks = sorted(getRanks(hand))
    return isFlush(hand) and ranks == [8, 9, 10, 11, 12]


def detectCombination(hand):
    if isRoyalFlush(hand):
        return "Royal Flush"
    if isStraightFlush(hand):
        return "Straight Flush"
    if isFourOfKind(hand):
        return "Four of a Kind"
    if isFullHouse(hand):
        return "Full House"
    if isFlush(hand):
        return "Flush"
    if isStraight(hand):
        return "Straight"
    if isThreeOfKind(hand):
        return "Three of a Kind"
    if isTwoPair(hand):
        return "Two Pair"

    #ternärer Operator (dict)
    return {True: "One Pair", False: "High Card"}[isPair(hand)]


if __name__ == "__main__":
    main()
