import Parameters as P
import HW8 as Cls
import SupportTransientState as Support

# create multiple cohorts for when the coin is fair
multiCohortFairCoin = Cls.MultipleGameSets(
    ids=range(P.NUM_SIM_COHORTS),   # [0, 1, 2 ..., NUM_SIM_COHORTS-1]
    n_games_in_a_set=[P.REAL_POP_SIZE] * P.NUM_SIM_COHORTS,  # [REAL_POP_SIZE, REAL_POP_SIZE, ..., REAL_POP_SIZE]
    prob_head=[P.prob_head]*P.NUM_SIM_COHORTS  # [p, p, ...]
)
# simulate all cohorts
multiCohortFairCoin.simulation()

# create multiple cohorts for when the coin is weighted and unfair
multiCohortWithUnfairCoin = Cls.MultipleGameSets(
    ids=range(P.NUM_SIM_COHORTS, 2*P.NUM_SIM_COHORTS),   # [NUM_SIM_COHORTS, NUM_SIM_COHORTS+1, NUM_SIM_COHORTS+2, ...]
    n_games_in_a_set=[P.REAL_POP_SIZE] * P.NUM_SIM_COHORTS,  # [REAL_POP_SIZE, REAL_POP_SIZE, ..., REAL_POP_SIZE]
    prob_head=[P.prob_head2]*P.NUM_SIM_COHORTS
)
# simulate all cohorts
multiCohortWithUnfairCoin.simulation()
print("Hmwk Q2")

# print outcomes of each cohort
Support.print_outcomes(multiCohortFairCoin, 'When you use the fair coin:')
Support.print_outcomes(multiCohortWithUnfairCoin, 'When you use the trick coin:')

# print comparative outcomes
Support.print_comparative_outcomes(multiCohortFairCoin, multiCohortWithUnfairCoin)
