from flask import Flask, render_template, redirect, url_for
from .config import Config
from .models import db, Autor, Livro
from .forms import AutorForm, LivroForm

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)

    # Criação do banco de dados na primeira execução
    with app.app_context():
        db.create_all()

    @app.route("/autores", methods=["GET", "POST"])
    def autores():
        form = AutorForm()
        autores = Autor.query.all()
        if form.validate_on_submit():
            novo_autor = Autor(nome=form.nome.data)
            db.session.add(novo_autor)
            db.session.commit()
            return redirect(url_for("autores"))
        return render_template("autores.html", form=form, autores=autores)

    @app.route("/", methods=["GET", "POST"])
    @app.route("/livros", methods=["GET", "POST"])
    def livros():
        form = LivroForm()
        livros = Livro.query.all()
        if form.validate_on_submit():
            novo_livro = Livro(
                titulo=form.titulo.data,
                ano_publicacao=form.ano_publicacao.data,
                autor=form.autor.data
            )
            db.session.add(novo_livro)
            db.session.commit()
            return redirect(url_for("livros"))
        return render_template("livros.html", form=form, livros=livros)

    return app
