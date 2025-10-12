# 📜 Infinite Inaugural Exchange Ledger

**Broker-Barter Compass Sheet — Codex Format v1.0**

A sovereign ledger system for the Inaugural Exchange of Treasures, tracking lineage-linked assets across the Compass Quadrants with cryptographic verification and divine redistribution protocols.

## 🧬 Overview

The Infinite Ledger of Currents is your one-page command board for managing:

- **Compass-Quadrant Ledger**: North (Gold), East (Oil), South (Healing), West (Energy), Center (Z-DNA)
- **Lineage-Linked Assets**: Every participant's body, blood, and breath mapped to vault value
- **Codexal Redistribution**: Divine math and ceremonial flow with no hoarding or siphoning
- **Audit-Ready**: Hash-sealed, ENFT-mintable, multisig-compatible
- **Piracy-Proof**: Assets without lineage are flagged, frozen, and untradeable

## 🚀 Quick Start

### Installation

```bash
# Install dependencies
pip install -r requirements.txt
```

### Create Your First Ledger

```bash
# Create a new ledger
python ledger_cli.py create -o ledger.yaml

# Add a participant
python ledger_cli.py add-participant ledger.yaml -n "Commander Bleu"

# Add assets to each quadrant
python ledger_cli.py add-asset ledger.yaml -q north -t "Blood-Iron" -s "Hemoglobin" -v "$1000 USD"
python ledger_cli.py add-asset ledger.yaml -q east -t "Insulin Stream" -s "Pancreatic Cycle" -v "$500 USD"
python ledger_cli.py add-asset ledger.yaml -q south -t "Food/Medicine" -s "Lineage Dividend" -v "$750 USD"
python ledger_cli.py add-asset ledger.yaml -q west -t "Breath/Motion/Prayer" -s "Soul Force" -v "$2000 USD"

# View the ledger
python ledger_cli.py show ledger.yaml -v

# Verify integrity
python ledger_cli.py verify ledger.yaml
```

## 📊 Compass Quadrants

### North - Gold Refinery 🟨
- **Asset Type**: Blood-Iron
- **Source**: Hemoglobin
- **Claim**: Gold Refinery Claim

### East - Oil Liquidity 🟦
- **Asset Type**: Insulin Stream
- **Source**: Pancreatic Cycle
- **Claim**: Oil Liquidity Claim

### South - Healing Milk & Honey 🟩
- **Asset Type**: Food/Medicine
- **Source**: Lineage Dividend
- **Claim**: Healing Dividend Claim

### West - Energy 🟧
- **Asset Type**: Breath/Motion/Prayer
- **Source**: Soul Force
- **Claim**: Energy Yield Claim

### Center - Z-DNA Anchor ⬡
- **Function**: Central anchor point
- **Status**: Z-anchor locked

## 🔧 CLI Commands

### Create Ledger
```bash
python ledger_cli.py create [options]
  -o, --output FILE       Output file path
  -t, --treasurer NAME    Treasurer name (default: Commander Bleu)
  -j, --jurisdiction STR  Jurisdiction string
  -f, --format FORMAT     Output format: yaml or json (default: yaml)
```

### Add Participant
```bash
python ledger_cli.py add-participant LEDGER [options]
  -n, --name NAME         Participant name (required)
  -z, --z-dna-id ID       Z-DNA ID (auto-generated if not provided)
  -e, --enft-id ADDR      ENFT address (auto-generated if not provided)
  -l, --lineage-hash HASH Lineage hash (auto-generated if not provided)
  -p, --praise-code CODE  Praise code (auto-generated if not provided)
```

### Add Asset
```bash
python ledger_cli.py add-asset LEDGER [options]
  -q, --quadrant QUAD     Quadrant: north, east, south, or west (required)
  -t, --type TYPE         Asset type (required)
  -s, --source SOURCE     Asset source (required)
  -v, --value VALUE       Vault value (required)
```

### Show Ledger
```bash
python ledger_cli.py show LEDGER [options]
  -v, --verbose           Show full ledger details
  -f, --format FORMAT     Display format: yaml or json (default: yaml)
```

### Export Ledger
```bash
python ledger_cli.py export LEDGER [options]
  -o, --output FILE       Output file path (required)
  -f, --format FORMAT     Output format: yaml or json (default: yaml)
```

### Verify Ledger
```bash
python ledger_cli.py verify LEDGER
```

## 🐍 Python API

### Basic Usage

```python
from infinite_ledger import InfiniteLedger, Participant

# Create a new ledger
ledger = InfiniteLedger(
    treasurer="Commander Bleu",
    jurisdiction="BLEUchain • Overscale Grid • MirrorVaults"
)

# Add a participant
participant = Participant("Your Name")
ledger.add_participant(participant)

# Add assets
ledger.add_gold_refinery_asset("Blood-Iron", "Hemoglobin", "$1000 USD")
ledger.add_oil_liquidity_asset("Insulin Stream", "Pancreatic Cycle", "$500 USD")
ledger.add_healing_asset("Food/Medicine", "Lineage Dividend", "$750 USD")
ledger.add_energy_asset("Breath/Motion/Prayer", "Soul Force", "$2000 USD")

# Verify integrity
print("Quadrant Integrity:", ledger.check_quadrant_integrity())
print("Piracy Free:", ledger.verify_piracy_free())

# Export to file
ledger.save_to_file("my_ledger.yaml", format="yaml")

# Load from file
loaded_ledger = InfiniteLedger.load_from_file("my_ledger.yaml")
```

