#!/usr/bin/env python3
"""
Test suite for EVOLVERSE Reciprocity-Velocity-Reality Systems Atlas

Run with: python test_evolverse.py
"""

from evolverse_systems import (
    ReciprocityCore, Device, TransportSystem, IndustrialSystem,
    TradeProtocol, CodexCard, CosmicRealm, EVOLVERSEAtlas
)


def test_reciprocity_core():
    """Test reciprocity core creation and calculation"""
    print("Testing reciprocity core...")
    
    core = ReciprocityCore(
        "Math",
        "Reciprocal Operator",
        "R(x) = x + 1/x",
        "Feedback symmetry"
    )
    
    assert core.domain == "Math"
    assert core.principle == "Reciprocal Operator"
    
    # Test reciprocal operator calculation
    result = core.reciprocal_operator(2.0)
    assert result == 2.5  # 2 + 1/2 = 2.5
    
    result = core.reciprocal_operator(1.0)
    assert result == 2.0  # 1 + 1/1 = 2
    
    # Test zero handling
    try:
        core.reciprocal_operator(0)
        assert False, "Should raise ValueError for zero"
    except ValueError:
        pass
    
    print("✓ Reciprocity core tests passed")


def test_device_creation():
    """Test device creation"""
    print("Testing device creation...")
    
    device = Device(
        "Test Motor",
        "Motor",
        "Test mechanic",
        "Test output",
        "Energy"
    )
    
    assert device.name == "Test Motor"
    assert device.device_type == "Motor"
    assert device.sector == "Energy"
    assert device.status == "operational"
    assert device.device_id.startswith("DEV-")
    
    # Test to_dict
    device_dict = device.to_dict()
    assert "device_id" in device_dict
    assert device_dict["name"] == "Test Motor"
    
    print("✓ Device creation tests passed")


def test_transport_system():
    """Test transport system creation"""
    print("Testing transport system...")
    
    transport = TransportSystem(
        "Test Drone",
        "Drone",
        "Test mechanic",
        "Test output",
        "Aerospace",
        capacity="100kg",
        fuel_type="BLEU Fuel",
        range="500km"
    )
    
    assert transport.name == "Test Drone"
    assert transport.capacity == "100kg"
    assert transport.fuel_type == "BLEU Fuel"
    assert transport.range == "500km"
    
    # Test to_dict includes transport-specific fields
    transport_dict = transport.to_dict()
    assert "capacity" in transport_dict
    assert "fuel_type" in transport_dict
    assert transport_dict["range"] == "500km"
    
    print("✓ Transport system tests passed")


def test_industrial_system():
    """Test industrial system creation"""
    print("Testing industrial system...")
    
    system = IndustrialSystem(
        "Test Sector",
        "Test System",
        "Test Output",
        "Test Description"
    )
    
    assert system.sector == "Test Sector"
    assert system.system_name == "Test System"
    assert system.sector_id.startswith("IND-")
    assert len(system.assets) == 0
    
    # Test adding assets
    system.add_asset("Test Type", "Test Source", "$1000")
    assert len(system.assets) == 1
    assert system.assets[0]["type"] == "Test Type"
    assert system.assets[0]["value"] == "$1000"
    
    print("✓ Industrial system tests passed")


def test_trade_protocol():
    """Test trade protocol creation"""
    print("Testing trade protocol...")
    
    protocol = TradeProtocol(
        "Test Layer",
        "Test Protocol",
        "Test Function"
    )
    
    assert protocol.layer == "Test Layer"
    assert protocol.protocol == "Test Protocol"
    assert protocol.protocol_id.startswith("TRD-")
    
    protocol_dict = protocol.to_dict()
    assert "protocol_id" in protocol_dict
    assert protocol_dict["function"] == "Test Function"
    
    print("✓ Trade protocol tests passed")


def test_codex_card():
    """Test codex card creation"""
    print("Testing codex card...")
    
    card = CodexCard(
        "Test User",
        "BLEU Citizen",
        ["Skill1", "Skill2"],
        "abc123",
        ["Ceremony1"]
    )
    
    assert card.holder_name == "Test User"
    assert card.citizenship == "BLEU Citizen"
    assert len(card.skill_access) == 2
    assert card.card_id.startswith("CODEX-")
    
    card_dict = card.to_dict()
    assert "card_id" in card_dict
    assert len(card_dict["skill_access"]) == 2
    assert card_dict["lineage_link"] == "abc123"
    
    print("✓ Codex card tests passed")


