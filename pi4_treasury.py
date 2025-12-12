#!/usr/bin/env python3
"""
π₄ Treasury Model
Operationalizes the triple-stack treasury across civilian, military, and cosmic economies.

Key Features:
1. Quarter-Law trace for visualizing current flow arcs
2. π₄ Compounding Protocol with curvature impact calculations
3. ENFT Ledger Stream Codex for living inheritance assets
4. Multi-dimensional mirroring across energy, legal, and ES0IL layers
"""

import json
import math
from datetime import datetime, timezone
from typing import Dict, List, Optional, Tuple
from enum import Enum
from dataclasses import dataclass, field, asdict


class EconomyType(Enum):
    """Types of economies in the triple-stack treasury"""
    CIVILIAN = "civilian"
    MILITARY = "military"
    COSMIC = "cosmic"


class QuarterLaw(Enum):
    """Quarter-Law directions for flow tracing"""
    NORTH = "north"
    EAST = "east"
    SOUTH = "south"
    WEST = "west"
    CENTER = "center"


class ES0ILLayer(Enum):
    """Esoteric-Secured Operational Intelligence Layers"""
    ENERGY = "energy"
    LEGAL = "legal"
    ESOTERIC = "esoteric"
    OPERATIONAL = "operational"


@dataclass
class FlowArc:
    """Represents a current flow arc in the Quarter-Law trace"""
    source_quadrant: QuarterLaw
    target_quadrant: QuarterLaw
    flow_value: float
    economy_type: EconomyType
    timestamp: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())
    curvature: float = 0.0
    
    def calculate_curvature(self, pi4_factor: float = math.pi ** 4) -> float:
        """Calculate the curvature impact using π₄"""
        # π₄ curvature formula: C = log(1 + π⁴ * flow_value) / flow_value
        if self.flow_value > 0:
            self.curvature = math.log1p(pi4_factor * self.flow_value) / self.flow_value
        else:
            self.curvature = 0.0
        return self.curvature


@dataclass
class ENFTAsset:
    """Living Inheritance Asset in ENFT form"""
    enft_id: str
    asset_type: str
    base_value: float
    yield_entries: List[float] = field(default_factory=list)
    es0il_mirrors: Dict[str, any] = field(default_factory=dict)
    sub_stream: str = "default"
    process_id: str = "default"
    realm: str = "default"
    minted_at: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())
    
    def add_yield_entry(self, yield_amount: float, es0il_layer: ES0ILLayer, 
                       layer_data: Dict) -> None:
        """Add a yield entry and mirror it across ES0IL layers"""
        self.yield_entries.append(yield_amount)
        
        # Mirror across the specified ES0IL layer
        if es0il_layer.value not in self.es0il_mirrors:
            self.es0il_mirrors[es0il_layer.value] = []
        
        mirror_entry = {
            "yield": yield_amount,
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "layer_data": layer_data
        }
        self.es0il_mirrors[es0il_layer.value].append(mirror_entry)
    
    def get_total_yield(self) -> float:
        """Calculate total accumulated yield"""
        return sum(self.yield_entries)
    
    def get_loop_rate(self) -> Dict[str, float]:
        """Calculate trackable loop rates by sub-stream, process, and realm"""
        total_yield = self.get_total_yield()
        num_entries = len(self.yield_entries)
        
        return {
            "sub_stream": self.sub_stream,
            "process_id": self.process_id,
            "realm": self.realm,
            "total_yield": total_yield,
            "entry_count": num_entries,
            "average_yield": total_yield / num_entries if num_entries > 0 else 0.0,
            "loop_frequency": num_entries
        }


