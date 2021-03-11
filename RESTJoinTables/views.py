from RESTJoinTables.serializers import JoinTableSerialize
from RESTJoinTables.models import JoinTablesmodel
from rest_framework import viewsets

class JoinTableApi(viewsets.ModelViewSet):
    queryset = JoinTablesmodel.objects.raw('SELECT PdInf.prd_name, PdInf.prd_cat, PdInf.prd_price, PdInf.prd_id, PdDet.prd_desc FROM Product_info PdInf LEFT OUTER JOIN Product_detail PdDet ON PdInf.prd_id = PdDet.prd_id')
    serializer_class = JoinTableSerialize