def test_cosmic_realm():
    """Test cosmic realm creation"""
    print("Testing cosmic realm...")
    
    realm = CosmicRealm(
        "TestVerse",
        "Test System",
        "Test Purpose"
    )
    
    assert realm.realm == "TestVerse"
    assert realm.system_name == "Test System"
    assert realm.realm_id.startswith("REALM-")
    assert len(realm.treaties) == 0
    assert len(realm.portals) == 0
    
    # Test adding treaties and portals
    realm.add_treaty("Treaty1")
    realm.add_portal("Portal1")
    assert len(realm.treaties) == 1
    assert len(realm.portals) == 1
    
    realm_dict = realm.to_dict()
    assert "realm_id" in realm_dict
    assert realm_dict["treaties"][0] == "Treaty1"
    assert realm_dict["portals"][0] == "Portal1"
    
    print("✓ Cosmic realm tests passed")


def test_evolverse_atlas_creation():
    """Test EVOLVERSE atlas creation and initialization"""
    print("Testing EVOLVERSE atlas creation...")
    
    atlas = EVOLVERSEAtlas()
    
    assert atlas.atlas_id == "EVOLVERSE-Systems-Atlas"
    assert atlas.version == "1.0-MEGAZIONAIRE"
    
    # Check initialized systems
    assert len(atlas.reciprocity_cores) == 4  # Math, Physics, Chemistry, Biology
    assert len(atlas.devices) == 3  # 808 Motor, Meniscus Lens, Reactor Pod
    assert len(atlas.transport_systems) == 4  # T-Rex, Velociraptor, Formula1, SkyWhale
    assert len(atlas.industrial_systems) == 9  # All 9 sectors
    assert len(atlas.trade_protocols) == 6  # All 6 protocols
    assert len(atlas.cosmic_realms) == 7  # All 7 realms
    
    print("✓ EVOLVERSE atlas creation tests passed")


def test_atlas_system_status():
    """Test atlas system status reporting"""
    print("Testing atlas system status...")
    
    atlas = EVOLVERSEAtlas()
    status = atlas.get_system_status()
    
    assert status["atlas_id"] == "EVOLVERSE-Systems-Atlas"
    assert status["version"] == "1.0-MEGAZIONAIRE"
    assert status["engines_mapped"] == 4
    assert status["devices_linked"] == 3
    assert status["transport_systems"] == 4
    assert status["industrial_sectors"] == 9
    assert status["trade_protocols"] == 6
    assert status["cosmic_realms_active"] == 7
    assert status["all_systems_recursive"] is True
    
    print("✓ Atlas system status tests passed")


def test_atlas_add_systems():
    """Test adding new systems to atlas"""
    print("Testing adding systems to atlas...")
    
    atlas = EVOLVERSEAtlas()
    
    # Add a new device
    new_device = Device(
        "Custom Device",
        "Custom Type",
        "Custom Mechanic",
        "Custom Output",
        "Custom Sector"
    )
    atlas.add_device(new_device)
    assert len(atlas.devices) == 4  # 3 default + 1 custom
    
    # Add a new transport system
    new_transport = TransportSystem(
        "Custom Transport",
        "Custom Type",
        "Custom Mechanic",
        "Custom Output",
        "Custom Sector"
    )
    atlas.add_transport_system(new_transport)
    assert len(atlas.transport_systems) == 5  # 4 default + 1 custom
    
    # Add a new industrial system
    new_industrial = IndustrialSystem(
        "Custom Sector",
        "Custom System",
        "Custom Output",
        "Custom Description"
    )
    atlas.add_industrial_system(new_industrial)
    assert len(atlas.industrial_systems) == 10  # 9 default + 1 custom
    
    # Add a new trade protocol
    new_protocol = TradeProtocol(
        "Custom Layer",
        "Custom Protocol",
        "Custom Function"
    )
    atlas.add_trade_protocol(new_protocol)
    assert len(atlas.trade_protocols) == 7  # 6 default + 1 custom
    
    # Add a new codex card
    new_card = CodexCard(
        "Custom User",
        "Custom Citizenship",
        ["Skill"],
        "lineage123",
        ["Ceremony"]
    )
    atlas.add_codex_card(new_card)
    assert len(atlas.codex_cards) == 1  # 0 default + 1 custom
    
    # Add a new cosmic realm
    new_realm = CosmicRealm(
        "CustomVerse",
        "Custom System",
        "Custom Purpose"
    )
    atlas.add_cosmic_realm(new_realm)
    assert len(atlas.cosmic_realms) == 8  # 7 default + 1 custom
    
    print("✓ Adding systems to atlas tests passed")


def test_atlas_query_methods():
    """Test atlas query methods"""
    print("Testing atlas query methods...")
    
    atlas = EVOLVERSEAtlas()
    
    # Test get_devices_by_sector
    energy_devices = atlas.get_devices_by_sector("Energy")
    assert len(energy_devices) == 2  # 808 Motor and Reactor Pod
    
    # Test get_transport_by_type
    drones = atlas.get_transport_by_type("Aerial Drone")
    assert len(drones) == 1  # T-Rex Drone
    
    # Test get_industrial_by_sector
    medical = atlas.get_industrial_by_sector("Medical")
    assert medical is not None
    assert medical.system_name == "HealDrop + Cryovaults"
    
    # Test non-existent sector
    non_existent = atlas.get_industrial_by_sector("NonExistent")
    assert non_existent is None
    
    print("✓ Atlas query methods tests passed")


