import scr.FormatFunctions as Format
import scr.FigureSupport as Figs
import scr.StatisticalClasses as Stat
import Parameters as P

ALPHA = 0.05

def print_outcomes(multi_cohort, strategy_name):
    """ prints the outcomes of a simulated cohort under steady state
    :param multi_cohort: output of a simulated cohort
    :param strategy_name: the name of the selected therapy
    """

    # mean and confidence interval text of patient survival time
    survival_mean_PI_text = Format.format_estimate_interval(
        estimate=multi_cohort.get_overall_mean_survival(),
        interval=multi_cohort.get_PI_mean_survival(alpha=P.ALPHA),
        deci=1)

    # print survival time statistics
    print(strategy_name)
    print("  Estimate of mean survival time (years) and {:.{prec}%} prediction interval:".format(1 - P.ALPHA, prec=0),
          survival_mean_PI_text)


def draw_histograms(multi_cohort_no_drug, multi_cohort_with_drug):
    """ draws the histograms of average survival time
    :param multi_cohort_no_drug: multiple cohorts simulated when drug is not available
    :param multi_cohort_with_drug: multiple cohorts simulated when drug is available
    """

    # histograms of average survival times
    set_of_survival_times = [
        multi_cohort_no_drug.get_all_mean_survival(),
        multi_cohort_with_drug.get_all_mean_survival()
    ]

    # graph histograms
    Figs.graph_histograms(
        data_sets=set_of_survival_times,
        title='Histogram of average patient survival time',
        x_label='Survival time',
        y_label='Counts',
        bin_width=1,
        legend=['No Drug', 'With Drug'],
        transparency=0.5,
        x_range=[6, 20]
    )


def print_comparative_outcomes(multiCohortNoTrickCoin, multiCohortTrickCoin):
    """ prints expected and percentage increase in average survival time when drug is available
    :param multi_cohort_no_drug: multiple cohorts simulated when drug is not available
    :param multi_cohort_with_drug: multiple cohorts simulated when drug is available
    """

    # increase in survival time
    increase = Stat.DifferenceStatIndp(
        name='Increase in mean survival time',
        x=multiCohortTrickCoin.get_all_mean_survival(),
        y_ref=multiCohortNoTrickCoin.get_all_mean_survival()
    )
    # estimate and prediction interval
    estimate_CI = Format.format_estimate_interval(
        estimate=increase.get_mean(),
        interval=increase.get_PI(alpha=P.ALPHA),
        deci=1
    )
    print("Expected increase in mean survival time (years) and {:.{prec}%} prediction interval:".format(1 - P.ALPHA, prec=0),
          estimate_CI)

    # % increase in mean survival time
    relative_diff = Stat.RelativeDifferenceIndp(
        name='% increase in mean survival time',
        x=multiCohortTrickCoin.get_all_mean_survival(),
        y_ref=multiCohortNoTrickCoin.get_all_mean_survival()
    )
    # estimate and prediction interval
    estimate_CI = Format.format_estimate_interval(
        estimate=relative_diff.get_mean(),
        interval=relative_diff.get_PI(alpha=P.ALPHA),
        deci=1,
        form=Format.FormatNumber.PERCENTAGE
    )
    print("Expected percentage increase in mean survival time and {:.{prec}%} confidence interval:".format(1 - ALPHA, prec=0),
          estimate_CI)
