"""Test basic imports to verify package installation."""

import pytest


def test_import_package():
    """Test that we can import the main package."""
    import mass_automation
    assert mass_automation.__version__ == "0.1.0"


def test_import_submodules():
    """Test that we can import key submodules."""
    from mass_automation import formula
    from mass_automation import deisotoping
    from mass_automation import sample_identification
    from mass_automation.experiment import Experiment, Spectrum
    from mass_automation.utils import Element, lorentzian
    
    # Basic sanity check that these imports worked
    assert hasattr(Element, 'n_elements')

def test_with_numpy():
    """Test NumPy integration."""
    import numpy as np
    from mass_automation.utils import lorentzian
    
    # Simple test calling a function that uses NumPy
    x = np.linspace(0, 1, 10)
    result = lorentzian(x, 0.5, 0.1)
    assert isinstance(result, np.ndarray)
    assert result.shape == x.shape 