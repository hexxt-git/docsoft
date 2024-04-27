from flask import Flask, request, jsonify
import psycopg2

app = Flask(__name__)

# Connexion à la base de données PostgreSQL
conn = psycopg2.connect(
    dbname="api",
    user="postgres",
    password="agoudjil",
    host="localhost",
    port="5017"
)
cursor = conn.cursor()


@app.route('/api/recherche', methods=['POST'])
def recherche():
    data = request.get_json()  # Récupérer les données POST
    phrase = data['phrase']  # Extraire la phrase à rechercher
    workspace_id = data.get('workspace_id')  # Extraire l'ID de l'espace de travail (s'il est fourni)

    # Découper la phrase en mots
    mots = phrase.split()

    # Requête SQL pour rechercher les correspondances dans la base de données
    sql_query = """
    SELECT DISTINCT file_name 
    FROM repeated_words 
    WHERE """

    if workspace_id:
        sql_query += "workspace_id = %s AND "

    sql_query += " ("

    for i in range(len(mots)):
        sql_query += "word LIKE %s"
        if i < len(mots) - 1:
            sql_query += " OR "

    sql_query += ")"

    if workspace_id:
        sql_query += "GROUP BY file_name HAVING COUNT(DISTINCT word) = %s"

    # Exécuter la requête SQL
    if workspace_id:
        params = tuple([workspace_id] + ['%' + mot + '%' for mot in mots] + [len(mots)])
    else:
        params = tuple(['%' + mot + '%' for mot in mots])

    cursor.execute(sql_query, params)
    resultats = cursor.fetchall()

    # Formater les résultats
    resultats_formatés = [row[0] for row in resultats]

    if not resultats_formatés:
        return "Désolé, je n'ai pas trouvé ce que vous voulez. Pouvez-vous préciser votre recherche ?", 404

    return jsonify(resultats_formatés)


if __name__ == '__main__':
    app.run(debug=True, port=5002)
