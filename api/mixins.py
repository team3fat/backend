from diquecito.models import *
from api.views import *
from .serializers import UsuarioSerializer, PostSerializer, ReservationSerializer, QualificationSerializer, CalendarioSerializer




class MesYAnioLookupMixin(object):
    def get_object(self):
        queryset = self.get_queryset()             # Get the base queryset
        filter = {}

        # TODO: creando filtro en base a querys "mes" y "anio" ==> date(mm/aaaa)
        # Controlar que esten presentes ambos atributos mes y anio, si falta alguno 
        #se retorna 400
        for field in self.lookup_url_kwarg:
            if self.kwargs[field]:  # Ignore empty fields.
                filter[field] = self.kwargs[field]



        # TODO: filtrar en base a la date del filtro, ignorando los dias y considerando 
        #"date<=final" && "date>=inicio"
        #obj = get_list_or_404(queryset, **filter)  # Lookup the object
        #self.check_object_permissions(self.request, obj)

        # Return deberia ser una lista con todas las reservation que tengan
        #"inicio" y/o "final" dentro del mes "date"
        return obj