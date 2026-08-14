def inject_skills(self, spawn_id, skills):
    # ... existing code ...
    
    # Record the injected skills in the run record
    run_record = self.get_run_record(spawn_id)
    run_record['injected_skills'] = skills
    self.save_run_record(spawn_id, run_record)
    
    # ... existing code ...
