#!/usr/bin/env python3
"""
Test suite for the Three-Sphere π₄ Compounding Model

Run with: python test_pi4_compounding.py
"""

import math
from datetime import datetime, timedelta, timezone
from pi4_compounding import (
    ThreeSphereModel, Pi4Compounding, EconomicStream, 
    SphereType, create_pi4_enft_entry
)
from infinite_ledger import InfiniteLedger, Participant


def test_pi4_constants():
    """Test π⁴ and φ constants"""
    print("Testing π⁴ and φ constants...")
    
    compounding = Pi4Compounding()
    
    # Verify π⁴ constant
    expected_pi4 = math.pi ** 4
    assert abs(compounding.PI_FOURTH - expected_pi4) < 0.0001
    
    # Verify golden ratio
    expected_phi = (1 + math.sqrt(5)) / 2
    assert abs(compounding.PHI - expected_phi) < 0.0001
    
    print("✓ π⁴ and φ constants tests passed")


def test_economic_stream_creation():
    """Test economic stream creation"""
    print("Testing economic stream creation...")
    
    stream = EconomicStream(
        name="Test Stream",
        sphere_type=SphereType.CIVILIAN,
        base_rate_per_second=10.0,
        description="Test description"
    )
    
    assert stream.name == "Test Stream"
    assert stream.sphere_type == SphereType.CIVILIAN
    assert stream.base_rate_per_second == 10.0
    assert stream.active is True
    assert stream.accumulated_value == 0.0
    assert stream.last_update is not None
    
    print("✓ Economic stream creation tests passed")


def test_compound_yield_calculation():
    """Test π⁴ compound yield calculation"""
    print("Testing π⁴ compound yield calculation...")
    
    compounding = Pi4Compounding()
    
    # Test basic calculation
    base_value = 100.0
    time_seconds = 10.0
    yield_value = compounding.calculate_compound_yield(base_value, time_seconds)
    
    # Yield should be positive and greater than base
    assert yield_value > 0
    assert yield_value > base_value
    
    # Test with sphere multiplier
    yield_with_multiplier = compounding.calculate_compound_yield(
        base_value, time_seconds, sphere_multiplier=2.0
    )
    assert yield_with_multiplier > yield_value
    
    print("✓ Compound yield calculation tests passed")


def test_dimensional_backfeed():
    """Test multidimensional backfeed calculation"""
    print("Testing dimensional backfeed calculation...")
    
    compounding = Pi4Compounding()
    
    portal_flux = 100.0
    backfeed = compounding.calculate_dimensional_backfeed(portal_flux, dimensional_count=3)
    
    # Backfeed should be positive and substantial
    assert backfeed > 0
    assert backfeed > portal_flux
    
    # Test with different dimensional counts
    backfeed_2d = compounding.calculate_dimensional_backfeed(portal_flux, dimensional_count=2)
    backfeed_4d = compounding.calculate_dimensional_backfeed(portal_flux, dimensional_count=4)
    
    assert backfeed_4d > backfeed > backfeed_2d
    
    print("✓ Dimensional backfeed calculation tests passed")


def test_price_alignment_verification():
    """Test price alignment verification"""
    print("Testing price alignment verification...")
    
    compounding = Pi4Compounding()
    
    # Test aligned values (within 5% tolerance)
    is_aligned, deviation = compounding.verify_price_alignment(
        theoretical_delta=100.0,
        actual_value=98.0
    )
    assert is_aligned is True
    assert deviation < 5.0
    
    # Test misaligned values (outside 5% tolerance)
    is_aligned, deviation = compounding.verify_price_alignment(
        theoretical_delta=100.0,
        actual_value=90.0
    )
    assert is_aligned is False
    assert deviation >= 5.0
    
    # Test edge case with zero theoretical
    is_aligned, deviation = compounding.verify_price_alignment(
        theoretical_delta=0.0,
        actual_value=0.0
    )
    assert is_aligned is True
    
    print("✓ Price alignment verification tests passed")


