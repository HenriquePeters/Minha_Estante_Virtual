from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired
from wtforms_sqlalchemy.fields import QuerySelectField
from .models import Autor

class AutorForm(FlaskForm):
    nome = StringField("Nome do Autor", validators=[DataRequired()])
    submit = SubmitField("Cadastrar Autor")

class LivroForm(FlaskForm):
    titulo = StringField("Título do Livro", validators=[DataRequired()])
    ano_publicacao = IntegerField("Ano de Publicação", validators=[DataRequired()])
    autor = QuerySelectField(
        "Autor",
        query_factory=lambda: Autor.query.all(),
        get_label="nome",
        allow_blank=False
    )
    submit = SubmitField("Cadastrar Livro")
