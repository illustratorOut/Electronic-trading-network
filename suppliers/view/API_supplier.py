from rest_framework.generics import RetrieveAPIView, DestroyAPIView, ListAPIView, UpdateAPIView, CreateAPIView, \
    get_object_or_404
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from users.models import User
from suppliers.models import Supplier
from suppliers.permissions import IsOwner, IsActive
from suppliers.seriallizers.API_supplier import SupplierAPISerializer, SupplierAPICreateSerializer


class SupplierDetailAPIView(RetrieveAPIView):
    '''Отображение одной сущности поставщика'''
    queryset = Supplier.objects.all()
    serializer_class = SupplierAPISerializer
    permission_classes = [IsAuthenticated, IsActive]


class SupplierListAPIView(ListAPIView):
    '''Отображение списка сущностей поставщика'''
    queryset = Supplier.objects.all()
    serializer_class = SupplierAPISerializer
    permission_classes = [IsAuthenticated, IsActive]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ('country',)


class SupplierCreateAPIView(CreateAPIView):
    '''Создание сущности поставщика'''
    queryset = Supplier.objects.all()
    serializer_class = SupplierAPICreateSerializer
    permission_classes = [IsAuthenticated, IsActive]

    def perform_create(self, serializer):
        '''При создании obj присваиваем автора(user)'''
        supplier = serializer.save()
        supplier.author = get_object_or_404(User, id=self.request.user.id)
        supplier.save()


class SupplierUpdateAPIView(UpdateAPIView):
    '''Редактирование (обновление) сущности поставщика'''
    queryset = Supplier.objects.all()
    serializer_class = SupplierAPISerializer
    permission_classes = [IsAuthenticated, IsOwner, IsActive]

    def perform_update(self, serializer):
        '''При обновлении obj присваиваем '''
        update_supplier = serializer.save()
        update_supplier.save()


class SupplierDeleteAPIView(DestroyAPIView):
    '''Удаление сущности поставщика'''
    queryset = Supplier.objects.all()
    serializer_class = SupplierAPISerializer
    permission_classes = [IsAuthenticated, IsOwner, IsActive]