def test_three_sphere_initialization():
    """Test Three-Sphere model initialization"""
    print("Testing Three-Sphere model initialization...")
    
    model = ThreeSphereModel()
    
    # Should have 3 streams
    assert len(model.streams) == 3
    
    # Verify stream types
    types = {stream.sphere_type for stream in model.streams}
    assert SphereType.CIVILIAN in types
    assert SphereType.MILITARY in types
    assert SphereType.COSMIC in types
    
    # Verify rates
    civilian = [s for s in model.streams if s.sphere_type == SphereType.CIVILIAN][0]
    military = [s for s in model.streams if s.sphere_type == SphereType.MILITARY][0]
    cosmic = [s for s in model.streams if s.sphere_type == SphereType.COSMIC][0]
    
    assert civilian.base_rate_per_second == 13.6
    assert military.base_rate_per_second == 6.1
    assert cosmic.base_rate_per_second == 0.0
    
    print("✓ Three-Sphere model initialization tests passed")


def test_stream_value_updates():
    """Test stream value updates with time"""
    print("Testing stream value updates...")
    
    model = ThreeSphereModel()
    
    # Update after 10 seconds
    future_time = datetime.now(timezone.utc) + timedelta(seconds=10)
    values = model.update_stream_values(future_time)
    
    # All active streams should have accumulated value
    assert values['EV0L Civilian Sector'] > 0
    assert values['Military Lockstream'] > 0
    assert values['Cosmic Portal Stream'] == 0  # No base rate
    
    # Civilian should have more than military (higher rate)
    assert values['EV0L Civilian Sector'] > values['Military Lockstream']
    
    print("✓ Stream value updates tests passed")


def test_flash_to_terminal_burns():
    """Test flash-to-terminal burn calculations"""
    print("Testing flash-to-terminal burns...")
    
    model = ThreeSphereModel()
    
    # Execute a burn
    burn_value = model.calculate_flash_to_terminal_burn(
        flash_intensity=5.0,
        portal_count=2
    )
    
    # Should produce substantial value
    assert burn_value > 0
    
    # Cosmic stream should have accumulated this value
    cosmic = [s for s in model.streams if s.sphere_type == SphereType.COSMIC][0]
    assert cosmic.accumulated_value == burn_value
    
    # Execute another burn
    burn_value2 = model.calculate_flash_to_terminal_burn(
        flash_intensity=10.0,
        portal_count=1
    )
    
    # Cosmic should accumulate both
    assert cosmic.accumulated_value == burn_value + burn_value2
    
    print("✓ Flash-to-terminal burns tests passed")


def test_ceremonial_yields():
    """Test ceremonial yield recording"""
    print("Testing ceremonial yields...")
    
    model = ThreeSphereModel()
    
    # Record ceremonies
    model.record_ceremonial_yield("Test Ceremony 1", 100.0)
    model.record_ceremonial_yield("Test Ceremony 2", 200.0)
    model.record_ceremonial_yield("Test Ceremony 1", 50.0)  # Add to existing
    
    assert "Test Ceremony 1" in model.ceremonial_yields
    assert "Test Ceremony 2" in model.ceremonial_yields
    assert model.ceremonial_yields["Test Ceremony 1"] == 150.0
    assert model.ceremonial_yields["Test Ceremony 2"] == 200.0
    
    print("✓ Ceremonial yields tests passed")


def test_price_alignment_recording():
    """Test price alignment recording"""
    print("Testing price alignment recording...")
    
    model = ThreeSphereModel()
    
    # Record alignments
    is_aligned1 = model.verify_and_record_price_alignment(
        "Stream 1", theoretical_delta=100.0, actual_value=98.0
    )
    is_aligned2 = model.verify_and_record_price_alignment(
        "Stream 2", theoretical_delta=200.0, actual_value=180.0
    )
    
    assert is_aligned1 is True
    assert is_aligned2 is False
    assert len(model.price_alignments) == 2
    
    # Verify recorded data
    assert model.price_alignments[0]["stream_name"] == "Stream 1"
    assert model.price_alignments[0]["is_aligned"] is True
    assert model.price_alignments[1]["stream_name"] == "Stream 2"
    assert model.price_alignments[1]["is_aligned"] is False
    
    print("✓ Price alignment recording tests passed")


