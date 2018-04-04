import scr.FormatFunctions as Format
import scr.StatisticalClasses as Stat
import Parameters as P

def print_outcomes(multi_cohort, strategy_name):
    """ prints the outcomes of a simulated cohort under steady state
    :param multi_cohort: output of a simulated cohort
    :param strategy_name: the name of the selected therapy
    """

    # mean and confidence interval text of patient survival time
    reward_mean_PI_text = Format.format_estimate_interval(
        estimate=multi_cohort.get_mean_mean_reward(),
        interval=multi_cohort.get_PI_mean_reward(alpha=P.ALPHA),
        deci=1)

    # print survival time statistics
    print(strategy_name)
    print("  Estimate of mean reward ($) and {:.{prec}%} prediction interval:".format(1 - P.ALPHA, prec=0),
          reward_mean_PI_text)

def print_comparative_outcomes(multi_cohort_fair_coin, multi_cohort_unfair_coin):
    """ prints expected and percentage increase in average survival time when drug is available
    :param multi_cohort_fair_coin: multiple cohorts simulated the coin is fair
    :param multi_cohort_unfair_coin: multiple cohorts simulated when the coin is unfair and weighted
    """

    # increase in survival time
    increase = Stat.DifferenceStatIndp(
        name='Increase in mean reward',
        x=multi_cohort_unfair_coin.get_mean_Rewards(),
        y_ref=multi_cohort_fair_coin.get_mean_Rewards()
    )
    # estimate and prediction interval
    estimate_CI = Format.format_estimate_interval(
        estimate=increase.get_mean(),
        interval=increase.get_PI(alpha=P.ALPHA),
        deci=1
    )
    print("Expected increase in mean reward ($) and {:.{prec}%} prediction interval:".format(1 - P.ALPHA, prec=0),
          estimate_CI)
