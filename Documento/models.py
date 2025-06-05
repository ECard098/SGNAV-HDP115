from django.db import models

# Create your models here.

class Documento(models.Model):
    # Opciones para el campo 'tipo'
    TIPO_OPCIONES = [
        ('factura', 'Factura comercial'),
        ('lista_embalaje', 'Lista de embalaje'),
        ('iva', 'Declaración de IVA'),
        ('aviso_embarque', 'Aviso de embarque'),
    ]

    # Opciones para el campo 'estado'
    ESTADO_OPCIONES = [
        ('pendiente', 'Pendiente'),
        ('valido', 'Válido'),
        ('rechazado', 'Rechazado'),
    ]

    tipo = models.CharField(max_length=20, choices=TIPO_OPCIONES)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    ruta_archivo = models.FileField(upload_to='documentos_pdfs/')
    estado = models.CharField(max_length=10, choices=ESTADO_OPCIONES, default='pendiente')
    observacionDocumento = models.TextField(blank=True, null=True)

