import pandas as pd
from pathlib import Path

# Create an ExcelWriter object to save multiple sheets
with pd.ExcelWriter("votes_feedback_data.xlsx", engine="openpyxl") as writer:
    votes = ['battle', 'upvote', 'downvote']
    
    for vote in votes:
        df_all = pd.DataFrame()
        fpaths = Path(".").rglob(f"clean_{vote}_conv_*.json")
        
        for fpath in fpaths:
            print(fpath)
            dft = pd.read_json(fpath)
            print(dft.head())
            print(dft.shape)
            df_all = pd.concat([df_all, dft])
        
        # Save df_all to a sheet named after the vote
        df_all.to_excel(writer, sheet_name=vote, index=False)