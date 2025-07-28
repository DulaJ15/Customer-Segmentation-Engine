from fpdf import FPDF
import os

class PersonaPDF(FPDF):
    def __init__(self, cluster_id, persona_data, radar_chart_path=None):
        super().__init__()
        self.cluster_id = cluster_id
        self.persona_data = persona_data
        self.radar_chart_path = radar_chart_path
        self.set_auto_page_break(auto=True, margin=15)
        self.add_page()
        self._create_report()

    def _create_report(self):
        self.set_font("Arial", "B", 16)
        self.cell(0, 10, f"🧠 Customer Persona - Cluster {self.cluster_id}", ln=True, align="C")

        self.ln(10)
        self.set_font("Arial", "", 12)

        for key, value in self.persona_data.items():
            self.multi_cell(0, 10, f"{key}: {value}", align="L")

        if self.radar_chart_path and os.path.exists(self.radar_chart_path):
            self.ln(5)
            self.image(self.radar_chart_path, x=30, w=150)

    def save(self, output_path):
        self.output(output_path)

# 🔧 Example usage
if __name__ == "__main__":
    example_persona = {
        "Segment Name": "High Value Loyalists",
        "Key Traits": "Frequent buyers, high average order value, low churn risk",
        "Avg. Spend": "$650",
        "Age Range": "30-45",
        "Preferred Region": "Urban South",
        "Behavior": "Buys monthly, prefers premium SKUs"
    }

    radar_chart = "charts/radar_cluster_1.png"  # optional radar chart
    output_file = "personas/persona_cluster_1.pdf"

    pdf = PersonaPDF(cluster_id=1, persona_data=example_persona, radar_chart_path=radar_chart)
    pdf.save(output_file)
