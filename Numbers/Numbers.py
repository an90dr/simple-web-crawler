import math
class Numbers:

    def percentage(numerator: int, denominator: int) -> float:
        return numerator/denominator*100

    def resolveProgress(numerator: int, denominator: int) -> str:
        factor = 10 ** 2
        perc = math.floor(Numbers.percentage(numerator, denominator) * factor) / factor
        return str(str(numerator) + " / " + str(denominator)) + ' (' + str(perc) + '%)'
