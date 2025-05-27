from flask import render_template, session
from classes.actors import Actors
from classes.studios import Studios
from datafile import filename

import pandas as pd
from sqlalchemy import create_engine
import matplotlib.pyplot as plt
import io
import base64

def apps_plot():
    engine = create_engine('sqlite:///' + filename + 'base.db')
    df_movies = pd.read_sql('Movies', con=engine)

    result = df_movies.groupby('studios_id').size()

    studio_ids = result.index
    studio_names = []
    for sid in studio_ids:
        studio_obj = Studios.obj.get(sid)
        studio_names.append(studio_obj.name if studio_obj else f"ID {sid}")

    movie_counts = result.values

    fig, ax = plt.subplots()
    ax.bar(studio_names, movie_counts, color="#AB9BC2")
    ax.set_xlabel('Studios')
    ax.set_ylabel('Number of films')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()

    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    plt.close(fig)
    buf.seek(0)
    image1 = base64.b64encode(buf.getvalue()).decode('utf-8')

    df_cast = pd.read_sql('Cast', con=engine)
    actor_counts = df_cast.groupby('actors_id').size().sort_values(ascending=False).head(10)
    actor_ids = actor_counts.index
    actor_names = []
    for aid in actor_ids:
        actor_obj = Actors.obj.get(aid)
        actor_names.append(actor_obj.name if actor_obj else f"ID {aid}")
    movie_counts_actors = actor_counts.values

    fig2, ax2 = plt.subplots()
    ax2.bar(actor_names, movie_counts_actors, color="#9C8AB6")
    ax2.set_xlabel('Actors')
    ax2.set_ylabel('Number of films')
    plt.setp(ax2.get_xticklabels(), rotation=45, ha='right')
    plt.tight_layout()
    buf2 = io.BytesIO()
    plt.savefig(buf2, format='png')
    plt.close(fig2)
    buf2.seek(0)
    image2 = base64.b64encode(buf2.getvalue()).decode('utf-8')

    return render_template("plot.html", image1=image1, image2=image2, ulogin=session.get("user"))
    