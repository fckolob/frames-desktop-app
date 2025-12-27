
import tkinter as tk
from tkinter import ttk, messagebox, filedialog
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

class FramesApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Frames Desktop")
        self.root.geometry("800x800")
        
        # --- Variables ---
        self.serie_var = tk.StringVar(value="Select an Option")
        self.color_var = tk.StringVar(value="Select an Option")
        self.vidrio_var = tk.StringVar(value="Select an Option")
        self.premarco_var = tk.StringVar(value="Select an Option")
        self.width_var = tk.StringVar()
        self.height_var = tk.StringVar()
        self.quantity_var = tk.StringVar()
        
        self.openings_list = [] # Store Opening objects
        
        # Load from storage on init
        self.load_data()

        # --- UI Layout ---
        self.create_widgets()
        self.update_openings_count()

    def create_widgets(self):
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.pack(fill=tk.BOTH, expand=True)

        # Title
        ttk.Label(main_frame, text="Frames", font=("Helvetica", 24, "bold")).pack(pady=(0, 10))
        
        # Count Label
        self.count_label = ttk.Label(main_frame, text="0 Openings Added", font=("Helvetica", 12))
        self.count_label.pack(pady=(0, 20))

        # Form Frame
        form_frame = ttk.LabelFrame(main_frame, text="Add Opening", padding="10")
        form_frame.pack(fill=tk.X, pady=(0, 20))

        # Grid for form
        grid_opts = {'padx': 5, 'pady': 5, 'sticky': 'w'}
        
        # Row 0
        ttk.Label(form_frame, text="Serie").grid(row=0, column=0, **grid_opts)
        self.serie_cb = ttk.Combobox(form_frame, textvariable=self.serie_var, state="readonly", values=[
            "s20", "s25", "s25TripleRiel", "probbaCorrediza", "probbaCorredizaTripleRiel"
        ])
        self.serie_cb.grid(row=0, column=1, **grid_opts)
        
        ttk.Label(form_frame, text="Color").grid(row=0, column=2, **grid_opts)
        self.color_cb = ttk.Combobox(form_frame, textvariable=self.color_var, state="readonly", values=[
            "anodizado", "anolok", "blanco", "imitacionMadera", "pintadoNegro"
        ])
        self.color_cb.grid(row=0, column=3, **grid_opts)

        # Row 1
        ttk.Label(form_frame, text="Vidrio").grid(row=1, column=0, **grid_opts)
        self.vidrio_cb = ttk.Combobox(form_frame, textvariable=self.vidrio_var, state="readonly", values=[
            "simple", "dvh"
        ])
        self.vidrio_cb.grid(row=1, column=1, **grid_opts)
        
        ttk.Label(form_frame, text="Premarco").grid(row=1, column=2, **grid_opts)
        self.premarco_cb = ttk.Combobox(form_frame, textvariable=self.premarco_var, state="readonly", values=[
            "Con Premarco", "Sin Premarco"
        ])
        self.premarco_cb.grid(row=1, column=3, **grid_opts)

        # Row 2
        ttk.Label(form_frame, text="Ancho (mm)").grid(row=2, column=0, **grid_opts)
        ttk.Entry(form_frame, textvariable=self.width_var).grid(row=2, column=1, **grid_opts)
        
        ttk.Label(form_frame, text="Alto (mm)").grid(row=2, column=2, **grid_opts)
        ttk.Entry(form_frame, textvariable=self.height_var).grid(row=2, column=3, **grid_opts)
        
        # Row 3
        ttk.Label(form_frame, text="Cantidad").grid(row=3, column=0, **grid_opts)
        ttk.Entry(form_frame, textvariable=self.quantity_var).grid(row=3, column=1, **grid_opts)

        # Submit Button
        ttk.Button(form_frame, text="Agregar Abertura", command=self.add_opening).grid(row=4, column=0, columnspan=4, pady=10)

        # Action Buttons
        btn_frame = ttk.Frame(main_frame)
        btn_frame.pack(pady=10)
        ttk.Button(btn_frame, text="Production", command=self.show_production).pack(side=tk.LEFT, padx=5)
        ttk.Button(btn_frame, text="Calculate Materials", command=self.show_materials).pack(side=tk.LEFT, padx=5)
        
        # New: Reset Button
        ttk.Button(btn_frame, text="Clear Data", command=self.clear_data).pack(side=tk.LEFT, padx=5)

        # Output Area
        output_frame = ttk.Frame(main_frame)
        output_frame.pack(fill=tk.BOTH, expand=True)
        
        self.output_text = tk.Text(output_frame, height=10) # Scrollable via scrollbar
        scrollbar = ttk.Scrollbar(output_frame, orient="vertical", command=self.output_text.yview)
        self.output_text.configure(yscrollcommand=scrollbar.set)
        
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.output_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Print Button (Hidden by default or shown always, simplified)
        self.print_btn = ttk.Button(main_frame, text="PRINT", command=self.print_output)
        self.print_btn.pack(pady=10)

    def load_data(self):
        data = utils.get_local_storage()
        self.openings_list = []
        for d in data:
            # Reconstruct opening objects
            # Keys in json: "width", "height", "serie", etc.
            op = Opening(
                d["width"], d["height"], d["serie"], d["color"], 
                d["dvh"], d["preframe"], d["quantity"]
            )
            # We don't need to init() yet unless we use them, but let's init
            op.init()
            self.openings_list.append(op)

    def update_openings_count(self):
        total = sum(int(op.quantity) for op in self.openings_list)
        self.count_label.config(text=f"{total} Openings Added")

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
            text = op.to_string()
            self.output_text.insert(tk.END, text + "\n")
    
    def show_materials(self):
        self.output_text.delete(1.0, tk.END)
        
        # Calculate
        calc = CalculateMaterials(self.openings_list)
        bars = calc.get_frame_bars()
        
        self.output_text.insert(tk.END, "Materials:\n\n")
        if not bars:
            self.output_text.insert(tk.END, "No materials calculated.\n")
        
        for bar in bars:
            line = f"{bar.quantity} Barra(s) de {bar.name} {bar.serie} {bar.color} Codigos: Aluminios del Uruguay = {bar.code.get('aluminiosDelUruguay', 'N/A')} Juan = {bar.code.get('juan', 'N/A')} Urualum = {bar.code.get('urualum', 'N/A')} Abasur = {bar.code.get('abasur', 'N/A')}\n"
            self.output_text.insert(tk.END, line)

    
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
    root = tk.Tk()
    app = FramesApp(root)
    root.mainloop()
