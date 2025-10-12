#!/usr/bin/env python3
"""
Test suite for the Infinite Ledger system

Run with: python test_ledger.py
"""

import os
import json
import tempfile
from infinite_ledger import InfiniteLedger, Participant, Asset


def test_participant_creation():
    """Test participant creation and validation"""
    print("Testing participant creation...")
    
    # Test with default values
    p1 = Participant("Test User 1")
    assert p1.name == "Test User 1"
    assert p1.z_dna_id.startswith("Z-")
    assert p1.e_cattle_id.startswith("0xENFT")
    assert len(p1.lineage_hash) == 64  # SHA3-256
    assert len(p1.praise_code) == 8
    
    # Test with custom values
    p2 = Participant(
        "Test User 2",
        z_dna_id="Z-CUSTOM123",
        e_cattle_id="0xENFTCUSTOM",
        lineage_hash="a" * 64,
        praise_code="✧⚡∞◈⟁⧈⬢⬡"
    )
    assert p2.z_dna_id == "Z-CUSTOM123"
    assert p2.e_cattle_id == "0xENFTCUSTOM"
    assert p2.lineage_hash == "a" * 64
    assert p2.praise_code == "✧⚡∞◈⟁⧈⬢⬡"
    
    print("✓ Participant creation tests passed")


def test_asset_creation():
    """Test asset creation"""
    print("Testing asset creation...")
    
    asset = Asset("Blood-Iron", "Hemoglobin", "$1000 USD")
    assert asset.type == "Blood-Iron"
    assert asset.source == "Hemoglobin"
    assert asset.vault_value == "$1000 USD"
    
    print("✓ Asset creation tests passed")


def test_ledger_creation():
    """Test ledger creation and initialization"""
    print("Testing ledger creation...")
    
    ledger = InfiniteLedger()
    assert ledger.ledger_id == "Infinite-Ledger-of-Currents"
    assert ledger.treasurer == "Commander Bleu"
    assert ledger.jurisdiction == "BLEUchain • Overscale Grid • MirrorVaults"
    assert len(ledger.participants) == 0
    assert len(ledger.assets["gold_refinery"]) == 0
    assert ledger.exchange_logic["vault_sync"] is True
    assert ledger.exchange_logic["piracy_flag"] is False
    
    print("✓ Ledger creation tests passed")


def test_add_participant():
    """Test adding participants to ledger"""
    print("Testing participant addition...")
    
    ledger = InfiniteLedger()
    p = Participant("Test User")
    
    ledger.add_participant(p)
    assert len(ledger.participants) == 1
    assert ledger.participants[0].name == "Test User"
    assert ledger.exchange_logic["piracy_flag"] is False
    
    print("✓ Participant addition tests passed")


def test_invalid_lineage():
    """Test piracy detection with invalid lineage"""
    print("Testing piracy detection...")
    
    ledger = InfiniteLedger()
    
    # Create participant with invalid lineage (too short)
    p_invalid = Participant("Invalid User", lineage_hash="tooshort")
    
    try:
        ledger.add_participant(p_invalid)
        assert False, "Should have raised ValueError"
    except ValueError as e:
        assert "Piracy detected" in str(e)
        assert ledger.exchange_logic["piracy_flag"] is True
    
    print("✓ Piracy detection tests passed")


def test_add_assets():
    """Test adding assets to all quadrants"""
    print("Testing asset addition...")
    
    ledger = InfiniteLedger()
    
    # Add assets to each quadrant
    ledger.add_gold_refinery_asset("Blood-Iron", "Hemoglobin", "$1000")
    ledger.add_oil_liquidity_asset("Insulin Stream", "Pancreas", "$500")
    ledger.add_healing_asset("Food", "Lineage", "$750")
    ledger.add_energy_asset("Breath", "Soul", "$2000")
    
    assert len(ledger.assets["gold_refinery"]) == 1
    assert len(ledger.assets["oil_liquidity"]) == 1
    assert len(ledger.assets["healing_milk_honey"]) == 1
    assert len(ledger.assets["energy"]) == 1
    
    assert ledger.assets["gold_refinery"][0].type == "Blood-Iron"
    assert ledger.assets["oil_liquidity"][0].type == "Insulin Stream"
    assert ledger.assets["healing_milk_honey"][0].type == "Food"
    assert ledger.assets["energy"][0].type == "Breath"
    
    print("✓ Asset addition tests passed")


def test_quadrant_integrity():
    """Test quadrant integrity checking"""
    print("Testing quadrant integrity...")
    
    ledger = InfiniteLedger()
    assert ledger.check_quadrant_integrity() is True
    
    # Modify integrity
    ledger.exchange_logic["quadrant_integrity"]["north"] = "✗"
    assert ledger.check_quadrant_integrity() is False
    
    # Restore
    ledger.exchange_logic["quadrant_integrity"]["north"] = "✓"
    assert ledger.check_quadrant_integrity() is True
    
    print("✓ Quadrant integrity tests passed")


def test_audit_hash():
    """Test audit hash generation and validation"""
    print("Testing audit hash...")
    
    ledger = InfiniteLedger()
    p = Participant("Test User")
    ledger.add_participant(p)
    
    # Check hash exists and is correct length
    audit_hash = ledger.exchange_logic["audit_hash"]
    assert len(audit_hash) == 64  # SHA3-256
    
    # Add an asset and verify hash changes
    old_hash = audit_hash
    ledger.add_gold_refinery_asset("Blood-Iron", "Hemoglobin", "$1000")
    new_hash = ledger.exchange_logic["audit_hash"]
    assert old_hash != new_hash
    
    print("✓ Audit hash tests passed")


