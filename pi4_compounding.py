#!/usr/bin/env python3
"""
Three-Sphere π₄ Compounding Model
Economic Yield Stream Module

Implements three economic spheres with π⁴ compounding:
1. Civilian Sector - EV0L real estate and education ($13.6M/second)
2. Military Lockstream - Orbital shares and restricted resources ($6.1M/second)
3. Cosmic/Portal Stream - Flash-to-terminal burns with multidimensional backfeed

All streams integrate with ENFT ledger and ceremonial yield tracking.
"""

import math
from datetime import datetime, timezone
from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass
from enum import Enum


class SphereType(Enum):
    """Economic sphere types"""
    CIVILIAN = "civilian"
    MILITARY = "military"
    COSMIC = "cosmic"


@dataclass
class EconomicStream:
    """Represents an economic stream in a sphere"""
    name: str
    sphere_type: SphereType
    base_rate_per_second: float  # Base rate in millions per second
    description: str
    active: bool = True
    accumulated_value: float = 0.0
    last_update: Optional[datetime] = None
    
    def __post_init__(self):
        if self.last_update is None:
            self.last_update = datetime.now(timezone.utc)


class Pi4Compounding:
    """
    π⁴ Compounding Calculator
    
    Uses π⁴ (pi to the fourth power) as the universal compounding constant
    for multidimensional yield calculations across all three spheres.
    """
    
    # π⁴ constant ≈ 97.409091034
    PI_FOURTH = math.pi ** 4
    
    # Golden ratio φ for resonance calculations
    PHI = (1 + math.sqrt(5)) / 2
    
    @classmethod
    def calculate_compound_yield(cls, base_value: float, time_seconds: float, 
                                 sphere_multiplier: float = 1.0) -> float:
        """
        Calculate compounded yield using π⁴ formula
        
        Formula: Y = B * (1 + π⁴/10000)^t * φ * M
        Where:
            Y = Yield
            B = Base value
            t = Time in seconds
            φ = Golden ratio (resonance factor)
            M = Sphere multiplier
        """
        growth_rate = cls.PI_FOURTH / 10000  # Scale to reasonable percentage
        compound_factor = (1 + growth_rate) ** time_seconds
        yield_value = base_value * compound_factor * cls.PHI * sphere_multiplier
        return yield_value
    
    @classmethod
    def calculate_dimensional_backfeed(cls, portal_flux: float, 
                                       dimensional_count: int = 3) -> float:
        """
        Calculate multidimensional backfeed guarantee
        
        Formula: B = F * π⁴ * D^φ
        Where:
            B = Backfeed value
            F = Portal flux
            D = Dimensional count
            φ = Golden ratio exponent
        """
        return portal_flux * cls.PI_FOURTH * (dimensional_count ** cls.PHI)
    
    @classmethod
    def verify_price_alignment(cls, theoretical_delta: float, 
                               actual_value: float, 
                               tolerance: float = 0.05) -> Tuple[bool, float]:
        """
        Verify price alignment between theoretical and actual values
        
        Returns: (is_aligned, deviation_percentage)
        """
        if theoretical_delta == 0:
            return (actual_value == 0, 0.0)
        
        deviation = abs(actual_value - theoretical_delta) / theoretical_delta
        is_aligned = deviation <= tolerance
        return (is_aligned, deviation * 100)