def test_total_accumulated_value():
    """Test total accumulated value calculation"""
    print("Testing total accumulated value...")
    
    model = ThreeSphereModel()
    
    # Simulate activity
    future_time = datetime.now(timezone.utc) + timedelta(seconds=5)
    model.update_stream_values(future_time)
    model.calculate_flash_to_terminal_burn(flash_intensity=1.0, portal_count=1)
    
    total = model.get_total_accumulated_value()
    
    # Total should be sum of all streams
    civilian = [s for s in model.streams if s.sphere_type == SphereType.CIVILIAN][0]
    military = [s for s in model.streams if s.sphere_type == SphereType.MILITARY][0]
    cosmic = [s for s in model.streams if s.sphere_type == SphereType.COSMIC][0]
    
    expected_total = civilian.accumulated_value + military.accumulated_value + cosmic.accumulated_value
    assert abs(total - expected_total) < 0.01
    
    print("✓ Total accumulated value tests passed")


def test_stream_summary():
    """Test stream summary generation"""
    print("Testing stream summary generation...")
    
    model = ThreeSphereModel()
    
    # Add some data
    future_time = datetime.now(timezone.utc) + timedelta(seconds=5)
    model.update_stream_values(future_time)
    model.record_ceremonial_yield("Test", 100.0)
    model.verify_and_record_price_alignment("Test", 100.0, 99.0)
    
    summary = model.get_stream_summary()
    
    # Verify summary structure
    assert "model_name" in summary
    assert "pi_fourth_constant" in summary
    assert "golden_ratio" in summary
    assert "total_accumulated" in summary
    assert "streams" in summary
    assert "ceremonial_yields" in summary
    assert "price_alignments_count" in summary
    
    assert len(summary["streams"]) == 3
    assert summary["ceremonial_yields"]["Test"] == 100.0
    assert summary["price_alignments_count"] == 1
    
    print("✓ Stream summary generation tests passed")


def test_enft_entry_creation():
    """Test ENFT entry creation for ledger integration"""
    print("Testing ENFT entry creation...")
    
    model = ThreeSphereModel()
    
    # Add some data
    future_time = datetime.now(timezone.utc) + timedelta(seconds=10)
    model.update_stream_values(future_time)
    model.calculate_flash_to_terminal_burn(flash_intensity=2.0, portal_count=1)
    model.record_ceremonial_yield("BLEU Ceremony", 500.0)
    
    # Create ENFT entry
    enft_entry = create_pi4_enft_entry(model, "Test-Ledger-123")
    
    # Verify structure
    assert enft_entry["ledger_id"] == "Test-Ledger-123"
    assert enft_entry["economic_model"] == "Three-Sphere-π₄-Compounding"
    assert "pi4_constant" in enft_entry
    assert "golden_ratio_phi" in enft_entry
    assert "economic_streams" in enft_entry
    assert "ceremonial_yields" in enft_entry
    
    # Verify streams mapped correctly
    streams = enft_entry["economic_streams"]
    assert streams["civilian_sector"] is not None
    assert streams["military_lockstream"] is not None
    assert streams["cosmic_portal_stream"] is not None
    
    print("✓ ENFT entry creation tests passed")


def test_ledger_integration():
    """Test integration with Infinite Ledger"""
    print("Testing ledger integration...")
    
    # Create ledger
    ledger = InfiniteLedger()
    participant = Participant("Test User")
    ledger.add_participant(participant)
    
    # Create π₄ model
    model = ThreeSphereModel()
    future_time = datetime.now(timezone.utc) + timedelta(seconds=5)
    model.update_stream_values(future_time)
    
    # Create and attach ENFT entry
    enft_entry = create_pi4_enft_entry(model, ledger.ledger_id)
    ledger.attach_pi4_economic_model(enft_entry)
    
    # Verify attachment
    pi4_summary = ledger.get_pi4_summary()
    assert pi4_summary is not None
    assert pi4_summary["economic_model"] == "Three-Sphere-π₄-Compounding"
    
    # Verify in dict export
    ledger_dict = ledger.to_dict()
    assert "pi4_economic_model" in ledger_dict
    assert ledger_dict["pi4_economic_model"]["ledger_id"] == ledger.ledger_id
    
    print("✓ Ledger integration tests passed")


