import scr.FormatFunctions as Format
import scr.SamplePathClasses as PathCls
import scr.FigureSupport as Figs
import scr.StatisticalClasses as Stat
import Parameters as P


def print_outcomes(sim_output, strategy_name):
    """ prints the outcomes of a simulated cohort under steady state
    :param sim_output: output of a simulated cohort
    :param strategy_name: the name of the selected therapy
    """

    # mean and confidence interval text of patient survival time
    survival_mean_CI_text = Format.format_estimate_interval(
        estimate=sim_output.get_ave_survival_time(),
        interval=sim_output.get_CI_survival_time(alpha=P.ALPHA),
        deci=1)

    # print survival time statistics
    print(strategy_name)
    print("  Estimate of mean survival time (years) and {:.{prec}%} confidence interval:".format(1 - P.ALPHA, prec=0),
          survival_mean_CI_text)


def draw_survival_curves_and_histograms(sim_output_no_drug, sim_output_with_drug):
    """ draws the survival curves and the histograms of survival time
    :param sim_output_no_drug: output of a cohort simulated when drug is not available
    :param sim_output_with_drug: output of a cohort simulated when drug is available
    """

    # get survival curves of both treatments
    survival_curves = [
        sim_output_no_drug.get_survival_curve(),
        sim_output_with_drug.get_survival_curve()
    ]

    # graph survival curve
    PathCls.graph_sample_paths(
        sample_paths=survival_curves,
        title='Survival curve',
        x_label='Simulation time step',
        y_label='Number of alive patients',
        legends=['No Drug', 'With Drug']
    )

    # histograms of survival times
    set_of_survival_times = [
        sim_output_no_drug.get_survival_times(),
        sim_output_with_drug.get_survival_times()
    ]

    # graph histograms
    Figs.graph_histograms(
        data_sets=set_of_survival_times,
        title='Histogram of patient survival time',
        x_label='Survival time',
        y_label='Counts',
        bin_width=1,
        legend=['No Drug', 'With Drug'],
        transparency=0.6
    )


def print_comparative_outcomes(sim_output_no_drug, sim_output_with_drug):
    """ prints expected and percentage increase in survival time when drug is available
    :param sim_output_no_drug: output of a cohort simulated when drug is not available
    :param sim_output_with_drug: output of a cohort simulated when drug is available
    """

    # increase in survival time
    increase = Stat.DifferenceStatIndp(
        name='Increase in survival time',
        x=sim_output_with_drug.get_survival_times(),
        y_ref=sim_output_no_drug.get_survival_times()
    )
    # estimate and CI
    estimate_CI = Format.format_estimate_interval(
        estimate=increase.get_mean(),
        interval=increase.get_t_CI(alpha=P.ALPHA),
        deci=1
    )
    print("Average increase in survival time (years) and {:.{prec}%} confidence interval:".format(1 - P.ALPHA, prec=0),
          estimate_CI)

    # % increase in survival time
    relative_diff = Stat.RelativeDifferenceIndp(
        name='Average % increase in survival time',
        x=sim_output_with_drug.get_survival_times(),
        y_ref=sim_output_no_drug.get_survival_times()
    )
    # estimate and CI
    estimate_CI = Format.format_estimate_interval(
        estimate=relative_diff.get_mean(),
        interval=relative_diff.get_bootstrap_CI(alpha=P.ALPHA, num_samples=1000),
        deci=1,
        form=Format.FormatNumber.PERCENTAGE
    )
    print("Average percentage increase in survival time and {:.{prec}%} confidence interval:".format(1 - P.ALPHA, prec=0),
          estimate_CI)