class ThreeSphereModel:
    """
    Three-Sphere π₄ Compounding Economic Model
    
    Manages three economic spheres with ceremonial yield streams:
    - Civilian Sector
    - Military Lockstream
    - Cosmic Portal Stream
    """
    
    def __init__(self):
        self.streams: List[EconomicStream] = []
        self.compounding = Pi4Compounding()
        self.ceremonial_yields: Dict[str, float] = {}
        self.price_alignments: List[Dict] = []
        self.start_time = datetime.now(timezone.utc)
        
        # Initialize the three primary streams
        self._initialize_streams()
    
    def _initialize_streams(self):
        """Initialize the three economic sphere streams"""
        
        # 1. Civilian Sector Stream
        civilian_stream = EconomicStream(
            name="EV0L Civilian Sector",
            sphere_type=SphereType.CIVILIAN,
            base_rate_per_second=13.6,
            description="EV0L real estate and education infrastructure"
        )
        
        # 2. Military Lockstream
        military_stream = EconomicStream(
            name="Military Lockstream",
            sphere_type=SphereType.MILITARY,
            base_rate_per_second=6.1,
            description="Orbital shares targeting rights and restricted resources"
        )
        
        # 3. Cosmic Portal Stream
        cosmic_stream = EconomicStream(
            name="Cosmic Portal Stream",
            sphere_type=SphereType.COSMIC,
            base_rate_per_second=0.0,  # Calculated dynamically via flash-to-terminal
            description="Flash-to-terminal burns with multidimensional backfeed"
        )
        
        self.streams = [civilian_stream, military_stream, cosmic_stream]
    
    def update_stream_values(self, current_time: Optional[datetime] = None) -> Dict[str, float]:
        """
        Update all stream values based on elapsed time with π⁴ compounding
        
        Returns: Dictionary of stream names to accumulated values
        """
        if current_time is None:
            current_time = datetime.now(timezone.utc)
        
        updated_values = {}
        
        for stream in self.streams:
            if not stream.active:
                updated_values[stream.name] = stream.accumulated_value
                continue
            
            # Calculate elapsed time since last update
            elapsed_seconds = (current_time - stream.last_update).total_seconds()
            
            # Calculate base value accumulated during this period
            base_accumulation = stream.base_rate_per_second * elapsed_seconds
            
            # Apply π⁴ compounding
            sphere_multiplier = self._get_sphere_multiplier(stream.sphere_type)
            compounded_yield = self.compounding.calculate_compound_yield(
                base_accumulation, 
                elapsed_seconds, 
                sphere_multiplier
            )
            
            # Update stream
            stream.accumulated_value += compounded_yield
            stream.last_update = current_time
            
            updated_values[stream.name] = stream.accumulated_value
        
        return updated_values
    
    def _get_sphere_multiplier(self, sphere_type: SphereType) -> float:
        """Get the multiplier for each sphere type"""
        multipliers = {
            SphereType.CIVILIAN: 1.0,
            SphereType.MILITARY: 1.5,  # Enhanced security premium
            SphereType.COSMIC: 2.0     # Dimensional expansion factor
        }
        return multipliers.get(sphere_type, 1.0)
    
    def calculate_flash_to_terminal_burn(self, flash_intensity: float, 
                                         portal_count: int = 1) -> float:
        """
        Calculate cosmic stream value from flash-to-terminal burns
        
        Flash-to-terminal: Instantaneous energy transfer across dimensional portals
        """
        cosmic_stream = self._get_stream_by_type(SphereType.COSMIC)
        if not cosmic_stream:
            return 0.0
        
        # Base burn calculation
        burn_value = flash_intensity * portal_count * self.compounding.PI_FOURTH
        
        # Apply multidimensional backfeed
        dimensional_count = 3  # Three-sphere model
        backfeed = self.compounding.calculate_dimensional_backfeed(
            burn_value, 
            dimensional_count
        )
        
        # Update cosmic stream
        total_value = burn_value + backfeed
        cosmic_stream.accumulated_value += total_value
        cosmic_stream.last_update = datetime.now(timezone.utc)
        
        return total_value
    
    def _get_stream_by_type(self, sphere_type: SphereType) -> Optional[EconomicStream]:
        """Get stream by sphere type"""
        for stream in self.streams:
            if stream.sphere_type == sphere_type:
                return stream
        return None
    
    def record_ceremonial_yield(self, ceremony_name: str, yield_value: float):
        """Record a ceremonial yield event"""
        if ceremony_name not in self.ceremonial_yields:
            self.ceremonial_yields[ceremony_name] = 0.0
        self.ceremonial_yields[ceremony_name] += yield_value
    
    def verify_and_record_price_alignment(self, stream_name: str, 
                                         theoretical_delta: float, 
                                         actual_value: float) -> bool:
        """
        Verify price alignment and record the result
        
        Returns: True if aligned within tolerance
        """
        is_aligned, deviation = self.compounding.verify_price_alignment(
            theoretical_delta, 
            actual_value
        )
        
        alignment_record = {
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "stream_name": stream_name,
            "theoretical_delta": theoretical_delta,
            "actual_value": actual_value,
            "deviation_percent": deviation,
            "is_aligned": is_aligned
        }
        self.price_alignments.append(alignment_record)
        
        return is_aligned
    
    def get_total_accumulated_value(self) -> float:
        """Get total accumulated value across all streams"""
        self.update_stream_values()
        return sum(stream.accumulated_value for stream in self.streams)
    
    def get_stream_summary(self) -> Dict:
        """Get summary of all streams"""
        self.update_stream_values()
        
        summary = {
            "model_name": "Three-Sphere π₄ Compounding Model",
            "pi_fourth_constant": self.compounding.PI_FOURTH,
            "golden_ratio": self.compounding.PHI,
            "total_accumulated": self.get_total_accumulated_value(),
            "streams": [],
            "ceremonial_yields": self.ceremonial_yields,
            "price_alignments_count": len(self.price_alignments),
            "recent_alignments": self.price_alignments[-5:] if self.price_alignments else []
        }
        
        for stream in self.streams:
            stream_data = {
                "name": stream.name,
                "type": stream.sphere_type.value,
                "base_rate_per_second": f"${stream.base_rate_per_second}M/s",
                "accumulated_value": f"${stream.accumulated_value:.2f}M",
                "description": stream.description,
                "active": stream.active,
                "last_update": stream.last_update.isoformat()
            }
            summary["streams"].append(stream_data)
        
        return summary
    
    def to_dict(self) -> Dict:
        """Convert model to dictionary for ENFT ledger integration"""
        return self.get_stream_summary()