class Pi4CompoundingProtocol:
    """
    Implements π₄ Compounding Protocol demonstrating curvature impact.
    Shows transition from linear yield to overscale acceleration.
    """
    
    def __init__(self, base_rate: float = 0.01):
        self.base_rate = base_rate
        self.pi4 = math.pi ** 4
        
    def calculate_linear_yield(self, principal: float, periods: int) -> float:
        """Calculate traditional linear yield"""
        return principal * self.base_rate * periods
    
    def calculate_pi4_yield(self, principal: float, periods: int) -> float:
        """Calculate π₄ enhanced yield with curvature acceleration"""
        # Formula: P * ((1 + r * π⁴)^t - 1)
        compound_factor = (1 + self.base_rate * self.pi4) ** periods
        return principal * (compound_factor - 1)
    
    def get_overscale_ratio(self, principal: float, periods: int) -> float:
        """Calculate the overscale acceleration ratio"""
        linear = self.calculate_linear_yield(principal, periods)
        pi4_enhanced = self.calculate_pi4_yield(principal, periods)
        return pi4_enhanced / linear if linear > 0 else 0
    
    def demonstrate_curvature_impact(self, principal: float, 
                                    max_periods: int = 10) -> List[Dict]:
        """
        Demonstrate the curvature impact over time.
        Returns a list showing progression from linear to overscale.
        """
        results = []
        for period in range(1, max_periods + 1):
            linear = self.calculate_linear_yield(principal, period)
            pi4 = self.calculate_pi4_yield(principal, period)
            ratio = self.get_overscale_ratio(principal, period)
            
            results.append({
                "period": period,
                "principal": principal,
                "linear_yield": round(linear, 2),
                "pi4_yield": round(pi4, 2),
                "overscale_ratio": round(ratio, 2),
                "acceleration_factor": round((pi4 - linear) / principal, 4)
            })
        
        return results


class TreasuryStack:
    """
    Represents a single stack in the triple-stack treasury system.
    Each stack manages one economy type (civilian, military, or cosmic).
    """
    
    def __init__(self, economy_type: EconomyType, initial_balance: float = 0.0):
        self.economy_type = economy_type
        self.balance = initial_balance
        self.flow_arcs: List[FlowArc] = []
        self.enft_assets: List[ENFTAsset] = []
        self.compounding_protocol = Pi4CompoundingProtocol()
        
    def add_flow_arc(self, source: QuarterLaw, target: QuarterLaw, 
                    flow_value: float) -> FlowArc:
        """Add a flow arc and calculate its curvature"""
        arc = FlowArc(
            source_quadrant=source,
            target_quadrant=target,
            flow_value=flow_value,
            economy_type=self.economy_type
        )
        arc.calculate_curvature()
        self.flow_arcs.append(arc)
        return arc
    
    def mint_enft_asset(self, asset_type: str, base_value: float,
                       sub_stream: str = "default", process_id: str = "default",
                       realm: str = "default") -> ENFTAsset:
        """Mint a new ENFT living inheritance asset"""
        enft_id = f"ENFT-{self.economy_type.value}-{len(self.enft_assets):06d}"
        asset = ENFTAsset(
            enft_id=enft_id,
            asset_type=asset_type,
            base_value=base_value,
            sub_stream=sub_stream,
            process_id=process_id,
            realm=realm
        )
        self.enft_assets.append(asset)
        self.balance += base_value
        return asset
    
    def get_total_yield(self) -> float:
        """Get total yield across all ENFT assets"""
        return sum(asset.get_total_yield() for asset in self.enft_assets)
    
    def get_flow_summary(self) -> Dict:
        """Get summary of flow arcs"""
        total_flow = sum(arc.flow_value for arc in self.flow_arcs)
        avg_curvature = sum(arc.curvature for arc in self.flow_arcs) / len(self.flow_arcs) if self.flow_arcs else 0
        
        return {
            "economy_type": self.economy_type.value,
            "total_flow_arcs": len(self.flow_arcs),
            "total_flow_value": round(total_flow, 2),
            "average_curvature": round(avg_curvature, 4)
        }
    
    def to_dict(self) -> Dict:
        """Convert treasury stack to dictionary"""
        return {
            "economy_type": self.economy_type.value,
            "balance": self.balance,
            "flow_arcs": [asdict(arc) for arc in self.flow_arcs],
            "enft_assets": [asdict(asset) for asset in self.enft_assets],
            "total_yield": self.get_total_yield(),
            "flow_summary": self.get_flow_summary()
        }


