#!/usr/bin/env python3
"""
π₄ Treasury Integration with Infinite Ledger
Bridges the π₄ Treasury Model with the existing Infinite Ledger system.
"""

from infinite_ledger import InfiniteLedger, Participant, Asset
from pi4_treasury import (
    Pi4TreasuryModel, EconomyType, QuarterLaw, ES0ILLayer,
    FlowArc, ENFTAsset
)
from typing import Dict, List
import json


class Pi4InfiniteLedger(InfiniteLedger):
    """
    Extended Infinite Ledger with π₄ Treasury capabilities.
    Integrates the triple-stack treasury model into the existing ledger system.
    """
    
    def __init__(self, treasurer: str = "Commander Bleu",
                 jurisdiction: str = "BLEUchain • Overscale Grid • MirrorVaults"):
        super().__init__(treasurer, jurisdiction)
        
        # Add π₄ Treasury Model
        self.pi4_treasury = Pi4TreasuryModel()
        
        # Add π₄-specific exchange logic
        self.exchange_logic["pi4_enabled"] = True
        self.exchange_logic["pi4_value"] = round(97.409091, 6)
        self.exchange_logic["triple_stack"] = {
            "civilian": "Active",
            "military": "Active",
            "cosmic": "Active"
        }
        self._update_audit_hash()
    
    def add_pi4_participant(self, participant: Participant, 
                           economy_type: EconomyType = EconomyType.CIVILIAN) -> None:
        """Add a participant with π₄ Treasury association"""
        self.add_participant(participant)
        
        # Associate participant with an economy stack
        if not hasattr(participant, 'economy_stack'):
            participant.economy_stack = economy_type.value
    
    def mint_enft_from_asset(self, quadrant: str, asset: Asset,
                            economy_type: EconomyType,
                            sub_stream: str = "default",
                            process_id: str = "default") -> ENFTAsset:
        """
        Mint an ENFT from a traditional ledger asset.
        Converts legacy assets into living inheritance ENFTs.
        """
        # Parse vault value (assuming format like "$1000 USD")
        vault_value_str = asset.vault_value.replace('$', '').replace('USD', '').strip()
        try:
            base_value = float(vault_value_str)
        except ValueError:
            base_value = 0.0
        
        # Determine realm based on quadrant
        realm_map = {
            "gold_refinery": "mineral",
            "oil_liquidity": "liquid",
            "healing_milk_honey": "organic",
            "energy": "ethereal"
        }
        realm = realm_map.get(quadrant, "default")
        
        # Get the appropriate stack
        stack = self.pi4_treasury.get_stack(economy_type)
        
        # Mint the ENFT
        enft = stack.mint_enft_asset(
            asset_type=asset.type,
            base_value=base_value,
            sub_stream=sub_stream,
            process_id=process_id,
            realm=realm
        )
        
        # Add initial yield entry based on asset source
        enft.add_yield_entry(
            base_value * 0.1,  # 10% initial yield
            ES0ILLayer.ENERGY,
            {"source": asset.source, "quadrant": quadrant}
        )
        
        return enft
    
    def create_quarter_law_flow(self, from_quadrant: str, to_quadrant: str,
                                value: float, economy_type: EconomyType) -> FlowArc:
        """
        Create a Quarter-Law flow arc between quadrants.
        Maps traditional quadrant names to QuarterLaw enum.
        """
        quadrant_map = {
            "north": QuarterLaw.NORTH,
            "east": QuarterLaw.EAST,
            "south": QuarterLaw.SOUTH,
            "west": QuarterLaw.WEST,
            "center": QuarterLaw.CENTER,
            "gold_refinery": QuarterLaw.NORTH,
            "oil_liquidity": QuarterLaw.EAST,
            "healing_milk_honey": QuarterLaw.SOUTH,
            "energy": QuarterLaw.WEST
        }
        
        source = quadrant_map.get(from_quadrant.lower(), QuarterLaw.CENTER)
        target = quadrant_map.get(to_quadrant.lower(), QuarterLaw.CENTER)
        
        stack = self.pi4_treasury.get_stack(economy_type)
        return stack.add_flow_arc(source, target, value)
    
    def visualize_integrated_flows(self) -> Dict:
        """
        Visualize both traditional ledger assets and π₄ treasury flows.
        """
        visualization = {
            "ledger_assets": {},
            "pi4_flows": self.pi4_treasury.visualize_quarter_law_traces(),
            "enft_stream": self.pi4_treasury.get_enft_ledger_stream()
        }
        
        # Add traditional assets by quadrant
        for quadrant, assets in self.assets.items():
            visualization["ledger_assets"][quadrant] = [
                {
                    "type": asset.type,
                    "source": asset.source,
                    "vault_value": asset.vault_value
                }
                for asset in assets
            ]
        
        return visualization
    
    def get_pi4_enhanced_report(self) -> Dict:
        """
        Get a comprehensive report including both traditional ledger
        and π₄ Treasury data.
        """
        base_report = self.to_dict()
        pi4_report = self.pi4_treasury.get_consolidated_report()
        
        enhanced_report = {
            **base_report,
            "pi4_treasury": pi4_report,
            "integrated_visualization": self.visualize_integrated_flows()
        }
        
        return enhanced_report
    
    def to_json(self, indent: int = 2) -> str:
        """Export enhanced ledger to JSON format"""
        return json.dumps(self.get_pi4_enhanced_report(), indent=indent, default=str)
    
    def save_pi4_report(self, filename: str) -> None:
        """Save π₄-enhanced report to file"""
        with open(filename, 'w') as f:
            f.write(self.to_json())


