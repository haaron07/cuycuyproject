# from flask import Blueprint, request, render_template, redirect, url_for, flash
# from db import mysql

# contacts = Blueprint('contacts', __name__, template_folder='app/templates')


# @contacts.route('/')
# def Index():
#     cur = mysql.connection.cursor()
#     cur.execute('SELECT * FROM contacts')
#     data = cur.fetchall()
#     cur.close()
#     return render_template('index.html', contacts=data)

# #---------------------------------------------------------------#
# @contacts.route('/proyecto1')
# def Proyecto1():
#     cur = mysql.connection.cursor()
#     cur.execute('SELECT * FROM peliculas')
#     data = cur.fetchall()

#     return render_template('proyecto1.html', contacts=data) 

# @contacts.route('/proyecto2')
# def Proyecto2():
#     cur = mysql.connection.cursor()
#     cur.execute('SELECT * FROM contacts')
#     data = cur.fetchall()
#     cur.close()
#     return render_template('proyecto2.html', contacts=data)

# @contacts.route('/proyecto3')
# def Proyecto3():
#     cur = mysql.connection.cursor()
#     cur.execute('SELECT * FROM contacts')
#     data = cur.fetchall()
#     cur.close()
#     return render_template('proyecto3.html', contacts=data) 

# @contacts.route('/proyecto4')
# def Proyecto4():
#     cur = mysql.connection.cursor()
#     cur.execute('SELECT * FROM contacts')
#     data = cur.fetchall()
#     cur.close()
#     return render_template('proyecto4.html', contacts=data)

# @contacts.route('/proyecto5')
# def Proyecto5():
#     cur = mysql.connection.cursor()
#     cur.execute('SELECT * FROM contacts')
#     data = cur.fetchall()
#     cur.close()
#     return render_template('proyecto5.html', contacts=data)

# @contacts.route('/proyecto6')
# def Proyecto6():
#     cur = mysql.connection.cursor()
#     cur.execute('SELECT * FROM contacts')
#     data = cur.fetchall()
#     cur.close()
#     return render_template('proyecto6.html', contacts=data)                   
# #---------------------------------------------------------------#



# #---------------------------------------------------------------------------------#
# #                Propiedades de Añadir, Actualizar y Eliminar
# #---------------------------------------------------------------------------------#
# @contacts.route('/add_contact', methods=['POST'])
# def add_contact():
#     if request.method == 'POST':
#         nombre = request.form['nombre']
#         imagen1 = request.form['imagen1']
#         imagen2 = request.form['imagen2']
#         imagen3 = request.form['imagen3']
#         imagen4 = request.form['imagen4']
#         video1 = request.form['video1']
#         video2 = request.form['video2']
#         video3 = request.form['video3']
#         video4 = request.form['video4']
#         try:
#             cur = mysql.connection.cursor()
#             cur.execute(
#                 "INSERT INTO peliculas (Nombre,Imagen1,Imagen2,Imagen3,Imagen4,Video1,Video2,Video3,Video4) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)", (nombre,imagen1,imagen2,imagen3,imagen4,video1,video2,video3,video4))
#             mysql.connection.commit()
#             flash('Contact Added successfully')
#             return redirect(url_for('contacts.Index'))
#         except Exception as e:
#             flash(e.args[1])
#             return redirect(url_for('contacts.Index'))


# @contacts.route('/edit/<id>', methods=['POST', 'GET'])
# def get_contact(id):
#     cur = mysql.connection.cursor()
#     cur.execute('SELECT * FROM peliculas WHERE id = %s', (id))
#     data = cur.fetchall()
#     cur.close()
#     print(data[0])
#     return render_template('edit-contact.html', contact=data[0])


# @contacts.route('/update/<id>', methods=['POST'])
# def update_contact(id):
#     if request.method == 'POST':
        
#         nombre = request.form['nombre']
#         imagen1 = request.form['imagen1']
#         imagen2 = request.form['imagen2']
#         imagen3 = request.form['imagen3']
#         imagen4 = request.form['imagen4']
#         video1 = request.form['video1']
#         video2 = request.form['video2']
#         video3 = request.form['video3']
#         video4 = request.form['video4']

#         cur = mysql.connection.cursor()
#         cur.execute("""
#             UPDATE peliculas
#             SET Nombre = %s,
#                 Imagen1 = %s,
#                 Imagen2 = %s,
#                 Imagen3 = %s,
#                 Imagen4 = %s,
#                 Video1 = %s,
#                 Video2 = %s,
#                 Video3 = %s,
#                 Video4 = %s
#             WHERE id = %s
#         """, (nombre,imagen1,imagen2,imagen3,imagen4,video1,video2,video3,video4,id))
#         flash('Contact Updated Successfully')
#         mysql.connection.commit()
#         return redirect(url_for('contacts.Index'))


# @contacts.route('/delete/<string:id>', methods=['POST', 'GET'])
# def delete_contact(id):
#     cur = mysql.connection.cursor()
#     cur.execute('DELETE FROM peliculas WHERE id = {0}'.format(id))
#     mysql.connection.commit()
#     flash('Contact Removed Successfully')
#     return redirect(url_for('contacts.Index'))

# #---------------------------------------------------------------------------------#