import pandas as pd
import streamlit as st
from sqlalchemy import create_engine, text

engine = create_engine("postgresql://postgres:123@localhost:5432/Football")

st.title("⚽ Football Dashboard")

teams = pd.read_sql("SELECT nom_equipe FROM equipe ORDER BY nom_equipe", engine)
selected_team = st.selectbox("Filtrer par équipe :", ["Toutes"] + teams["nom_equipe"].tolist())

if selected_team == "Toutes":
    team_filter = ""
else:
    team_filter = f"WHERE e.nom_equipe = '{selected_team}'"

top_scorers = pd.read_sql_query(text(f"""
    SELECT j.nom_joueur, e.nom_equipe, s.buts
    FROM joueur j
    JOIN statistique_joueur s ON j.id_joueur = s.id_joueur
    JOIN equipe e ON j.id_equipe = e.id_equipe
    {team_filter}
    ORDER BY s.buts DESC
    LIMIT 10;
"""), engine)

ranking = pd.read_sql_query(text(f"""
    SELECT e.nom_equipe,
           SUM(CASE WHEN r.resultat = 'Victoire' THEN 3
                    WHEN r.resultat = 'Nul' THEN 1 ELSE 0 END) AS points,
           SUM(r.buts_marques) AS buts_marques,
           SUM(r.buts_concedes) AS buts_concedes
    FROM resultat_match r
    JOIN equipe e ON r.id_equipe = e.id_equipe
    GROUP BY e.nom_equipe
    ORDER BY points DESC;
"""), engine)

st.subheader("🏅 Top 10 buteurs")
st.bar_chart(top_scorers.set_index("nom_joueur")["buts"])
st.dataframe(top_scorers)

csv = top_scorers.to_csv(index=False).encode('utf-8')
st.download_button("Télécharger CSV", csv, "top_buteurs.csv", "text/csv")

st.subheader("📊 Classement des équipes")
st.dataframe(ranking)
st.bar_chart(ranking.set_index("nom_equipe")["points"])

csv2 = ranking.to_csv(index=False).encode('utf-8')
st.download_button("Télécharger classement", csv2, "classement.csv", "text/csv")
