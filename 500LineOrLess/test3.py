import numpy as np
from scipy.special import gammaln

'''
    决策取样器
    a rejection sampler
    linked: https://github.com/HT524/500LineorLess_CN/blob/master/%E5%86%B3%E7%AD%96%E9%87%87%E6%A0%B7%E5%99%A8_A_Rejection_Sampler/%E5%86%B3%E7%AD%96%E9%87%87%E6%A0%B7%E5%99%A8_A_Rejection_Sampler.md
'''

class MultinomialDistribution(object):
    def __init__(self, p, rso=np.random):
        if not np.isclose(np.sum(p), 1.0):
            raise ValueError("event probability do not sum to 1")
        self.p = p
        self.rso = rso
        self.logp = np.log(self.p)

    def sample(self, n):
        x = self.rso.multinomial(n, self.p)
        return x

    def log_pmf(self, x):
        n = np.sum(x)
        log_n_factorial = gammaln(n + 1)
        sum_log_xi_factorial = np.sum(gammaln(x + 1))
        log_pi_xi = self.logp * x
        log_pi_xi[x == 0] = 0
        sum_log_pi_xi = np.sum(log_pi_xi)
        log_pmf = log_n_factorial - sum_log_xi_factorial + sum_log_pi_xi
        return log_pmf

    def pmf(self, x):
        pmf = np.exp(self.log_pmf(x))
        return pmf


class MagicItemDistribution(object):
    status_names = ("dexterity", "constitution", "strength", "intelligence", "wisdom", "charisma")

    def __init__(self, bonus_probs, stats_probs, rso=np.random):
        self.bonus_dist = MultinomialDistribution(bonus_probs, rso=rso)
        self.status_dist = MultinomialDistribution(stats_probs, rso=rso)

    def _sample_bonus(self):
        sample = self.bonus_dist.sample(1)
        bonus = np.argmax(sample)
        return bonus

    def _sample_stats(self):
        bonus = self._sample_bonus()
        stats = self.status_dist.sample(bonus)
        return stats

    def sample(self):
        stats = self._sample_stats()
        item_stats = dict(zip(self.status_names, stats))
        return item_stats

    def log_pmf(self, item):
        stats = np.array([item[stat] for stat in self.status_names])
        log_pmf = self._stats_log_pmf(stats)
        return log_pmf

    def pmf(self, item):
        return np.exp(self.log_pmf(item))

    def _stats_log_pmf(self, stats):
        total_bonus = np.sum(stats)
        logp_bonus = self._bonus_log_pmf(total_bonus)
        logp_stats = self.status_dist.log_pmf(stats)
        log_pmf = logp_bonus + logp_stats
        return log_pmf

    def _bonus_log_pmf(self, bonus):
        if bonus < 0 or bonus >= len(self.bonus_dist.p):
            return -np.inf
        x = np.zeros(len(self.bonus_dist.p))
        x[bonus] = 1
        return self.bonus_dist.log_pmf(x)


class DamageDistribution(object):
    def __init__(self, num_items, item_dist, num_dice_sides=12, num_hits=1, rso=np.random):
        self.dice_sides = np.arange(1, num_dice_sides + 1)
        self.dice_dist = MultinomialDistribution(np.ones(num_dice_sides) / float(num_dice_sides), rso=rso)
        self.num_hits = num_hits
        self.num_items = num_items
        self.item_dist = item_dist

    def sample(self):
        items = [self.item_dist.sample() for i in range(self.num_items)]
        num_dice = 1 + np.sum([item['strength'] for item in items])
        dice_rolls = self.dice_dist.sample(self.num_hits * num_dice)
        damage = np.sum(self.dice_sides * dice_rolls)
        return damage


bonus_probs = np.array([0.0, 0.55, 0.25, 0.12, 0.06, 0.02])
stats_probs = np.ones(6) / 6.0
rso = np.random.RandomState(234893)
item_dist = MagicItemDistribution(bonus_probs, stats_probs, rso=rso)
print(item_dist.sample())
damage_dist = DamageDistribution(2, item_dist, num_hits=3, rso=rso)
samples = np.array([damage_dist.sample() for i in range(100000)])

print(samples)
