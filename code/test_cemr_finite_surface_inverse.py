import numpy as np

from cemr_finite_surface_inverse import fit_scenario


def test_clean_calibrated_recovers_conformal_field():
    result = fit_scenario("clean_calibrated", seed=101, sigma_log_area=0.002)
    assert result.classification == "PASS_SCOPED"
    assert result.jacobian_rank == result.n_parameters == 4
    assert result.reduced_chi2 is not None and result.reduced_chi2 < 4.0
    assert result.max_abs_theta_error < 0.02


def test_global_scale_nuisance_is_rank_deficient():
    result = fit_scenario("global_scale_nuisance", seed=101, sigma_log_area=0.002)
    assert result.classification == "BLOCKED_NONIDENTIFIABLE"
    assert result.jacobian_rank < result.n_parameters


def test_unmodelled_channel_anisotropy_is_rejected():
    result = fit_scenario(
        "channel_anisotropy",
        seed=101,
        epsilon=0.05,
        sigma_log_area=0.002,
    )
    assert result.classification == "INCOMPATIBLE_SCALAR_CONFORMAL_SCOPED"
    assert result.reduced_chi2 is not None and result.reduced_chi2 > 9.0


def test_profiled_channel_nuisance_closes_false_geometric_tension():
    epsilon = 0.05
    result = fit_scenario(
        "channel_profiled",
        seed=101,
        epsilon=epsilon,
        sigma_log_area=0.002,
    )
    assert result.classification == "PASS_SCOPED"
    assert result.jacobian_rank == result.n_parameters == 5
    assert result.reduced_chi2 is not None and result.reduced_chi2 < 4.0
    assert result.nuisance_fit is not None
    assert np.isclose(result.nuisance_fit, epsilon, atol=0.005)
    assert result.max_abs_theta_error < 0.02
