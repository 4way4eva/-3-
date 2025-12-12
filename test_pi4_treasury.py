#!/usr/bin/env python3
"""
Test suite for π₄ Treasury Model

Tests all components:
- π₄ Treasury Model
- Triple-stack economies
- Quarter-Law flow tracing
- ENFT Ledger Stream
- π₄ Compounding Protocol
- Integration with Infinite Ledger
"""

import os
import json
import math
from pi4_treasury import (
    Pi4TreasuryModel, TreasuryStack, EconomyType, QuarterLaw,
    ES0ILLayer, FlowArc, ENFTAsset, Pi4CompoundingProtocol
)
from pi4_integration import Pi4InfiniteLedger
from infinite_ledger import Participant, Asset


def test_pi4_treasury_model_creation():
    """Test π₄ Treasury Model initialization"""
    print("Testing π₄ Treasury Model creation...")
    
    model = Pi4TreasuryModel()
    assert model.model_id == "Pi4-Treasury-Triple-Stack"
    assert len(model.stacks) == 3
    assert EconomyType.CIVILIAN in model.stacks
    assert EconomyType.MILITARY in model.stacks
    assert EconomyType.COSMIC in model.stacks
    
    print("✓ π₄ Treasury Model creation tests passed")


def test_treasury_stack():
    """Test individual treasury stack operations"""
    print("Testing treasury stack...")
    
    stack = TreasuryStack(EconomyType.CIVILIAN, initial_balance=1000.0)
    assert stack.economy_type == EconomyType.CIVILIAN
    assert stack.balance == 1000.0
    assert len(stack.flow_arcs) == 0
    assert len(stack.enft_assets) == 0
    
    print("✓ Treasury stack tests passed")


def test_flow_arc_creation():
    """Test Quarter-Law flow arc creation and curvature calculation"""
    print("Testing flow arc creation...")
    
    stack = TreasuryStack(EconomyType.CIVILIAN)
    arc = stack.add_flow_arc(QuarterLaw.NORTH, QuarterLaw.EAST, 1000.0)
    
    assert arc.source_quadrant == QuarterLaw.NORTH
    assert arc.target_quadrant == QuarterLaw.EAST
    assert arc.flow_value == 1000.0
    assert arc.curvature > 0.0  # Should have calculated curvature
    assert len(stack.flow_arcs) == 1
    
    # Verify curvature calculation
    pi4 = math.pi ** 4
    expected_curvature = math.log1p(pi4 * 1000.0) / 1000.0
    assert abs(arc.curvature - expected_curvature) < 0.0001
    
    print("✓ Flow arc tests passed")


def test_enft_asset_creation():
    """Test ENFT living inheritance asset creation"""
    print("Testing ENFT asset creation...")
    
    stack = TreasuryStack(EconomyType.CIVILIAN)
    enft = stack.mint_enft_asset(
        asset_type="Housing",
        base_value=50000.0,
        sub_stream="urban",
        process_id="dev_001",
        realm="physical"
    )
    
    assert enft.enft_id.startswith("ENFT-civilian-")
    assert enft.asset_type == "Housing"
    assert enft.base_value == 50000.0
    assert enft.sub_stream == "urban"
    assert enft.process_id == "dev_001"
    assert enft.realm == "physical"
    assert stack.balance == 50000.0
    assert len(stack.enft_assets) == 1
    
    print("✓ ENFT asset creation tests passed")


def test_enft_yield_entries():
    """Test ENFT yield entry and ES0IL mirroring"""
    print("Testing ENFT yield entries...")
    
    enft = ENFTAsset(
        enft_id="TEST-001",
        asset_type="Test",
        base_value=1000.0
    )
    
    # Add yield entries across different ES0IL layers
    enft.add_yield_entry(100.0, ES0ILLayer.ENERGY, {"source": "solar"})
    enft.add_yield_entry(150.0, ES0ILLayer.LEGAL, {"contract": "test_001"})
    enft.add_yield_entry(200.0, ES0ILLayer.ESOTERIC, {"frequency": "432hz"})
    
    assert len(enft.yield_entries) == 3
    assert enft.get_total_yield() == 450.0
    assert len(enft.es0il_mirrors) == 3
    assert "energy" in enft.es0il_mirrors
    assert "legal" in enft.es0il_mirrors
    assert "esoteric" in enft.es0il_mirrors
    
    print("✓ ENFT yield entry tests passed")


