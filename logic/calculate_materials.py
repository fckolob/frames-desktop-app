
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

    def classify_frames(self):
        self.grouped_frames = {}
        for opening in self.openings:
            # Framing must have been called on opening
            if not opening.frames:
                opening.framing()
            
            for key, frame in opening.frames.items():
                if frame is None: continue
                # Unique key for grouping: (serie, color, name)
                # This groups standard frames
                group_key = (frame.serie, frame.color, frame.name)
                
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
        if len(length_group) > 100:
            return self.greedy_bin_packing(length_group, bar_length, 4)
        
        pieces = sorted(length_group, reverse=True)
        memo = {}

        def helper(index, remains):
            # JS Logic: Math.min(...pieces.slice(index))
            if index >= len(pieces):
                return 0
            
            min_remaining_piece = min(pieces[index:])
            filtered_remains = [r for r in remains if r >= min_remaining_piece + 4]
            
            key = f"{index}|{','.join(map(str, sorted(filtered_remains)))}"
            if key in memo:
                return memo[key]

            min_bars = float('inf')
            piece = pieces[index]
            
            # Try to put in existing bin
            for i in range(len(filtered_remains)):
                if filtered_remains[i] >= piece + 4:
                    new_remains = list(filtered_remains)
                    new_remains[i] -= (piece + 4)
                    res = helper(index + 1, new_remains)
                    min_bars = min(min_bars, res)

            # Try to start new bin
            new_remain = bar_length - (piece + 4)
            res_new = 1 + helper(index + 1, remains + [new_remain])
            min_bars = min(min_bars, res_new)
            
            memo[key] = min_bars
            return min_bars

        return helper(0, [])

    def greedy_bin_packing(self, pieces, bar_length, slice_val=4):
        bins = []
        pieces = sorted(pieces, reverse=True)
        for piece in pieces:
            placed = False
            for i in range(len(bins)):
                if bins[i] >= piece + slice_val:
                    bins[i] -= (piece + slice_val)
                    placed = True
                    break
            if not placed:
                bins.append(bar_length - (piece + slice_val))
        return len(bins)

    def calculate_frame_bars(self):
        self.classify_frames()
        self.frame_bars = []
        
        for key, frames_list in self.grouped_frames.items():
            if not frames_list: continue
            
            serie, color, name = key
            
            is_custom_length_serie = (serie == "probbaCorrediza" or serie == "probbaCorredizaTripleRiel" or serie == "galaCorredizaCuatroRieles")
            current_bar_length = 6700 if is_custom_length_serie else self.bar_length
            
            length_group = self.calculate_length_groups(frames_list)
            bars_quantity = self.calculate_frame_bars_quantity_with_custom_length(length_group, current_bar_length)
            
            if bars_quantity > 0:
                rep = frames_list[0]
                self.frame_bars.append(Bar(
                    bars_quantity,
                    rep.spanish_name,
                    rep.serie,
                    rep.color,
                    rep.code
                ))
    
    def get_frame_bars(self):
        self.calculate_frame_bars()
        return self.frame_bars