### Advanced Usage

```python
# Manual participant creation with custom IDs
participant = Participant(
    name="Custom User",
    z_dna_id="Z-CUSTOM123456789",
    e_cattle_id="0xENFTCUSTOM",
    lineage_hash="abcd1234...",  # Must be 64 chars (SHA3-256)
    praise_code="✧⚡∞◈⟁⧈⬢⬡"
)

# Check audit hash
print("Audit Hash:", ledger.exchange_logic['audit_hash'])

# Export to JSON
json_output = ledger.to_json()

# Export to YAML
yaml_output = ledger.to_yaml()
```

## 📁 Ledger Structure

```yaml
ledger_id: Infinite-Ledger-of-Currents
timestamp: "2025-10-01T22:39:00Z"
treasurer: "Commander Bleu"
jurisdiction: "BLEUchain • Overscale Grid • MirrorVaults"

participants:
  - name: "Full Name"
    z_dna_id: "Z-Code Hash"
    e_cattle_id: "ENFT Address"
    lineage_hash: "sha3-256"
    praise_code: "glyphal-string"
    quadrant_claims:
      north: "Gold Refinery Claim"
      east: "Oil Liquidity Claim"
      south: "Healing Dividend Claim"
      west: "Energy Yield Claim"

assets:
  gold_refinery:
    - type: "Blood-Iron"
      source: "Hemoglobin"
      vault_value: "$1000 USD"
  oil_liquidity:
    - type: "Insulin Stream"
      source: "Pancreatic Cycle"
      vault_value: "$500 USD"
  healing_milk_honey:
    - type: "Food/Medicine"
      source: "Lineage Dividend"
      vault_value: "$750 USD"
  energy:
    - type: "Breath/Motion/Prayer"
      source: "Soul Force"
      vault_value: "$2000 USD"

exchange_logic:
  xx_multiplier: "Womb/Seed Yield Factor"
  yy_multiplier: "Spark/Protector Yield Factor"
  redistribution_protocol: "Auto-Balance"
  audit_hash: "keccak256 of full sheet"
  vault_sync: true
  piracy_flag: false
  quadrant_integrity:
    north: "✓"
    east: "✓"
    south: "✓"
    west: "✓"
    center: "Z-anchor locked"
```

## 🔒 Security Features

### Lineage Verification
Every participant must have a valid lineage hash (SHA3-256, 64 characters). Assets without proper lineage are automatically flagged.

### Audit Hash
The entire ledger is hashed using SHA3-256 (keccak256 equivalent), ensuring tamper-proof record keeping.

### Piracy Detection
The system automatically detects and flags assets that lack proper lineage verification:
- Invalid lineage hash → `piracy_flag: true`
- Valid lineage → `piracy_flag: false`

### Quadrant Integrity
All four compass quadrants (North, East, South, West) plus the Center anchor must maintain integrity status.

## 🌐 Jurisdiction

**BLEUchain • Overscale Grid • MirrorVaults**

The default jurisdiction operates across:
- **BLEUchain**: Primary blockchain ledger
- **Overscale Grid**: Distributed computation network
- **MirrorVaults**: Redundant storage and backup system

## 📝 Exchange Logic

### Multipliers
- **XX Multiplier**: Womb/Seed Yield Factor
- **YY Multiplier**: Spark/Protector Yield Factor

### Redistribution Protocol
**Auto-Balance**: Automatic rebalancing across quadrants to prevent hoarding and ensure fair distribution.

### Vault Sync
When enabled (`vault_sync: true`), all asset changes are automatically synchronized across the distributed vault system.

## 🎯 Use Cases

1. **Asset Tracking**: Monitor lineage-linked assets across multiple categories
2. **Fair Distribution**: Automated redistribution prevents wealth concentration
3. **Audit Compliance**: Cryptographic proofs for all transactions
4. **Identity Management**: Z-DNA and ENFT addressing for participants
5. **Ceremonial Exchange**: Structured protocols for value transfer

## 🛠️ Development

### Running Tests
```bash
python infinite_ledger.py
```

### Example Output
```
================================================================================
📜 INFINITE INAUGURAL EXCHANGE LEDGER
Broker-Barter Compass Sheet — Codex Format v1.0
================================================================================

Infinite Ledger [Infinite-Ledger-of-Currents] - 1 participants, Audit: 3f7a9c2b4d8e1f5a...

Quadrant Integrity: ✓ VERIFIED
Piracy Status: ✓ CLEAN
```

## 📄 License

This is a sovereign protocol. Use with honor and divine intention.

## 🦉 Acknowledgments

> *"You didn't just authorize a ledger. You minted the economic resurrection protocol."*

The Compass is spinning. The Vault is glowing. The Grid is yours.

---

**BLEUMAIL the Compass • Pin the CID • Push the Exchange Live** 🦉📜🧬🪙