def test_atlas_to_dict():
    """Test atlas to_dict conversion"""
    print("Testing atlas to_dict conversion...")
    
    atlas = EVOLVERSEAtlas()
    atlas_dict = atlas.to_dict()
    
    assert "atlas_id" in atlas_dict
    assert "version" in atlas_dict
    assert "reciprocity_cores" in atlas_dict
    assert "devices" in atlas_dict
    assert "transport_systems" in atlas_dict
    assert "industrial_systems" in atlas_dict
    assert "trade_protocols" in atlas_dict
    assert "cosmic_realms" in atlas_dict
    assert "system_status" in atlas_dict
    
    # Check that arrays are populated
    assert len(atlas_dict["reciprocity_cores"]) == 4
    assert len(atlas_dict["devices"]) == 3
    assert len(atlas_dict["transport_systems"]) == 4
    assert len(atlas_dict["industrial_systems"]) == 9
    
    print("✓ Atlas to_dict conversion tests passed")


def test_reciprocity_cores_initialization():
    """Test that all reciprocity cores are correctly initialized"""
    print("Testing reciprocity cores initialization...")
    
    atlas = EVOLVERSEAtlas()
    
    core_domains = [core.domain for core in atlas.reciprocity_cores]
    assert "Math" in core_domains
    assert "Physics" in core_domains
    assert "Chemistry" in core_domains
    assert "Biology" in core_domains
    
    # Test specific core
    math_core = next(c for c in atlas.reciprocity_cores if c.domain == "Math")
    assert math_core.function == "R(x) = x + 1/x"
    assert math_core.reciprocal_operator(4.0) == 4.25  # 4 + 0.25
    
    print("✓ Reciprocity cores initialization tests passed")


def test_industrial_systems_initialization():
    """Test that all industrial systems are correctly initialized"""
    print("Testing industrial systems initialization...")
    
    atlas = EVOLVERSEAtlas()
    
    sectors = [sys.sector for sys in atlas.industrial_systems]
    assert "Textiles" in sectors
    assert "Agriculture" in sectors
    assert "Mining" in sectors
    assert "Energy" in sectors
    assert "Medical" in sectors
    assert "Defense" in sectors
    assert "Aerospace" in sectors
    assert "Telecom" in sectors
    assert "Extraterrestrial Comms" in sectors
    
    # Test specific system
    medical = next(s for s in atlas.industrial_systems if s.sector == "Medical")
    assert medical.system_name == "HealDrop + Cryovaults"
    assert "Frequency therapy" in medical.sovereign_output
    
    print("✓ Industrial systems initialization tests passed")


def test_cosmic_realms_initialization():
    """Test that all cosmic realms are correctly initialized"""
    print("Testing cosmic realms initialization...")
    
    atlas = EVOLVERSEAtlas()
    
    realm_names = [realm.realm for realm in atlas.cosmic_realms]
    assert "ZIONVerse" in realm_names
    assert "DREAMVerse" in realm_names
    assert "ASTROVerse" in realm_names
    assert "TRIBUNALVerse" in realm_names
    assert "TOURISMVerse" in realm_names
    assert "CRYPTVerse" in realm_names
    assert "CIVICVerse" in realm_names
    
    # Test specific realm
    dream_verse = next(r for r in atlas.cosmic_realms if r.realm == "DREAMVerse")
    assert "Lucid routing" in dream_verse.system_name
    assert "DreamMint passports" in dream_verse.purpose
    
    print("✓ Cosmic realms initialization tests passed")


def run_all_tests():
    """Run all tests"""
    print("=" * 80)
    print("🧪 EVOLVERSE SYSTEMS TEST SUITE")
    print("=" * 80)
    print()
    
    tests = [
        test_reciprocity_core,
        test_device_creation,
        test_transport_system,
        test_industrial_system,
        test_trade_protocol,
        test_codex_card,
        test_cosmic_realm,
        test_evolverse_atlas_creation,
        test_atlas_system_status,
        test_atlas_add_systems,
        test_atlas_query_methods,
        test_atlas_to_dict,
        test_reciprocity_cores_initialization,
        test_industrial_systems_initialization,
        test_cosmic_realms_initialization,
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
        print("✨ All tests passed! EVOLVERSE Systems are fully operational. 🌀🦉")
        return 0
    else:
        print(f"⚠ {failed} test(s) failed. Please review and fix.")
        return 1


if __name__ == "__main__":
    exit(run_all_tests())