def test_loop_rate_calculation():
    """Test trackable loop rate calculations"""
    print("Testing loop rate calculations...")
    
    enft = ENFTAsset(
        enft_id="TEST-002",
        asset_type="Test",
        base_value=1000.0,
        sub_stream="test_stream",
        process_id="proc_001",
        realm="test_realm"
    )
    
    enft.add_yield_entry(100.0, ES0ILLayer.ENERGY, {})
    enft.add_yield_entry(200.0, ES0ILLayer.ENERGY, {})
    enft.add_yield_entry(150.0, ES0ILLayer.ENERGY, {})
    
    loop_rate = enft.get_loop_rate()
    assert loop_rate["sub_stream"] == "test_stream"
    assert loop_rate["process_id"] == "proc_001"
    assert loop_rate["realm"] == "test_realm"
    assert loop_rate["total_yield"] == 450.0
    assert loop_rate["entry_count"] == 3
    assert loop_rate["average_yield"] == 150.0
    assert loop_rate["loop_frequency"] == 3
    
    print("✓ Loop rate calculation tests passed")


def test_pi4_compounding_protocol():
    """Test π₄ Compounding Protocol calculations"""
    print("Testing π₄ Compounding Protocol...")
    
    protocol = Pi4CompoundingProtocol(base_rate=0.01)
    
    # Test linear yield
    linear = protocol.calculate_linear_yield(1000.0, 5)
    assert linear == 50.0  # 1000 * 0.01 * 5
    
    # Test π₄ yield (should be much higher)
    pi4_yield = protocol.calculate_pi4_yield(1000.0, 5)
    assert pi4_yield > linear
    assert pi4_yield > 10000.0  # π₄ effect should be significant
    
    # Test overscale ratio
    ratio = protocol.get_overscale_ratio(1000.0, 5)
    assert ratio > 1.0  # π₄ should exceed linear
    assert ratio > 100.0  # Should be substantial
    
    # Test demonstration
    demo = protocol.demonstrate_curvature_impact(1000.0, 5)
    assert len(demo) == 5
    assert demo[0]["period"] == 1
    assert demo[4]["period"] == 5
    assert demo[4]["overscale_ratio"] > demo[0]["overscale_ratio"]  # Should accelerate
    
    print("✓ π₄ Compounding Protocol tests passed")


def test_quarter_law_visualization():
    """Test Quarter-Law trace visualization"""
    print("Testing Quarter-Law visualization...")
    
    model = Pi4TreasuryModel()
    
    # Add flows to civilian economy
    civilian = model.get_stack(EconomyType.CIVILIAN)
    civilian.add_flow_arc(QuarterLaw.NORTH, QuarterLaw.EAST, 1000.0)
    civilian.add_flow_arc(QuarterLaw.EAST, QuarterLaw.SOUTH, 800.0)
    
    # Add flows to military economy
    military = model.get_stack(EconomyType.MILITARY)
    military.add_flow_arc(QuarterLaw.WEST, QuarterLaw.CENTER, 2000.0)
    
    # Get visualization
    traces = model.visualize_quarter_law_traces()
    
    assert "civilian" in traces
    assert "military" in traces
    assert "cosmic" in traces
    assert len(traces["civilian"]) == 2
    assert len(traces["military"]) == 1
    assert len(traces["cosmic"]) == 0
    
    # Verify trace structure
    trace = traces["civilian"][0]
    assert "from" in trace
    assert "to" in trace
    assert "value" in trace
    assert "curvature" in trace
    assert "timestamp" in trace
    
    print("✓ Quarter-Law visualization tests passed")


def test_enft_ledger_stream():
    """Test ENFT Ledger Stream Codex"""
    print("Testing ENFT Ledger Stream...")
    
    model = Pi4TreasuryModel()
    
    # Mint assets across different economies
    civilian = model.get_stack(EconomyType.CIVILIAN)
    enft1 = civilian.mint_enft_asset("Housing", 50000.0, "urban", "dev", "physical")
    enft1.add_yield_entry(5000.0, ES0ILLayer.ENERGY, {})
    
    military = model.get_stack(EconomyType.MILITARY)
    enft2 = military.mint_enft_asset("Defense", 100000.0, "tactical", "fort", "sovereign")
    enft2.add_yield_entry(10000.0, ES0ILLayer.OPERATIONAL, {})
    
    # Get ledger stream
    stream = model.get_enft_ledger_stream()
    
    assert "civilian" in stream
    assert "military" in stream
    assert len(stream["civilian"]) == 1
    assert len(stream["military"]) == 1
    
    # Verify stream entry structure
    entry = stream["civilian"][0]
    assert "enft_id" in entry
    assert "asset_type" in entry
    assert "base_value" in entry
    assert "total_yield" in entry
    assert "loop_rate" in entry
    assert "es0il_mirrors" in entry
    assert "minted_at" in entry
    
    print("✓ ENFT Ledger Stream tests passed")


