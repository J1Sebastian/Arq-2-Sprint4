from ..models import Usuario

def get_usuarios():
    queryset = Usuario.objects.all()
    return (queryset)

def get_usuario(usuario_pk):
    usuario = Usuario.objects.get(pk=usuario_pk)
    return usuario

def create_usuario(form):
    usuario = form.save()
    usuario.save()
    return ()

def update_usuario(usuario_pk, new_usuario):
    usuario = get_usuario(usuario_pk)
    usuario.nombres = new_usuario.nombres
    usuario.apellidos = new_usuario.apellidos
    usuario.fecha_nacimiento = new_usuario.fecha_nacimiento
    usuario.genero = new_usuario.genero
    usuario.tipo_sangre = new_usuario.tipo_sangre
    usuario.save()
    return usuario