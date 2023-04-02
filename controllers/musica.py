from flask import Blueprint, request, jsonify, render_template, redirect, url_for, current_app
from models import db, Musica
from flask import flash

musica_bp = Blueprint('musica_bp', __name__)

# Renderizar o formulário de cadastro de música
@musica_bp.route('/musicas/cadastrar', methods=['GET'])
def form_cadastro_musica():
    return render_template('cadastro_musica.html')

@musica_bp.route('/musicas', methods=['POST'])
def create_musica():
    titulo = request.form['titulo']
    artista = request.form['artista']
    video = request.form['video']
    link = request.form['link']
    genero = request.form.get('genero', None)

    musica = Musica(titulo=titulo, artista=artista, video=video, link=link, genero=genero)

    db.session.add(musica)
    db.session.commit()

    #return render_template('cadastro.html')
    return render_template('cadastro.html', comunicacao=f'Música {titulo}, criada com sucesso!')



# Renderizar o formulário de excluir de música
@musica_bp.route('/deletar/deletar', methods=['GET'])
def form_delete_musica():
    return render_template('deletar_musica.html')

# Deletar uma músicas por ID
@musica_bp.route('/deletar', methods=['POST'])
def delete_musica():
    ids = request.form.getlist('musica_ids[]')

    print(f'IDs: {ids}')

    if not ids:
        musicas = Musica.query.all()
        return render_template('deletar.html', musicas=musicas, comunicacao='Nenhuma música selecionada para exclusão')
    for id in ids:
        musica = Musica.query.get(id)
        if not musica:
            return render_template('deletar.html', comunicacao=f'Música não encontrada!')
        titulo = musica.titulo
        db.session.delete(musica)
    db.session.commit()

    musicas = Musica.query.all()

    if not musicas:
        return render_template('deletar.html', mensagem='Nenhuma música cadastrada')
    else:
        return render_template('index.html', musicas=musicas, comunicacao=f'Música {titulo}, excluida com sucesso!')



# Obter todas as músicas
@musica_bp.route('/musicas', methods=['GET'])
def get_musicas():
    musicas = Musica.query.all()
    return render_template('index.html', musicas=musicas)

# Obter uma música específica por ID
@musica_bp.route('/musicas/<int:musica_id>', methods=['GET'])
def get_musica(musica_id):
    musica = Musica.query.get(musica_id)

    if not musica:
        return jsonify({'message': 'Musica não encontrada'}), 404

    return jsonify(musica.__dict__)

# Atualizar uma música específica por ID
@musica_bp.route('/musicas/<int:musica_id>', methods=['POST', 'PUT'])
def update_musica(musica_id):
    musica = Musica.query.get(musica_id)

    if not musica:
        return jsonify({'message': 'Musica não encontrada'}), 404

    musica.titulo = request.form['titulo']
    musica.artista = request.form['artista']
    musica.video = request.form['video']
    musica.link = request.form['link']
    musica.genero = request.form.get('genero', None)

    db.session.commit()

    flash('Música atualizada com sucesso!')

    return redirect(url_for('musica_bp.get_musicas'))

"""# Deletar uma música específica por ID
@musica_bp.route('/musicas', methods=['POST'])
def delete_musica(musica_id):
    musica = Musica.query.get(musica_id)

    if not musica:
        return jsonify({'message': 'Musica não encontrada'}), 404

    db.session.delete(musica)
    db.session.commit()

    flash('Música deletada com sucesso!')

    return render_template('deletar.html', musica_deletada=True)"""