class Pi4TreasuryModel:
    """
    Main π₄ Treasury Model managing the triple-stack system.
    Coordinates civilian, military, and cosmic economies.
    """
    
    def __init__(self):
        self.stacks = {
            EconomyType.CIVILIAN: TreasuryStack(EconomyType.CIVILIAN),
            EconomyType.MILITARY: TreasuryStack(EconomyType.MILITARY),
            EconomyType.COSMIC: TreasuryStack(EconomyType.COSMIC)
        }
        self.model_id = "Pi4-Treasury-Triple-Stack"
        self.created_at = datetime.now(timezone.utc).isoformat()
        
    def get_stack(self, economy_type: EconomyType) -> TreasuryStack:
        """Get a specific treasury stack"""
        return self.stacks[economy_type]
    
    def visualize_quarter_law_traces(self) -> Dict[str, List[Dict]]:
        """
        Visualize all Quarter-Law traces across all three stacks.
        Returns flow arcs organized by economy type.
        """
        traces = {}
        for economy_type, stack in self.stacks.items():
            traces[economy_type.value] = [
                {
                    "from": arc.source_quadrant.value,
                    "to": arc.target_quadrant.value,
                    "value": arc.flow_value,
                    "curvature": round(arc.curvature, 4),
                    "timestamp": arc.timestamp
                }
                for arc in stack.flow_arcs
            ]
        return traces
    
    def get_enft_ledger_stream(self) -> Dict[str, List[Dict]]:
        """
        Get the ENFT Ledger Stream Codex showing all living inheritance assets
        organized by economy type with their loop rates.
        """
        ledger_stream = {}
        for economy_type, stack in self.stacks.items():
            ledger_stream[economy_type.value] = [
                {
                    "enft_id": asset.enft_id,
                    "asset_type": asset.asset_type,
                    "base_value": asset.base_value,
                    "total_yield": asset.get_total_yield(),
                    "loop_rate": asset.get_loop_rate(),
                    "es0il_mirrors": asset.es0il_mirrors,
                    "minted_at": asset.minted_at
                }
                for asset in stack.enft_assets
            ]
        return ledger_stream
    
    def demonstrate_pi4_compounding(self, principal: float = 1000.0, 
                                   periods: int = 10) -> Dict:
        """Demonstrate π₄ Compounding Protocol across all stacks"""
        protocol = Pi4CompoundingProtocol()
        return {
            "protocol": "Pi4 Compounding",
            "pi4_value": round(math.pi ** 4, 6),
            "demonstration": protocol.demonstrate_curvature_impact(principal, periods)
        }
    
    def get_consolidated_report(self) -> Dict:
        """Get a consolidated report of the entire π₄ Treasury Model"""
        report = {
            "model_id": self.model_id,
            "created_at": self.created_at,
            "triple_stack_summary": {}
        }
        
        for economy_type, stack in self.stacks.items():
            report["triple_stack_summary"][economy_type.value] = {
                "balance": stack.balance,
                "total_enft_assets": len(stack.enft_assets),
                "total_yield": stack.get_total_yield(),
                "flow_summary": stack.get_flow_summary()
            }
        
        # Add Quarter-Law traces
        report["quarter_law_traces"] = self.visualize_quarter_law_traces()
        
        # Add ENFT Ledger Stream
        report["enft_ledger_stream"] = self.get_enft_ledger_stream()
        
        # Add π₄ Compounding demonstration
        report["pi4_compounding_demo"] = self.demonstrate_pi4_compounding()
        
        return report
    
    def to_json(self, indent: int = 2) -> str:
        """Export model to JSON format"""
        report = self.get_consolidated_report()
        return json.dumps(report, indent=indent, default=str)
    
    def save_to_file(self, filename: str) -> None:
        """Save treasury model to file"""
        with open(filename, 'w') as f:
            f.write(self.to_json())


