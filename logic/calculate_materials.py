
from .models import Bar
from .opening import Opening
import math

class CalculateMaterials:
    def __init__(self, openings=None, bar_length=5900):
        if openings is None:
            openings = []
        self.slice = 4
        self.bar_length = bar_length
        self.openings = openings
        self.frame_bars = []
        self.grouped_frames = {} 

    def get_bar_length(self, serie):
        is_custom_length_serie = (serie == "probbaCorrediza" or serie == "probbaCorredizaTripleRiel" or serie == "galaCorredizaCuatroRieles" or serie == "galaCorredizaTripleRiel")
        return 6700 if is_custom_length_serie else self.bar_length

    def classify_frames(self):
        self.grouped_frames = {}
        for opening in self.openings:
            # Framing must have been called on opening
            if not opening.frames:
                opening.framing()
            
            for key, frame in opening.frames.items():
                if frame is None: continue
                
                # Convert code dict to a hashable format (sorted tuple of items)
                # This ensures frames with different names but same profile codes are grouped
                code_key = frozenset(frame.code.items())
                
                bar_length = self.get_bar_length(frame.serie)
                
                # Unique key for grouping: (bar_length, color, profile_codes)
                # We ignore the serie name to allow unification across compatible series
                group_key = (bar_length, frame.color, code_key)
                
                if group_key not in self.grouped_frames:
                    self.grouped_frames[group_key] = []
                self.grouped_frames[group_key].append(frame)

    def calculate_length_groups(self, frames):
        frame_elements = []
        for frame in frames:
            if frame.name == "Screen Shash" or frame.name == "U Dvh":
                 for _ in range(int(frame.width_quantity)):
                     frame_elements.append(frame.lenght['width'])
                 for _ in range(int(frame.height_quantity)):
                     frame_elements.append(frame.lenght['height'])
            else:
                 for _ in range(int(frame.quantity)):
                     frame_elements.append(frame.lenght)
        return frame_elements

    def calculate_frame_bars_quantity_with_custom_length(self, length_group, bar_length):
        slice_val = 4
        
        # 1. Sort Descending
        pieces = sorted(length_group, reverse=True)
        
        # 2. Initial Solution: Greedy
        best_solution, best_assignments = self.greedy_bin_packing(pieces, bar_length, slice_val)

        # 3. Threshold check
        if len(pieces) > 40:
            return best_solution, "Greedy", best_assignments

        # 4. Branch and Bound / DFS
        count_ref = len(pieces)
        bins = [0.0] * count_ref # Max bins = number of pieces
        
        # 4. Branch and Bound / DFS
        count_ref = len(pieces)
        bins = [0.0] * count_ref # Max bins = number of pieces
        
        # We need to use a mutable container for best_solution to modify it inside closure
        # Also track best assignments
        solution_wrapper = {'best': best_solution, 'assignments': best_assignments}
        
        # Track current assignments during recursion: list of bin indices for each piece [0, 1, 0, ...]
        current_assignments = [-1] * count_ref

        def dfs_bnb(current_piece_idx, bin_count):
            # Pruning 1
            if bin_count >= solution_wrapper['best']:
                return

            # Base case
            # Base case
            if current_piece_idx >= count_ref:
                if bin_count < solution_wrapper['best']:
                    solution_wrapper['best'] = bin_count
                    solution_wrapper['assignments'] = list(current_assignments) # Copy state
                return

            # Pruning 2: Lower Bound
            remaining_sum = 0
            for i in range(current_piece_idx, count_ref):
                remaining_sum += (pieces[i] + slice_val)
            
            current_free_space = 0
            for i in range(bin_count):
                current_free_space += bins[i]
            
            needed_volume = remaining_sum - current_free_space
            min_additional = 0
            if needed_volume > 0:
                min_additional = math.ceil(needed_volume / bar_length)

            if bin_count + min_additional >= solution_wrapper['best']:
                return

            piece_size = pieces[current_piece_idx] + slice_val

            # Try existing bins
            for i in range(bin_count):
                # Pruning 3: Symmetry Breaking
                symmetric = False
                for k in range(i):
                     if abs(bins[k] - bins[i]) < 0.001:
                         symmetric = True
                         break
                
                if symmetric: continue

                if bins[i] >= piece_size:
                    bins[i] -= piece_size
                    current_assignments[current_piece_idx] = i
                    dfs_bnb(current_piece_idx + 1, bin_count)
                    bins[i] += piece_size # Backtrack
                    current_assignments[current_piece_idx] = -1
                    
                    if solution_wrapper['best'] <= bin_count:
                        return

            # New bin
            if bin_count + 1 < solution_wrapper['best']:
                bins[bin_count] = bar_length - piece_size
                current_assignments[current_piece_idx] = bin_count
                dfs_bnb(current_piece_idx + 1, bin_count + 1)
                current_assignments[current_piece_idx] = -1

        dfs_bnb(0, 0)
        
        # Reconstruct detailed assignment structure from index list
        # solution_wrapper['assignments'] is like [0, 1, 0, 2] meaning piece 0 in bin 0, piece 1 in bin 1...
        # We want [[p0, p2], [p1], [p3]]
        
        final_assignments = []
        # Pre-allocate
        if solution_wrapper['assignments']:
             num_bins = max(solution_wrapper['assignments']) + 1 if solution_wrapper['assignments'] else 0
             # Note: max might be -1 if empty, but len(pieces) > 0 handled
             # Verify consistency: greedy returns bin_count? greedy returns (count, [[..], [..]])
             
             # Actually greedy implementation below needs update first to understand structure
             pass

        # Since greedy returns structured list, we should convert our flat index list to structured list
        # pieces are sorted desc.
        if solution_wrapper['assignments']:
            # Create list of empty lists
            num_bins = solution_wrapper['best'] # Should match max index + 1
            # Safety: use computed max to avoid index error if best is loosely tracked
            max_idx = max(solution_wrapper['assignments'])
            num_bins = max(num_bins, max_idx + 1)
            
            structured_assignments = [[] for _ in range(num_bins)]
            for p_idx, b_idx in enumerate(solution_wrapper['assignments']):
                if b_idx >= 0:
                    structured_assignments[b_idx].append(pieces[p_idx])
            
            return solution_wrapper['best'], "Optimal", structured_assignments

        return solution_wrapper['best'], "Optimal", [] # Should not happen if greedy worked

    def greedy_bin_packing(self, pieces, bar_length, slice_val=4):
        bins = [] # stores remaining space
        bin_contents = [] # stores list of pieces in each bin
        
        # pieces is assumed sorted desc
        for piece in pieces:
            placed = False
            piece_size = piece + slice_val
            for i in range(len(bins)):
                if bins[i] >= piece_size:
                    bins[i] -= piece_size
                    bin_contents[i].append(piece)
                    placed = True
                    break
            if not placed:
                bins.append(bar_length - piece_size)
                bin_contents.append([piece])
        return len(bins), bin_contents

    def calculate_frame_bars(self):
        self.classify_frames()
        self.frame_bars = []
        
        for key, frames_list in self.grouped_frames.items():
            if not frames_list: continue
            
            bar_length, color, profile_codes = key
            
            length_group = self.calculate_length_groups(frames_list)
            bars_quantity, method, details = self.calculate_frame_bars_quantity_with_custom_length(length_group, bar_length)
            
            if bars_quantity > 0:
                rep = frames_list[0]
                new_bar = Bar(
                    bars_quantity,
                    rep.spanish_name,
                    rep.serie,
                    rep.color,
                    rep.code,
                    calculation_method=method
                )
                new_bar.cutting_details = details
                self.frame_bars.append(new_bar)
    
    def get_frame_bars(self):
        self.calculate_frame_bars()
        return self.frame_bars
