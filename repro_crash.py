
def reproduction():
    pieces = [1000.0, 1000.0]
    # Mock Greedy Result: count=1, details=[[1000.0, 1000.0]]
    greedy_details = [[1000.0, 1000.0]]
    best_solution = 1
    
    # Buggy initialization
    solution_wrapper = {'best': best_solution, 'assignments': greedy_details}
    
    # Simulate BnB not finding better solution (so assignments remains greedy_details)
    
    # Reconstruction logic crash
    print("Attempting reconstruction...")
    try:
        # Code that assumes flat list
        num_bins = solution_wrapper['best']
        max_idx = max(solution_wrapper['assignments']) # max([[...]]) -> [1000.0, 1000.0]
        # num_bins = max(num_bins, max_idx + 1) -> max(1, [..] + 1) -> TypeError
        
        structured_assignments = [[] for _ in range(num_bins)]
        for p_idx, b_idx in enumerate(solution_wrapper['assignments']):
             # b_idx is [1000.0, 1000.0]
             if b_idx >= 0: # TypeError: '>' not supported between instances of 'list' and 'int'
                structured_assignments[b_idx].append(pieces[p_idx])
                
    except Exception as e:
        print(f"Caught Expected Crash: {e}")

if __name__ == "__main__":
    reproduction()