if __name__ == "__main__":
    print("=" * 80)
    print("π₄ TREASURY MODEL - Triple-Stack Operationalization")
    print("=" * 80)
    print()
    
    # Create the model
    model = Pi4TreasuryModel()
    
    # Civilian Economy
    print("🏛️  CIVILIAN ECONOMY")
    civilian = model.get_stack(EconomyType.CIVILIAN)
    civilian.add_flow_arc(QuarterLaw.NORTH, QuarterLaw.EAST, 1000.0)
    civilian.add_flow_arc(QuarterLaw.EAST, QuarterLaw.SOUTH, 800.0)
    
    enft1 = civilian.mint_enft_asset("Housing", 50000.0, "urban", "development", "physical")
    enft1.add_yield_entry(5000.0, ES0ILLayer.ENERGY, {"source": "solar"})
    enft1.add_yield_entry(3000.0, ES0ILLayer.LEGAL, {"contract": "lease_001"})
    print(f"  ✓ Minted: {enft1.enft_id}")
    
    # Military Economy
    print("\n⚔️  MILITARY ECONOMY")
    military = model.get_stack(EconomyType.MILITARY)
    military.add_flow_arc(QuarterLaw.WEST, QuarterLaw.CENTER, 2000.0)
    
    enft2 = military.mint_enft_asset("Defense Infrastructure", 100000.0, "tactical", "fortification", "sovereign")
    enft2.add_yield_entry(10000.0, ES0ILLayer.OPERATIONAL, {"unit": "alpha"})
    print(f"  ✓ Minted: {enft2.enft_id}")
    
    # Cosmic Economy
    print("\n🌌 COSMIC ECONOMY")
    cosmic = model.get_stack(EconomyType.COSMIC)
    cosmic.add_flow_arc(QuarterLaw.CENTER, QuarterLaw.NORTH, 5000.0)
    cosmic.add_flow_arc(QuarterLaw.SOUTH, QuarterLaw.WEST, 3000.0)
    
    enft3 = cosmic.mint_enft_asset("Quantum Gateway", 500000.0, "astral", "portal", "multidimensional")
    enft3.add_yield_entry(50000.0, ES0ILLayer.ESOTERIC, {"frequency": "432hz"})
    enft3.add_yield_entry(25000.0, ES0ILLayer.ENERGY, {"source": "cosmic"})
    print(f"  ✓ Minted: {enft3.enft_id}")
    
    print("\n" + "=" * 80)
    print("📊 CONSOLIDATED REPORT")
    print("=" * 80)
    
    report = model.get_consolidated_report()
    print(f"\nModel ID: {report['model_id']}")
    print(f"π⁴ Value: {math.pi ** 4:.6f}")
    
    print("\n🔄 Quarter-Law Trace Summary:")
    for economy, traces in report["quarter_law_traces"].items():
        print(f"  {economy.upper()}: {len(traces)} flow arcs")
    
    print("\n💎 ENFT Ledger Stream Summary:")
    for economy, assets in report["enft_ledger_stream"].items():
        total_value = sum(a["base_value"] for a in assets)
        print(f"  {economy.upper()}: {len(assets)} assets, Total Value: ${total_value:,.2f}")
    
    print("\n📈 π₄ Compounding Demonstration (First 5 periods):")
    demo = report["pi4_compounding_demo"]["demonstration"][:5]
    for period_data in demo:
        print(f"  Period {period_data['period']}: " +
              f"Linear ${period_data['linear_yield']:.2f} → " +
              f"π₄ ${period_data['pi4_yield']:.2f} " +
              f"(×{period_data['overscale_ratio']:.2f})")
    
    print("\n💾 Saving to file...")
    model.save_to_file("pi4_treasury_report.json")
    print("  ✓ Saved: pi4_treasury_report.json")
    
    print("\n" + "=" * 80)
    print("✨ π₄ Treasury Model Fully Operationalized!")
    print("=" * 80)