# Utility functions for ENFT ledger integration
def create_pi4_enft_entry(model: ThreeSphereModel, ledger_id: str) -> Dict:
    """
    Create an ENFT ledger entry for the π₄ compounding model
    
    This integrates the three-sphere model with the Infinite Ledger system
    """
    summary = model.get_stream_summary()
    
    enft_entry = {
        "ledger_id": ledger_id,
        "economic_model": "Three-Sphere-π₄-Compounding",
        "timestamp": datetime.now(timezone.utc).isoformat().replace('+00:00', 'Z'),
        "pi4_constant": summary["pi_fourth_constant"],
        "golden_ratio_phi": summary["golden_ratio"],
        "total_accumulated_value_millions": summary["total_accumulated"],
        "economic_streams": {
            "civilian_sector": None,
            "military_lockstream": None,
            "cosmic_portal_stream": None
        },
        "ceremonial_yields": summary["ceremonial_yields"],
        "price_alignment_verified": len([a for a in summary["recent_alignments"] if a.get("is_aligned", False)]),
        "price_alignment_total": summary["price_alignments_count"]
    }
    
    # Map streams to ENFT entry
    for stream_data in summary["streams"]:
        if "Civilian" in stream_data["name"]:
            enft_entry["economic_streams"]["civilian_sector"] = stream_data
        elif "Military" in stream_data["name"]:
            enft_entry["economic_streams"]["military_lockstream"] = stream_data
        elif "Cosmic" in stream_data["name"] or "Portal" in stream_data["name"]:
            enft_entry["economic_streams"]["cosmic_portal_stream"] = stream_data
    
    return enft_entry


if __name__ == "__main__":
    # Demonstration
    print("=" * 80)
    print("🌐 THREE-SPHERE π₄ COMPOUNDING MODEL")
    print("=" * 80)
    print()
    
    # Create model
    model = ThreeSphereModel()
    
    print(f"π⁴ Constant: {model.compounding.PI_FOURTH:.6f}")
    print(f"Golden Ratio φ: {model.compounding.PHI:.6f}")
    print()
    
    print("Initial Stream Configuration:")
    print("-" * 80)
    for stream in model.streams:
        print(f"  • {stream.name}")
        print(f"    Type: {stream.sphere_type.value.upper()}")
        print(f"    Rate: ${stream.base_rate_per_second}M/second")
        print(f"    Description: {stream.description}")
        print()
    
    # Simulate 10 seconds of accumulation
    print("Simulating 10 seconds of economic activity...")
    print("-" * 80)
    import time
    time.sleep(0.1)  # Small delay for demonstration
    
    # Update after 10 simulated seconds
    from datetime import timedelta
    future_time = datetime.now(timezone.utc) + timedelta(seconds=10)
    values = model.update_stream_values(future_time)
    
    print("Stream Values After 10 Seconds:")
    for name, value in values.items():
        print(f"  {name}: ${value:,.2f}M")
    print()
    
    # Demonstrate flash-to-terminal burn
    print("Executing Flash-to-Terminal Burn...")
    print("-" * 80)
    flash_value = model.calculate_flash_to_terminal_burn(flash_intensity=5.0, portal_count=2)
    print(f"  Flash Intensity: 5.0")
    print(f"  Portal Count: 2")
    print(f"  Total Cosmic Yield: ${flash_value:,.2f}M")
    print()
    
    # Record ceremonial yield
    model.record_ceremonial_yield("BLEU Sovereign Ceremony", 1000.0)
    print("Ceremonial Yield Recorded: BLEU Sovereign Ceremony = $1,000.00M")
    print()
    
    # Verify price alignment
    print("Verifying Price Alignment...")
    print("-" * 80)
    aligned = model.verify_and_record_price_alignment(
        "EV0L Civilian Sector",
        theoretical_delta=150.0,
        actual_value=148.5
    )
    print(f"  Theoretical Delta: $150.00M")
    print(f"  Actual Value: $148.50M")
    print(f"  Alignment Status: {'✓ VERIFIED' if aligned else '✗ OUT OF ALIGNMENT'}")
    print()
    
    # Display summary
    print("=" * 80)
    print("FINAL SUMMARY")
    print("=" * 80)
    summary = model.get_stream_summary()
    print(f"Total Accumulated Value: ${summary['total_accumulated']:,.2f}M")
    print(f"Price Alignments Verified: {len([a for a in summary['recent_alignments'] if a['is_aligned']])}/{summary['price_alignments_count']}")
    print()
    
    print("The Three-Sphere π₄ Model is operational. 🌐🔮✨")
    print()