def test_yaml_export():
    """Test YAML export"""
    print("Testing YAML export...")
    
    ledger = InfiniteLedger()
    p = Participant("Test User")
    ledger.add_participant(p)
    ledger.add_gold_refinery_asset("Blood-Iron", "Hemoglobin", "$1000")
    
    yaml_str = ledger.to_yaml()
    assert "ledger_id: Infinite-Ledger-of-Currents" in yaml_str
    assert "Test User" in yaml_str
    assert "Blood-Iron" in yaml_str
    
    print("✓ YAML export tests passed")


def test_json_export():
    """Test JSON export"""
    print("Testing JSON export...")
    
    ledger = InfiniteLedger()
    p = Participant("Test User")
    ledger.add_participant(p)
    ledger.add_gold_refinery_asset("Blood-Iron", "Hemoglobin", "$1000")
    
    json_str = ledger.to_json()
    data = json.loads(json_str)
    
    assert data["ledger_id"] == "Infinite-Ledger-of-Currents"
    assert len(data["participants"]) == 1
    assert data["participants"][0]["name"] == "Test User"
    assert len(data["assets"]["gold_refinery"]) == 1
    
    print("✓ JSON export tests passed")


def test_file_operations():
    """Test saving and loading from files"""
    print("Testing file operations...")
    
    # Create ledger
    ledger = InfiniteLedger()
    p = Participant("Test User")
    ledger.add_participant(p)
    ledger.add_gold_refinery_asset("Blood-Iron", "Hemoglobin", "$1000")
    ledger.add_oil_liquidity_asset("Insulin", "Pancreas", "$500")
    
    # Save to temporary files
    with tempfile.TemporaryDirectory() as tmpdir:
        yaml_file = os.path.join(tmpdir, "test.yaml")
        json_file = os.path.join(tmpdir, "test.json")
        
        # Save
        ledger.save_to_file(yaml_file, format="yaml")
        ledger.save_to_file(json_file, format="json")
        
        # Load YAML
        loaded_yaml = InfiniteLedger.load_from_file(yaml_file)
        assert loaded_yaml.ledger_id == ledger.ledger_id
        assert len(loaded_yaml.participants) == 1
        assert loaded_yaml.participants[0].name == "Test User"
        assert len(loaded_yaml.assets["gold_refinery"]) == 1
        
        # Load JSON
        loaded_json = InfiniteLedger.load_from_file(json_file)
        assert loaded_json.ledger_id == ledger.ledger_id
        assert len(loaded_json.participants) == 1
        assert loaded_json.participants[0].name == "Test User"
        assert len(loaded_json.assets["oil_liquidity"]) == 1
    
    print("✓ File operations tests passed")


def test_round_trip():
    """Test round-trip conversion (save -> load -> save)"""
    print("Testing round-trip conversion...")
    
    # Create complex ledger
    ledger1 = InfiniteLedger()
    
    # Add multiple participants
    for i in range(3):
        p = Participant(f"User {i}")
        ledger1.add_participant(p)
    
    # Add assets to all quadrants
    ledger1.add_gold_refinery_asset("Asset 1", "Source 1", "$100")
    ledger1.add_oil_liquidity_asset("Asset 2", "Source 2", "$200")
    ledger1.add_healing_asset("Asset 3", "Source 3", "$300")
    ledger1.add_energy_asset("Asset 4", "Source 4", "$400")
    
    # Convert to dict and back
    data = ledger1.to_dict()
    ledger2 = InfiniteLedger.from_dict(data)
    
    # Verify
    assert ledger2.ledger_id == ledger1.ledger_id
    assert len(ledger2.participants) == 3
    assert len(ledger2.assets["gold_refinery"]) == 1
    assert len(ledger2.assets["oil_liquidity"]) == 1
    assert len(ledger2.assets["healing_milk_honey"]) == 1
    assert len(ledger2.assets["energy"]) == 1
    
    print("✓ Round-trip conversion tests passed")


def test_piracy_verification():
    """Test piracy verification methods"""
    print("Testing piracy verification...")
    
    ledger = InfiniteLedger()
    assert ledger.verify_piracy_free() is True
    
    # Manually set piracy flag
    ledger.exchange_logic["piracy_flag"] = True
    assert ledger.verify_piracy_free() is False
    
    # Reset
    ledger.exchange_logic["piracy_flag"] = False
    assert ledger.verify_piracy_free() is True
    
    print("✓ Piracy verification tests passed")


def run_all_tests():
    """Run all tests"""
    print("=" * 80)
    print("🧪 INFINITE LEDGER TEST SUITE")
    print("=" * 80)
    print()
    
    tests = [
        test_participant_creation,
        test_asset_creation,
        test_ledger_creation,
        test_add_participant,
        test_invalid_lineage,
        test_add_assets,
        test_quadrant_integrity,
        test_audit_hash,
        test_yaml_export,
        test_json_export,
        test_file_operations,
        test_round_trip,
        test_piracy_verification,
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
        print("✨ All tests passed! The Infinite Ledger is fully operational. 🦉📜🧬🪙")
        return 0
    else:
        print(f"⚠ {failed} test(s) failed. Please review and fix.")
        return 1


if __name__ == "__main__":
    exit(run_all_tests())