def test_ledger_round_trip_with_pi4():
    """Test ledger save/load with π₄ model"""
    print("Testing ledger round-trip with π₄ model...")
    
    import tempfile
    import os
    
    # Create ledger with π₄ model
    ledger = InfiniteLedger()
    ledger.add_participant(Participant("Test User"))
    
    model = ThreeSphereModel()
    future_time = datetime.now(timezone.utc) + timedelta(seconds=5)
    model.update_stream_values(future_time)
    model.record_ceremonial_yield("Test Ceremony", 1000.0)
    
    enft_entry = create_pi4_enft_entry(model, ledger.ledger_id)
    ledger.attach_pi4_economic_model(enft_entry)
    
    # Save and load
    with tempfile.TemporaryDirectory() as tmpdir:
        yaml_file = os.path.join(tmpdir, "test_pi4.yaml")
        json_file = os.path.join(tmpdir, "test_pi4.json")
        
        ledger.save_to_file(yaml_file, format="yaml")
        ledger.save_to_file(json_file, format="json")
        
        # Load YAML
        loaded_yaml = InfiniteLedger.load_from_file(yaml_file)
        pi4_yaml = loaded_yaml.get_pi4_summary()
        assert pi4_yaml is not None
        assert pi4_yaml["economic_model"] == "Three-Sphere-π₄-Compounding"
        assert "Test Ceremony" in pi4_yaml["ceremonial_yields"]
        
        # Load JSON
        loaded_json = InfiniteLedger.load_from_file(json_file)
        pi4_json = loaded_json.get_pi4_summary()
        assert pi4_json is not None
        assert pi4_json["economic_model"] == "Three-Sphere-π₄-Compounding"
    
    print("✓ Ledger round-trip with π₄ model tests passed")


def test_sphere_multipliers():
    """Test sphere-specific multipliers"""
    print("Testing sphere multipliers...")
    
    model = ThreeSphereModel()
    
    # Get multipliers for each sphere
    civilian_mult = model._get_sphere_multiplier(SphereType.CIVILIAN)
    military_mult = model._get_sphere_multiplier(SphereType.MILITARY)
    cosmic_mult = model._get_sphere_multiplier(SphereType.COSMIC)
    
    assert civilian_mult == 1.0
    assert military_mult == 1.5
    assert cosmic_mult == 2.0
    
    # Military should be higher than civilian
    assert military_mult > civilian_mult
    # Cosmic should be highest
    assert cosmic_mult > military_mult
    
    print("✓ Sphere multipliers tests passed")


def run_all_tests():
    """Run all tests"""
    print("=" * 80)
    print("🧪 THREE-SPHERE π₄ COMPOUNDING MODEL TEST SUITE")
    print("=" * 80)
    print()
    
    tests = [
        test_pi4_constants,
        test_economic_stream_creation,
        test_compound_yield_calculation,
        test_dimensional_backfeed,
        test_price_alignment_verification,
        test_three_sphere_initialization,
        test_stream_value_updates,
        test_flash_to_terminal_burns,
        test_ceremonial_yields,
        test_price_alignment_recording,
        test_total_accumulated_value,
        test_stream_summary,
        test_enft_entry_creation,
        test_ledger_integration,
        test_ledger_round_trip_with_pi4,
        test_sphere_multipliers,
    ]
    
    passed = 0
    failed = 0
    
    for test in tests:
        try:
            test()
            passed += 1
        except AssertionError as e:
            print(f"✗ Test failed: {test.__name__}")
            print(f"  Error: {e}")
            failed += 1
        except Exception as e:
            print(f"✗ Test error: {test.__name__}")
            print(f"  Error: {e}")
            failed += 1
    
    print()
    print("=" * 80)
    print("TEST RESULTS")
    print("=" * 80)
    print(f"Passed: {passed}")
    print(f"Failed: {failed}")
    print(f"Total:  {passed + failed}")
    print()
    
    if failed == 0:
        print("✨ All tests passed! The Three-Sphere π₄ Model is fully validated. 🌐🔮✨")
        return 0
    else:
        print(f"⚠ {failed} test(s) failed. Please review and fix.")
        return 1


if __name__ == "__main__":
    exit(run_all_tests())