def test_pi4_integration():
    """Test integration with Infinite Ledger"""
    print("Testing π₄ integration with Infinite Ledger...")
    
    ledger = Pi4InfiniteLedger()
    
    # Verify π₄ capabilities are present
    assert hasattr(ledger, 'pi4_treasury')
    assert ledger.exchange_logic["pi4_enabled"] is True
    assert "pi4_value" in ledger.exchange_logic
    assert "triple_stack" in ledger.exchange_logic
    
    # Add participant with economy association
    participant = Participant("Test User")
    ledger.add_pi4_participant(participant, EconomyType.CIVILIAN)
    assert len(ledger.participants) == 1
    
    # Add traditional asset
    ledger.add_gold_refinery_asset("Blood-Iron", "Hemoglobin", "$5000 USD")
    assert len(ledger.assets["gold_refinery"]) == 1
    
    # Convert to ENFT
    asset = ledger.assets["gold_refinery"][0]
    enft = ledger.mint_enft_from_asset(
        "gold_refinery", asset, EconomyType.CIVILIAN
    )
    assert enft.enft_id.startswith("ENFT-civilian-")
    assert enft.base_value == 5000.0
    
    # Create Quarter-Law flow
    arc = ledger.create_quarter_law_flow("north", "east", 2500.0, EconomyType.CIVILIAN)
    assert arc.source_quadrant == QuarterLaw.NORTH
    assert arc.target_quadrant == QuarterLaw.EAST
    
    print("✓ π₄ integration tests passed")


def test_consolidated_report():
    """Test consolidated report generation"""
    print("Testing consolidated report...")
    
    model = Pi4TreasuryModel()
    
    # Add some data
    civilian = model.get_stack(EconomyType.CIVILIAN)
    civilian.add_flow_arc(QuarterLaw.NORTH, QuarterLaw.EAST, 1000.0)
    enft = civilian.mint_enft_asset("Test", 10000.0)
    enft.add_yield_entry(1000.0, ES0ILLayer.ENERGY, {})
    
    # Generate report
    report = model.get_consolidated_report()
    
    assert "model_id" in report
    assert "created_at" in report
    assert "triple_stack_summary" in report
    assert "quarter_law_traces" in report
    assert "enft_ledger_stream" in report
    assert "pi4_compounding_demo" in report
    
    # Verify structure
    assert "civilian" in report["triple_stack_summary"]
    assert "military" in report["triple_stack_summary"]
    assert "cosmic" in report["triple_stack_summary"]
    
    print("✓ Consolidated report tests passed")


def test_json_export():
    """Test JSON export functionality"""
    print("Testing JSON export...")
    
    model = Pi4TreasuryModel()
    
    # Add minimal data
    civilian = model.get_stack(EconomyType.CIVILIAN)
    civilian.add_flow_arc(QuarterLaw.NORTH, QuarterLaw.EAST, 1000.0)
    
    # Export to JSON
    json_str = model.to_json()
    
    # Verify it's valid JSON
    data = json.loads(json_str)
    assert "model_id" in data
    assert "triple_stack_summary" in data
    
    print("✓ JSON export tests passed")


def test_file_operations():
    """Test saving to file"""
    print("Testing file operations...")
    
    model = Pi4TreasuryModel()
    civilian = model.get_stack(EconomyType.CIVILIAN)
    civilian.add_flow_arc(QuarterLaw.NORTH, QuarterLaw.EAST, 1000.0)
    
    # Save to file
    filename = "test_pi4_treasury.json"
    model.save_to_file(filename)
    
    # Verify file exists and contains valid JSON
    assert os.path.exists(filename)
    with open(filename, 'r') as f:
        data = json.load(f)
        assert "model_id" in data
    
    # Clean up
    os.remove(filename)
    
    print("✓ File operations tests passed")


def run_all_tests():
    """Run all π₄ Treasury tests"""
    print("=" * 80)
    print("🧪 π₄ TREASURY MODEL TEST SUITE")
    print("=" * 80)
    print()
    
    tests = [
        test_pi4_treasury_model_creation,
        test_treasury_stack,
        test_flow_arc_creation,
        test_enft_asset_creation,
        test_enft_yield_entries,
        test_loop_rate_calculation,
        test_pi4_compounding_protocol,
        test_quarter_law_visualization,
        test_enft_ledger_stream,
        test_pi4_integration,
        test_consolidated_report,
        test_json_export,
        test_file_operations
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
        print("✨ All π₄ Treasury tests passed! Triple-stack is fully operational. 🦉📜🧬🪙")
        return 0
    else:
        print(f"⚠ {failed} test(s) failed.")
        return 1


if __name__ == "__main__":
    exit(run_all_tests())
