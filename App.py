from flask import (Flask, render_template, request, url_for, Blueprint, g, Response, redirect, flash)
from flask_mysqldb import MySQL
from imdb import IMDb
import tmdbsimple as tmdb


tmdb.API_KEY = 'b888b64c9155c26ade5659ea4dd60e64'

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'searchflix'
mysql = MySQL(app)

app.secret_key='mysecretkey'

local=False

# enable_extra - loads poster and plot overview from tmdb for movie info
enable_extra=True

# to laod posters on profile page
posters_on_profile_page=True

tmdb_img_url = r'https://image.tmdb.org/t/p/w342'

ia = IMDb()

@app.route('/')
def index():
    return render_template('index.html')
    """ return render_template('index.html').replace('<html lang="en"',
            '<html lang="en" style="background-image:url(../static/img/bg.jpg)"'
            ,1) """

@app.route('/busqueda')
def busqueda():
    query = request.args.get('pelicula', None)
    
    if query:
        q_res = ia.search_movie(query)
        q_res[0]
        results = []
        for m in q_res:
            try:
                 results.append({
                    'id': m['Movie id'],
                    'title': m['title'],
                    'year': m['startYear'],
                    'kind': m['kind']
                })
            except KeyError:
                pass
        else:
            results =[{
                'id': m.getID(),
                'cover': m['cover url'],
                'title': m['title'],
                'year': m['year'],
                'kind': m['kind']
            }for m in q_res]
    return render_template('busqueda.html', results=results,
            local=local).replace('<html lang="en"',
                '<html lang="en" style="background-color:#efefef"',
                 1)




@app.route('/informacion')
def informacion():
    movid = request.args.get('id', None)
    if not movid:
        return('')
    else:
        mov = ia.get_movie(movid)
        movie={}

        titulo_largo = mov.get('long imdb title')
        titulo = mov.get('title')
        rating = rating = mov.get('rating', None)
        generos = (", ".join(mov.get('genres', []))).title()
        runmin = 0
        if mov.get('runtime'):
            runmin = int(mov.get('runtime',['0'])[0])
        runtime = "{}h {}m".format(runmin//60, runmin%60)


        director = ''
        escritor = ''
        if mov.get('director'):
            director = mov.get('director')[0]['name']
        if mov.get('writer'):
            escritor = mov.get('writer')[0]['name']
        
        cover = mov.get('full-size cover url', None)
        plot = mov.get('plot', [''])[0].split('::')[0]

        if enable_extra:
            find = tmdb.Find('tt{:07}'.format(int(movid)))
            find.info(external_source='imdb_id')
            if (find.movie_results and find.movie_results[0]['poster_path']
            and find.movie_results[0]['overview']):
                cover = tmdb_img_url + find.movie_results[0]['poster_path']
                plot = find.movie_results[0]['overview']
            elif (find.tv_results and find.tv_results[0]['poster_path']
            and find.tv_results[0]['overview']):
                cover = tmdb_img_url + find.tv_results[0]['poster_path']
                plot = find.tv_results[0]['overview']

        movie = {
                'id': mov.getID(),
                'long title': titulo_largo,
                'title': titulo,
                'rating': rating if rating else '',
                'genres': generos,
                'runtime': runtime,
                'director': director,
                'writer': escritor,
                'plot': plot if plot else '',
                'cover': cover if cover else ''
        }


        visitadas(movie)

        return render_template("informacion.html",
                movie=movie).replace(
                '<html lang="en"',
                '<html lang="en" style="background-color:#efefef"',
                1)

@app.route('/top-peliculas')
def topPeliculas():
    top = ia.get_top250_movies()
    results = []
    for m in top:
        try:
            results.append({
                'id': m['Movie id'],
                'title': m['title'],
                'year': m['startYear'],
                'kind': m['kind']
            })
        except KeyError:
            pass
    else:
        results =[{
            'id': m.getID(),
            
            'title': m['title'],
            'year': m['year'],
            'kind': m['kind']
        }for m in top]
    return render_template('top-peliculas.html',results=results,
            local=local)

@app.route('/top-shows')
def topShows():
    top = ia.get_top250_tv()
    results = []
    for m in top:
        try:
            results.append({
                'id': m['Movie id'],
                'title': m['title'],
                'year': m['startYear'],
                'kind': m['kind']
            })
        except KeyError:
            pass
    else:
        results =[{
            'id': m.getID(),
            
            'title': m['title'],
            'year': m['year'],
            'kind': m['kind']
        }for m in top]
    return render_template('top-shows.html',results=results,
            local=local)

@app.route('/recomendar', methods=['POST'])
def recomendar():
    if request.method == 'POST':
        id = request.form['id']
        titulo = request.form['titulo']
        poster = request.form['poster']
        rating = request.form['rating']
        genero = request.form['genero']
        duracion = request.form['duracion']
        trama = request.form['trama']
        director = request.form['director']
        escritor = request.form['escritor']
        cur = mysql.connection.cursor()

        query_strin = 'SELECT id FROM recomendar WHERE id = %s'
        cur.execute(query_strin,(id,))
        data = cur.fetchall()
        
        if data:
            flash('Gracias por recomendar esta pelicula')
            return redirect(url_for('index'))
        else:
            cur.execute('INSERT INTO recomendar VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)',
            (id, titulo, poster, rating, genero, duracion, trama, director, escritor))
            mysql.connection.commit()
            

        flash('Gracias por recomendar esta pelicula')
        return redirect(url_for('index'))

@app.route('/recomendada')
def recomendada():
    cur = mysql.connection.cursor()
    query_strin = 'SELECT id, titulo, poster,rating, genero FROM recomendar'
    cur.execute(query_strin)
    data = cur.fetchall()
    
    #print(datos)
    #return "hola"
    return render_template('recomendada.html',resultado=data)

@app.route('/visitadas')
def visitadas(movie):
    cur = mysql.connection.cursor()
    cur.execute('INSERT INTO visitadas VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)',
            (movie['id'], movie['long title'], movie['title'], movie['rating'], movie['genres'], movie['runtime'], movie['director'], movie['writer'], movie['plot'],movie['cover']))
    mysql.connection.commit()
    return "exito"

@app.route('/recientes')
def recientes():
    cur = mysql.connection.cursor()
    query_strin = 'SELECT id,long_titulo,rating,generos,cover FROM visitadas'
    cur.execute(query_strin)
    data = cur.fetchall()
    
    #print(datos)
    #return "hola"
    return render_template('recientes.html',resultado=data)





if __name__ == '__main__':
    app.run(port = 3000, debug = True)

