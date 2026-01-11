
import customtkinter as ctk
from tkinter import messagebox, filedialog
import tkinter as tk # For constants like BOTH, etc. if needed, though ctk usually handles it
import json
import os
import sys

# Ensure we can import from local modules
try:
    from logic.opening import Opening
    from logic.calculate_materials import CalculateMaterials
    import utils
except ImportError as e:
    # If run as script
    sys.path.append(os.path.dirname(os.path.abspath(__file__)))
    from logic.opening import Opening
    from logic.calculate_materials import CalculateMaterials
    import utils

# --- THEME SETUP ---
ctk.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
ctk.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"

class FramesApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Frames Desktop")
        self.geometry("900x850")
        
        # --- Variables ---
        # ctk ComboBoxes use StringVar properly
        self.serie_var = ctk.StringVar(value="Select an Option")
        self.color_var = ctk.StringVar(value="Select an Option")
        self.vidrio_var = ctk.StringVar(value="Select an Option")
        self.premarco_var = ctk.StringVar(value="Select an Option")
        self.width_var = ctk.StringVar()
        self.height_var = ctk.StringVar()
        self.quantity_var = ctk.StringVar()
        
        self.openings_list = [] # Store Opening objects
        
        # Clear data on startup
        utils.clear_local_storage()
        self.openings_list = []

        # --- UI Layout ---
        self.create_widgets()
        self.update_openings_count()

    def create_widgets(self):
        # scrollable main frame if needed, but standard frame is fine for now
        self.main_frame = ctk.CTkFrame(self, corner_radius=10)
        self.main_frame.pack(fill="both", expand=True, padx=20, pady=20)

        # Title
        # Plasma color - purple/cyan accent
        title_label = ctk.CTkLabel(self.main_frame, text="Frames", font=("Roboto", 28, "bold"), text_color="#9F2B68") # Deep purple-ish
        title_label.pack(pady=(20, 10))
        
        # Count Label
        self.count_label = ctk.CTkLabel(self.main_frame, text="0 Openings Added", font=("Roboto", 14))
        self.count_label.pack(pady=(0, 20))

        # Form Frame
        self.form_frame = ctk.CTkFrame(self.main_frame, corner_radius=10, border_width=1, border_color="#555")
        self.form_frame.pack(fill="x", padx=20, pady=(0, 20))
        
        # Form Title inside the frame (simulating LabelFrame)
        ctk.CTkLabel(self.form_frame, text="Add Opening", font=("Roboto", 14, "bold")).grid(row=0, column=0, columnspan=4, pady=10)

        # Grid for form
        grid_opts = {'padx': 10, 'pady': 10, 'sticky': 'w'}
        
        # Row 1
        ctk.CTkLabel(self.form_frame, text="Serie").grid(row=1, column=0, **grid_opts)
        self.serie_cb = ctk.CTkComboBox(self.form_frame, variable=self.serie_var, values=[
            "s20", "s25", "s25TripleRiel", "probbaCorrediza", "probbaCorredizaTripleRiel", "galaCorredizaTripleRiel", "galaCorredizaCuatroRieles"
        ], width=200)
        self.serie_cb.grid(row=1, column=1, **grid_opts)
        
        ctk.CTkLabel(self.form_frame, text="Color").grid(row=1, column=2, **grid_opts)
        self.color_cb = ctk.CTkComboBox(self.form_frame, variable=self.color_var, values=[
            "anodizado", "anolok", "blanco", "imitacionMadera", "pintadoNegro"
        ], width=200)
        self.color_cb.grid(row=1, column=3, **grid_opts)

        # Row 2
        ctk.CTkLabel(self.form_frame, text="Vidrio").grid(row=2, column=0, **grid_opts)
        self.vidrio_cb = ctk.CTkComboBox(self.form_frame, variable=self.vidrio_var, values=[
            "simple", "dvh"
        ], width=200)
        self.vidrio_cb.grid(row=2, column=1, **grid_opts)
        
        ctk.CTkLabel(self.form_frame, text="Premarco").grid(row=2, column=2, **grid_opts)
        self.premarco_cb = ctk.CTkComboBox(self.form_frame, variable=self.premarco_var, values=[
            "Con Premarco", "Sin Premarco"
        ], width=200)
        self.premarco_cb.grid(row=2, column=3, **grid_opts)

        # Row 3
        ctk.CTkLabel(self.form_frame, text="Ancho (mm)").grid(row=3, column=0, **grid_opts)
        ctk.CTkEntry(self.form_frame, textvariable=self.width_var, width=200).grid(row=3, column=1, **grid_opts)
        
        ctk.CTkLabel(self.form_frame, text="Alto (mm)").grid(row=3, column=2, **grid_opts)
        ctk.CTkEntry(self.form_frame, textvariable=self.height_var, width=200).grid(row=3, column=3, **grid_opts)
        
        # Row 4
        ctk.CTkLabel(self.form_frame, text="Cantidad").grid(row=4, column=0, **grid_opts)
        ctk.CTkEntry(self.form_frame, textvariable=self.quantity_var, width=200).grid(row=4, column=1, **grid_opts)

        # Submit Button
        submit_btn = ctk.CTkButton(self.form_frame, text="Agregar Abertura", command=self.add_opening, 
                      fg_color="#6A0DAD", hover_color="#9F2B68", width=200, height=40) # Purple plasma
        submit_btn.grid(row=5, column=0, columnspan=4, pady=20)

        # Action Buttons
        btn_frame = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        btn_frame.pack(pady=10)
        
        # Styling action buttons
        action_btn_opts = {"width": 140, "height": 35, "fg_color": "#2E2E2E", "hover_color": "#444444", "border_width": 1, "border_color": "#6A0DAD"}
        
        ctk.CTkButton(btn_frame, text="Production", command=self.show_production, **action_btn_opts).pack(side="left", padx=5)
        ctk.CTkButton(btn_frame, text="Calculate Materials", command=self.show_materials, **action_btn_opts).pack(side="left", padx=5)
        ctk.CTkButton(btn_frame, text="Clear Data", command=self.clear_data, **action_btn_opts).pack(side="left", padx=5)

        # Print Button (Packed first at bottom to ensure visibility)
        ctk.CTkButton(self.main_frame, text="PRINT (Save PDF)", command=self.print_output, 
                      fg_color="#008B8B", hover_color="#00CED1", width=200, height=40).pack(side="bottom", pady=10)

        # Output Area
        self.output_text = ctk.CTkTextbox(self.main_frame, height=200)
        self.output_text.pack(fill="both", expand=True, padx=20, pady=10)

    def load_data(self):
        data = utils.get_local_storage()
        self.openings_list = []
        for d in data:
            # Reconstruct opening objects
            op = Opening(
                d["width"], d["height"], d["serie"], d["color"], 
                d["dvh"], d["preframe"], d["quantity"]
            )
            op.init()
            self.openings_list.append(op)

    def update_openings_count(self):
        total = sum(int(op.quantity) for op in self.openings_list)
        self.count_label.configure(text=f"{total} Openings Added")

    def add_opening(self):
        # Validation
        if self.serie_var.get() == "Select an Option" or self.width_var.get() == "" or self.quantity_var.get() == "":
            messagebox.showerror("Error", "Please fill required fields")
            return

        serie = self.serie_var.get()
        color = self.color_var.get()
        vidrio = self.vidrio_var.get()
        premarco = self.premarco_var.get()
        width = self.width_var.get()
        height = self.height_var.get()
        quantity = self.quantity_var.get()

        dvh = (vidrio == "dvh")
        preframe_bool = (premarco == "Con Premarco")

        # Create Opening
        op = Opening(width, height, serie, color, dvh, preframe_bool, quantity)
        op.init()

        # Add to memory and persisted storage
        self.openings_list.insert(0, op) # Prepend
        utils.add_to_local_storage(op) # Stores raw data at top

        print(f"Added opening: {serie} {width}x{height}")
        
        # Reset form
        self.serie_cb.set("Select an Option")
        self.color_cb.set("Select an Option")
        self.vidrio_cb.set("Select an Option")
        self.premarco_cb.set("Select an Option")
        self.width_var.set("")
        self.height_var.set("")
        self.quantity_var.set("")
        
        self.update_openings_count()
        messagebox.showinfo("Success", "Opening Added")

    def show_production(self):
        self.output_text.delete(1.0, tk.END)
        for op in self.openings_list:
            text = op.to_string().replace("\n", "\n\n")
            self.output_text.insert(tk.END, text)
    
    def show_materials(self):
        self.output_text.delete(1.0, tk.END)
        
        # Calculate
        calc = CalculateMaterials(self.openings_list)
        bars = calc.get_frame_bars()
        
        self.output_text.insert(tk.END, "Materials:\n\n")
        if not bars:
            self.output_text.insert(tk.END, "No materials calculated.\n\n")
        
        for bar in bars:
            line = f"{bar.quantity} Barra(s) de {bar.name} {bar.serie} {bar.color} [Method: {bar.calculation_method}] Codigos: Aluminios del Uruguay = {bar.code.get('aluminiosDelUruguay', 'N/A')} Juan = {bar.code.get('juan', 'N/A')} Urualum = {bar.code.get('urualum', 'N/A')} Abasur = {bar.code.get('abasur', 'N/A')}\n"
            self.output_text.insert(tk.END, line)
            
            if hasattr(bar, 'cutting_details') and bar.cutting_details:
                for i, cuts in enumerate(bar.cutting_details):
                    cuts_str = ", ".join([f"{c:.0f}" for c in cuts])
                    waste = bar.quantity * 0 # Placeholder if we want per-bar waste, but simple logic: 
                    # Actually bar.quantity is total bars. cutting_details is list of *unique patterns*? 
                    # NO. greedy/bnb returns specific bins for *all* pieces. 
                    # So len(cutting_details) should equal bar.quantity ideally.
                    
                    # calculate used
                    used = sum([c + 4 for c in cuts])
                    remaining = (6700 if bar.serie in ["probbaCorrediza", "probbaCorredizaTripleRiel", "galaCorredizaTripleRiel", "galaCorredizaCuatroRieles"] else 5900) - used + 4
                    
                    self.output_text.insert(tk.END, f"  Barra {i+1}: [{cuts_str}] (Resto: {remaining:.0f})\n")
            
            self.output_text.insert(tk.END, "\n")

    
    def print_output(self):
        # Generate PDF report
        content = self.output_text.get(1.0, tk.END)
        
        # Ask user for save location
        filename = filedialog.asksaveasfilename(
            defaultextension=".pdf",
            filetypes=[("PDF files", "*.pdf"), ("All files", "*.*")],
            title="Save Report As",
            initialfile="production_report.pdf"
        )
        
        if not filename: # User cancelled
            return

        try:
            utils.generate_pdf(filename, "Production Report", content)
            # Open the file - this allows user to print from PDF viewer
            os.startfile(filename)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to generate/open PDF report:\n{e}")


    def clear_data(self):
        if messagebox.askyesno("Confirm", "Are you sure you want to clear all data?"):
            utils.clear_local_storage()
            self.openings_list = []
            self.update_openings_count()
            self.output_text.delete(1.0, tk.END)

if __name__ == "__main__":
    app = FramesApp()
    app.mainloop()