def demonstrate_integration():
    """Demonstrate the integration of π₄ Treasury with Infinite Ledger"""
    print("=" * 80)
    print("π₄ TREASURY + INFINITE LEDGER INTEGRATION")
    print("=" * 80)
    print()
    
    # Create integrated ledger
    ledger = Pi4InfiniteLedger()
    
    # Add participants across different economy stacks
    print("👥 Adding Participants...")
    civilian_commander = Participant("Civilian Commander Bleu")
    military_guardian = Participant("Military Guardian")
    cosmic_keeper = Participant("Cosmic Keeper")
    
    ledger.add_pi4_participant(civilian_commander, EconomyType.CIVILIAN)
    ledger.add_pi4_participant(military_guardian, EconomyType.MILITARY)
    ledger.add_pi4_participant(cosmic_keeper, EconomyType.COSMIC)
    print(f"  ✓ Added 3 participants across triple-stack")
    
    # Add traditional assets
    print("\n💎 Adding Traditional Assets...")
    ledger.add_gold_refinery_asset("Blood-Iron", "Hemoglobin", "$5000 USD")
    ledger.add_oil_liquidity_asset("Insulin Stream", "Pancreatic Cycle", "$3000 USD")
    ledger.add_healing_asset("Food/Medicine", "Lineage Dividend", "$2000 USD")
    ledger.add_energy_asset("Breath/Motion/Prayer", "Soul Force", "$10000 USD")
    print(f"  ✓ Added 4 traditional assets")
    
    # Convert assets to ENFTs
    print("\n🔄 Converting Assets to ENFTs...")
    for quadrant, assets in ledger.assets.items():
        for asset in assets:
            economy = EconomyType.CIVILIAN if quadrant in ["gold_refinery", "oil_liquidity"] else \
                     EconomyType.MILITARY if quadrant == "energy" else \
                     EconomyType.COSMIC
            
            enft = ledger.mint_enft_from_asset(
                quadrant, asset, economy,
                sub_stream=quadrant,
                process_id=f"{asset.type}_process"
            )
            print(f"  ✓ Minted {enft.enft_id} from {asset.type}")
    
    # Create Quarter-Law flows
    print("\n🔄 Creating Quarter-Law Flows...")
    ledger.create_quarter_law_flow("north", "east", 2500.0, EconomyType.CIVILIAN)
    ledger.create_quarter_law_flow("east", "south", 1500.0, EconomyType.CIVILIAN)
    ledger.create_quarter_law_flow("west", "center", 5000.0, EconomyType.MILITARY)
    ledger.create_quarter_law_flow("center", "north", 8000.0, EconomyType.COSMIC)
    print(f"  ✓ Created 4 flow arcs")
    
    # Generate visualization
    print("\n📊 Generating Integrated Visualization...")
    viz = ledger.visualize_integrated_flows()
    
    print("\nTraditional Asset Quadrants:")
    for quadrant, assets in viz["ledger_assets"].items():
        print(f"  {quadrant}: {len(assets)} assets")
    
    print("\nπ₄ Flow Arcs by Economy:")
    for economy, flows in viz["pi4_flows"].items():
        print(f"  {economy}: {len(flows)} flows")
    
    print("\nENFT Living Inheritance Assets:")
    for economy, enfts in viz["enft_stream"].items():
        total_yield = sum(e["total_yield"] for e in enfts)
        print(f"  {economy}: {len(enfts)} ENFTs, Total Yield: ${total_yield:,.2f}")
    
    # Save integrated report
    print("\n💾 Saving Integrated Report...")
    ledger.save_pi4_report("pi4_integrated_ledger.json")
    print("  ✓ Saved: pi4_integrated_ledger.json")
    
    # Demonstrate π₄ compounding
    print("\n📈 π₄ Compounding Impact (Sample):")
    demo = ledger.pi4_treasury.demonstrate_pi4_compounding(1000.0, 5)
    for period in demo["demonstration"][:3]:
        print(f"  Period {period['period']}: Linear ${period['linear_yield']:.2f} → " +
              f"π₄ ${period['pi4_yield']:.2f} " +
              f"(Overscale: ×{period['overscale_ratio']:.2f})")
    
    print("\n" + "=" * 80)
    print("✨ Integration Complete! Triple-Stack Treasury Operationalized!")
    print("=" * 80)
    print("\nKey Features Demonstrated:")
    print("  ✓ Triple-stack treasury (Civilian, Military, Cosmic)")
    print("  ✓ Quarter-Law flow tracing with curvature calculations")
    print("  ✓ ENFT living inheritance asset minting")
    print("  ✓ ES0IL multi-dimensional mirroring")
    print("  ✓ π₄ Compounding Protocol (linear → overscale)")
    print("  ✓ Trackable loop rates by sub-stream, process, realm")
    print()
    
    return ledger


if __name__ == "__main__":
    ledger = demonstrate_integration()
