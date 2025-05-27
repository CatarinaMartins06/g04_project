from flask import render_template, session
from classes.actors import Actors
from classes.movies import Movies
from classes.studios import Studios
from datafile import filename

import pandas as pd
from sqlalchemy import create_engine
import plotly.express as px

def apps_plotly():
    engine = create_engine('sqlite:///' + filename + 'base.db')
    df_movies = pd.read_sql('Movies', con=engine)

    result = df_movies.groupby('studios_id').size()

    studio_ids = result.index
    studio_names = []
    for sid in studio_ids:
        studio_obj = Studios.obj.get(sid)
        studio_names.append(studio_obj.name if studio_obj else f"ID {sid}")

    movie_counts = result.values

    df_plot = pd.DataFrame({'Estúdio': studio_names, 'Número de Filmes': movie_counts})
    fig = px.bar(
        df_plot,
        x='Estúdio',
        y='Número de Filmes',
        labels={'Estúdio': 'Estúdio', 'Número de Filmes': 'Número de Filmes'},
        color_discrete_sequence=['#9C8AB6']
        )

    df_plot = pd.DataFrame({'Studio': studio_names, 'Number of Movies': movie_counts})

    fig = px.bar(
        df_plot,
        x='Studio',
        y='Number of Movies',
        labels={'Studio': 'Studio', 'Number of Movies': 'Number of Movies'},
        color_discrete_sequence=['#9C8AB6']
    )

    plot_div_studios = fig.to_html(full_html=False, div_id='my-plot')

    df_cast = pd.read_sql('Cast', con=engine)
    actor_counts = df_cast.groupby('actors_id').size()
    top_actors = actor_counts.sort_values(ascending=False).head(10)
    actor_ids = top_actors.index
    counts = top_actors.values
    actor_names = []
    for aid in actor_ids:
        actor_obj = Actors.obj.get(aid)
        actor_names.append(actor_obj.name if actor_obj else f"ID {aid}")
    df_actors = pd.DataFrame({'Actor': actor_names, 'Number of Movies': counts})

    fig_actors = px.bar(
        df_actors,
        x='Actor',
        y='Number of Movies',
        labels={'Actor': 'Actor', 'Number of Movies': 'Number of Movies'},
        color_discrete_sequence=["#AB9BC2"]
    )

    plot_div_actors = fig_actors.to_html(full_html=False, div_id='actors-plot')

    return render_template(
        "plotly.html", 
        plot_div_studios=plot_div_studios, 
        plot_div_actors=plot_div_actors, 
        ulogin=session.get("user")
    )
