import psycopg2
from flask import jsonify


def saveExecute(data):
    conn = psycopg2.connect(
        dbname="activitiesdb",
        user="admin",
        password="admin",
        host="18.230.95.142",
        port="5432"
    )

    cur = conn.cursor()
    insert_query = """
        INSERT INTO activities (categoria, classificacao, descricao, horas, horas_aproveitadas)
        VALUES (%s, %s, %s, %s, %s);
    """
    print(data)
    dados = (data['categoria'], data['classificacao'], data['descricao'], data['horas'], data['horasAproveitadas'])

    cur.execute(insert_query, dados)
    conn.commit()
    cur.close()
    conn.close()


def querySum():
    conn = psycopg2.connect(
        dbname="activitiesdb",
        user="admin",
        password="admin",
        host="localhost",
        port="5432"
    )

    cur = conn.cursor()

    query = """
        SELECT categoria, SUM(CAST(horas_aproveitadas AS DECIMAL) ) AS total_horas_aproveitadas
        FROM activities
        GROUP BY categoria
    """

    cur.execute(query)
    resultados = cur.fetchall()

    categorias = []
    for row in resultados:
        categorias.append({
            "categoria": row[0],
            "total_horas_aproveitadas": row[1]
        })

    return jsonify(categorias)

    cur.close()
    conn.close()

def queryDescriptions():
    conn = psycopg2.connect(
        dbname="activitiesdb",
        user="admin",
        password="admin",
        host="18.230.95.142",
        port="5432"
    )

    cur = conn.cursor()

    query = """
        SELECT descricao, horas_aproveitadas FROM activities
    """

    cur.execute(query)
    resultados = cur.fetchall()

    desc = []
    for row in resultados:
        desc.append({row[0]: row[1]})

    print(resultados)
    print(desc)
    return jsonify(desc)
