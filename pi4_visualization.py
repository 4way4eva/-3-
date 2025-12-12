#!/usr/bin/env python3
"""
π₄ Treasury Visualization
Creates visual representations of Quarter-Law traces and flow arcs.
"""

from pi4_treasury import Pi4TreasuryModel, EconomyType, QuarterLaw
from typing import Dict, List, Tuple
import json


class Pi4Visualizer:
    """
    Visualizes π₄ Treasury Model components including:
    - Quarter-Law flow traces
    - ENFT Ledger Stream
    - π₄ Compounding curves
    """
    
    def __init__(self, model: Pi4TreasuryModel):
        self.model = model
    
    def generate_ascii_compass(self, economy_type: EconomyType) -> str:
        """
        Generate an ASCII art compass showing Quarter-Law flows
        for a specific economy type.
        """
        stack = self.model.get_stack(economy_type)
        
        # Count flows for each direction
        flow_counts = {q: 0 for q in QuarterLaw}
        flow_values = {q: 0.0 for q in QuarterLaw}
        
        for arc in stack.flow_arcs:
            flow_counts[arc.target_quadrant] += 1
            flow_values[arc.target_quadrant] += arc.flow_value
        
        # Build ASCII compass
        compass = f"""
    ┌─────────────────────────────────────┐
    │      NORTH (Gold Refinery ✨)      │
    │   Flows: {flow_counts[QuarterLaw.NORTH]:2d}  Value: ${flow_values[QuarterLaw.NORTH]:>10,.0f}  │
    └──────────────┬──────────────────────┘
                   │
    ┌──────────────┼──────────────────────┐
    │              │                      │
    │   WEST      │ CENTER (Z-DNA ⬡)    │      EAST
    │  Energy⚡    │  Flows: {flow_counts[QuarterLaw.CENTER]:2d}         │   Oil 🛢️
    │ Flows: {flow_counts[QuarterLaw.WEST]:2d}   │  Value: ${flow_values[QuarterLaw.CENTER]:>6,.0f}    │  Flows: {flow_counts[QuarterLaw.EAST]:2d}
    │ ${flow_values[QuarterLaw.WEST]:>6,.0f}    │                      │  ${flow_values[QuarterLaw.EAST]:>6,.0f}
    │              │                      │
    └──────────────┼──────────────────────┘
                   │
    ┌──────────────┴──────────────────────┐
    │   SOUTH (Healing Milk & Honey 🍯)  │
    │   Flows: {flow_counts[QuarterLaw.SOUTH]:2d}  Value: ${flow_values[QuarterLaw.SOUTH]:>10,.0f}  │
    └─────────────────────────────────────┘
        """
        
        return compass
    
    def generate_flow_arc_table(self, economy_type: EconomyType) -> str:
        """Generate a detailed table of flow arcs for an economy"""
        stack = self.model.get_stack(economy_type)
        
        if not stack.flow_arcs:
            return "No flow arcs recorded."
        
        table = "\n"
        table += "┌─────────┬─────────┬────────────┬──────────────┐\n"
        table += "│  FROM   │   TO    │   VALUE    │  CURVATURE   │\n"
        table += "├─────────┼─────────┼────────────┼──────────────┤\n"
        
        for arc in stack.flow_arcs:
            from_q = arc.source_quadrant.value.upper()[:7]
            to_q = arc.target_quadrant.value.upper()[:7]
            value = f"${arc.flow_value:>8,.0f}"
            curve = f"{arc.curvature:>12.6f}"
            table += f"│ {from_q:<7} │ {to_q:<7} │ {value} │ {curve} │\n"
        
        table += "└─────────┴─────────┴────────────┴──────────────┘\n"
        
        return table
    
    def generate_enft_stream_table(self, economy_type: EconomyType) -> str:
        """Generate a table showing ENFT assets and their loop rates"""
        stack = self.model.get_stack(economy_type)
        
        if not stack.enft_assets:
            return "No ENFT assets minted."
        
        table = "\n"
        table += "┌─────────────────────┬──────────────┬────────────┬─────────────┐\n"
        table += "│      ENFT ID        │  BASE VALUE  │   YIELD    │  LOOP RATE  │\n"
        table += "├─────────────────────┼──────────────┼────────────┼─────────────┤\n"
        
        for asset in stack.enft_assets:
            enft_id = asset.enft_id[:19]
            base_val = f"${asset.base_value:>11,.0f}"
            total_yield = f"${asset.get_total_yield():>9,.0f}"
            loop_rate = asset.get_loop_rate()
            rate_str = f"{loop_rate['entry_count']:>3} entries"
            
            table += f"│ {enft_id:<19} │ {base_val} │ {total_yield} │ {rate_str:<11} │\n"
        
        table += "└─────────────────────┴──────────────┴────────────┴─────────────┘\n"
        
        return table
    
    def generate_es0il_mirror_map(self, economy_type: EconomyType) -> str:
        """Generate visualization of ES0IL layer mirroring"""
        stack = self.model.get_stack(economy_type)
        
        if not stack.enft_assets:
            return "No ENFT assets to visualize."
        
        layers = {"energy": 0, "legal": 0, "esoteric": 0, "operational": 0}
        
        for asset in stack.enft_assets:
            for layer, entries in asset.es0il_mirrors.items():
                layers[layer] += len(entries)
        
        viz = "\n"
        viz += "┌────────────────────────────────────────┐\n"
        viz += "│     ES0IL Multi-Dimensional Layers     │\n"
        viz += "├────────────────────────────────────────┤\n"
        
        for layer, count in layers.items():
            bar = "█" * min(count, 30)
            viz += f"│ {layer.upper():<12} │ {bar:<30} {count:>2} │\n"
        
        viz += "└────────────────────────────────────────┘\n"
        
        return viz
    
    def generate_pi4_compounding_chart(self, periods: int = 10) -> str:
        """Generate ASCII chart showing π₄ compounding effect"""
        demo = self.model.demonstrate_pi4_compounding(1000.0, periods)
        results = demo["demonstration"]
        
        chart = "\n"
        chart += "π₄ COMPOUNDING: Linear vs Overscale\n"
        chart += "─" * 60 + "\n"
        
        max_value = max(r["pi4_yield"] for r in results)
        scale = 50.0 / max_value if max_value > 0 else 1.0
        
        for r in results:
            period = r["period"]
            linear = r["linear_yield"]
            pi4 = r["pi4_yield"]
            ratio = r["overscale_ratio"]
            
            linear_bar = "▪" * int(linear * scale)
            pi4_bar = "█" * int(pi4 * scale)
            
            chart += f"P{period:2d} │ Linear: {linear_bar:<20} ${linear:>8,.2f}\n"
            chart += f"    │ π₄:     {pi4_bar:<20} ${pi4:>8,.2f} (×{ratio:.1f})\n"
            chart += "    ├" + "─" * 55 + "\n"
        
        return chart
    
    def generate_triple_stack_summary(self) -> str:
        """Generate summary visualization of all three economy stacks"""
        summary = "\n"
        summary += "╔════════════════════════════════════════════════════════════════╗\n"
        summary += "║          π₄ TREASURY MODEL - TRIPLE-STACK SUMMARY             ║\n"
        summary += "╚════════════════════════════════════════════════════════════════╝\n\n"
        
        for economy_type in [EconomyType.CIVILIAN, EconomyType.MILITARY, EconomyType.COSMIC]:
            stack = self.model.get_stack(economy_type)
            icon = "🏛️ " if economy_type == EconomyType.CIVILIAN else \
                   "⚔️ " if economy_type == EconomyType.MILITARY else "🌌"
            
            summary += f"\n{icon} {economy_type.value.upper()} ECONOMY\n"
            summary += "─" * 60 + "\n"
            summary += f"Balance:      ${stack.balance:>15,.2f}\n"
            summary += f"Flow Arcs:    {len(stack.flow_arcs):>15}\n"
            summary += f"ENFT Assets:  {len(stack.enft_assets):>15}\n"
            summary += f"Total Yield:  ${stack.get_total_yield():>15,.2f}\n"
            
            flow_summary = stack.get_flow_summary()
            summary += f"Total Flow:   ${flow_summary['total_flow_value']:>15,.2f}\n"
            summary += f"Avg Curvature:{flow_summary['average_curvature']:>15.6f}\n"
        
        return summary
    
    def generate_complete_visualization(self) -> str:
        """Generate a complete visual report of the entire π₄ Treasury Model"""
        report = []
        
        report.append("=" * 80)
        report.append("π₄ TREASURY MODEL - COMPLETE VISUALIZATION")
        report.append("=" * 80)
        
        # Triple-stack summary
        report.append(self.generate_triple_stack_summary())
        
        # Detailed views for each economy
        for economy_type in [EconomyType.CIVILIAN, EconomyType.MILITARY, EconomyType.COSMIC]:
            icon = "🏛️ " if economy_type == EconomyType.CIVILIAN else \
                   "⚔️ " if economy_type == EconomyType.MILITARY else "🌌"
            
            report.append("\n" + "=" * 80)
            report.append(f"{icon} {economy_type.value.upper()} ECONOMY - DETAILED VIEW")
            report.append("=" * 80)
            
            # Compass visualization
            report.append("\nQuarter-Law Compass:")
            report.append(self.generate_ascii_compass(economy_type))
            
            # Flow arc table
            report.append("\nFlow Arc Details:")
            report.append(self.generate_flow_arc_table(economy_type))
            
            # ENFT stream table
            report.append("\nENFT Ledger Stream:")
            report.append(self.generate_enft_stream_table(economy_type))
            
            # ES0IL mirror map
            report.append("\nES0IL Layer Mirroring:")
            report.append(self.generate_es0il_mirror_map(economy_type))
        
        # π₄ Compounding demonstration
        report.append("\n" + "=" * 80)
        report.append("π₄ COMPOUNDING PROTOCOL DEMONSTRATION")
        report.append("=" * 80)
        report.append(self.generate_pi4_compounding_chart(10))
        
        report.append("\n" + "=" * 80)
        report.append("✨ π₄ TREASURY VISUALIZATION COMPLETE")
        report.append("=" * 80)
        
        return "\n".join(report)
    
    def save_visualization(self, filename: str = "pi4_visualization.txt") -> None:
        """Save complete visualization to a text file"""
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(self.generate_complete_visualization())


def main():
    """Demonstrate visualization capabilities"""
    from pi4_integration import demonstrate_integration
    
    print("Generating π₄ Treasury Visualization...")
    print()
    
    # Use the integrated ledger to get a populated model
    ledger = demonstrate_integration()
    
    # Create visualizer
    visualizer = Pi4Visualizer(ledger.pi4_treasury)
    
    # Generate and display complete visualization
    print("\n" + "=" * 80)
    print("GENERATING COMPLETE VISUALIZATION")
    print("=" * 80)
    
    viz = visualizer.generate_complete_visualization()
    print(viz)
    
    # Save to file
    visualizer.save_visualization("pi4_visualization.txt")
    print("\n💾 Visualization saved to: pi4_visualization.txt")
    

if __name__ == "__main__":
    main()
