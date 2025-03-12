import streamlit as st
import pandas as pd
import plotly.express as px
import time
import random

def main():
    st.title("Cheater Statistics Estimator")

    # Game options
    game_options = ["Fortnite", "League of Legends", "Counter-Strike: GO", "Minecraft", "Grand Theft Auto V",
                    "Call of Duty: Warzone", "Apex Legends", "Valorant", "Overwatch", "PUBG"]

    # Input fields
    game_name = st.selectbox("Select Game:", game_options)
    player_alias = st.text_input("Enter Player Alias:", "SuspiciousPlayer123")

    if player_alias:
        # Simulate loading
        with st.spinner("Generating statistics..."):
            time.sleep(2)  # Simulate a 2-second loading time

            # Generate unique data based on player alias
            random.seed(player_alias)  # Use player alias as seed for reproducibility
            detection_rate = round(random.uniform(0.05, 0.25), 2)
            suspicious_behavior = round(random.uniform(0.10, 0.40), 2)
            vulnerability_exploits = round(random.uniform(0.01, 0.10), 2)

            data = {
                "Statistic": ["Detection Rate", "Suspicious Behavior", "Vulnerability Exploits"],
                "Value": [detection_rate, suspicious_behavior, vulnerability_exploits]
            }
            df = pd.DataFrame(data)

            # Display data
            st.write(f"Estimated Cheater Statistics for {player_alias} in {game_name}:")
            st.dataframe(df)

            # Visualization
            fig = px.bar(df, x="Statistic", y="Value", labels={'Value': 'Percentage'}, title='Cheater Statistics')
            st.plotly_chart(fig)

if __name__ == "__main__":
    main()