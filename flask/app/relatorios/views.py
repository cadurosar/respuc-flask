from flask import flash, redirect, render_template, url_for
from flask_login import login_required

import plotly
import plotly.graph_objs as go
from plotly.offline import plot
from markupsafe import Markup

from . import relatorios
from .. import db
from ..models import Pessoa

@relatorios.route('/relatorios', methods=['GET', 'POST'])
@login_required
def relatorio():

    ################  GRÁFICO PIZZA DIVISAO POR SEXO ###############

    #  QUAL O NUMERO PARA MASCULINO / FEMININO ???
    qtd_masculino = db.session.query(Pessoa.rg_numero).filter(Pessoa.sexo == 1).count()
    qtd_feminino = db.session.query(Pessoa.rg_numero).filter(Pessoa.sexo == 0).count()

    trace_sexo = {
        'values': [qtd_masculino, qtd_feminino],
        'labels': ['Masculino', 'Feminino'],
        'hoverinfo': 'label+percent',
        'type': 'pie'
    }

    figure_sexo = {
        'data': [trace_sexo],
        'layout': {
            'height': 600,
            'plot_bgcolor': 'rgba(0,0,0,0)',
            'paper_bgcolor': 'rgba(0,0,0,0)',
            'legend': {
                'font': {
                    'size': 18
                },
                'x': 0.2,
                'y': 0
            }
        }
    }

    grafico_divisao_sexo = plot(figure_sexo, output_type='div')

    #######################################################################


    ################  GRÁFICO PIZZA DIVISAO POR IDADE ###############

    # É NECESSARIO ADAPTAR PRA LEVAR EM CONSIDERAÇÃO A DATA ATUAL
    qtd_14_15_anos = db.session.query(Pessoa.rg_numero).filter(Pessoa.data_nascimento.between('2003-08-22', '2004-08-22')).count()
    qtd_16_17_anos = db.session.query(Pessoa.rg_numero).filter(Pessoa.data_nascimento.between('2002-08-22', '2003-08-22')).count()
    qtd_18_anos = db.session.query(Pessoa.rg_numero).filter(Pessoa.data_nascimento >= '2002-08-22').count()

    trace_idade = {
        'values': [qtd_14_15_anos, qtd_16_17_anos, qtd_18_anos],
        'labels': ['14 a 15 anos', '15 a 16 anos', '18 anos'],
        'hoverinfo': 'label+percent',
        'type': 'pie'
    }

    figure_idade = {
        'data': [trace_idade],
        'layout': {
            'height': 600,
            'plot_bgcolor': 'rgba(0,0,0,0)',
            'paper_bgcolor': 'rgba(0,0,0,0)',
            'legend': {
                'font': {
                    'size': 18
                },
                'x': 0.2,
                'y': 0
            }
        }
    }

    grafico_divisao_idade = plot(figure_idade, output_type='div')

    #######################################################################



    return render_template('pessoas/relatorios.html', chartSexo=Markup(grafico_divisao_sexo), chartIdade=Markup(grafico_divisao_idade) ,title="Relatórios")
