from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import current_user, login_required
from datetime import datetime
from .models import Pesaje, db

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
@login_required
def dashboard():
    pesajes = Pesaje.query.filter_by(usuario_id=current_user.id).all()
    return render_template('dashboard.html', pesajes=pesajes)

@main_bp.route('/pesajes', methods=['GET', 'POST'])
@login_required
def pesajes():
    if request.method == 'POST':
        try:
            peso = float(request.form.get('peso', 0))
            descripcion = request.form.get('descripcion', '').strip()
            fecha_str = request.form.get('fecha', '')

            fecha = datetime.strptime(fecha_str, '%Y-%m-%dT%H:%M') if fecha_str else datetime.utcnow()

            nuevo_pesaje = Pesaje(
                peso=peso,
                descripcion=descripcion,
                fecha=fecha,
                usuario_id=current_user.id
            )
            db.session.add(nuevo_pesaje)
            db.session.commit()
            flash('Pesaje registrado!', 'success')
            return redirect(url_for('main.dashboard'))

        except ValueError:
            flash('Error: Datos inválidos', 'danger')
    return render_template('pesajes.html', now=datetime.utcnow())