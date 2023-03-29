from rest_framework.response import Response
from rest_framework.decorators import api_view
from vpn.models import VpnList,Form,Specification,Device,Location,Service
from .serializers import VpnList_Serializer,Form_Serializer,Specification_Serializer,Device_Serializer,Location_Serializer,Service_Serializer
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.renderers import JSONRenderer
import io
from rest_framework.parsers import JSONParser
from django.http import FileResponse

@api_view(['GET'])
def Instruction(request):
    instruction =(
        ('','instructions'),
        ('/specification',"specification_of_all_vpn"),
        ('/vpn','Vpn_List'),
        ('/vpn/id','Vpn_with_id'),
        ('/vpn/id/logo','logo_of_vpn_of_id'),
        ('/device','Show all Devices'),
        ('/device/id','Specific device with its top 7 vpn'),
        ('/location','Show all Locations'),
        ('/location/id','Specific Location with its top 7 vpn'),
        ('/service','Show all services'),
        ('/service/id','Specific service with its top 7 vpn'),
        ('/form/','form details')
    )
    return Response(instruction)


@api_view(["GET"])
def Specification_without_id(request):
    specification_data_set = Specification.objects.all()
    serializer = Specification_Serializer(specification_data_set,many = True)
    return Response(serializer.data)



@api_view(["GET"])
def Vpn_without_id(request):
    vpn_list = VpnList.objects.all()
    serializer = VpnList_Serializer(vpn_list, many=True, context={'request': request})
    return Response(serializer.data)


@api_view(["GET"])
def Vpn_with_id(request,pk):
    try:
        top_10_data_object = VpnList.objects.get(title=pk)
        serializer = VpnList_Serializer(top_10_data_object,many = False,context={'request': request})
        return Response(serializer.data)
    except:
        return Response("No object present with that specific id")




@api_view(['GET'])
def get_logo_url(request, pk):
    try:
        vpn_logo = VpnList.objects.get(id=pk)
        logo_path = open(vpn_logo.logo.path, 'rb')
        print(type(logo_path))
        return FileResponse(logo_path)
    except VpnList.DoesNotExist:
        return Response("No object present with that specific id")

@api_view(['GET'])
def DeviceWithoutId(request):
    deviceset = Device.objects.all()
    DeviceName =[]
    for device in deviceset:
        DeviceName.append(device.name)
    return Response(DeviceName)    


@api_view(['GET'])
def DeviceWithId(request,pk): 
    try:
        deviceobject = Device.objects.get(name = pk)
        serializer = Device_Serializer(deviceobject,context = {'request':request})
        return Response(serializer.data)
    except:
        return Response("Id is invalid")    



@api_view(['GET'])
def LocationWithoutId(request):
    locationset = Location.objects.all()
    locationName =[]
    for location in locationset:
        locationName.append(location.name)   
    return Response(locationName)    


@api_view(['GET'])
def LocationWithId(request,pk): 
    try:
        Locationobject = Location.objects.get(name = pk)
        serializer = Location_Serializer(Locationobject,context = {'request':request})
        return Response(serializer.data)
    except:
        return Response("Id is invalid")   


@api_view(['GET'])
def ServiceWithoutId(request):
    serviceset = Service.objects.all()
    serviceName =[]
    for service in serviceset:
        serviceName.append(service.name)   
    return Response(serviceName)  



@api_view(['GET'])
def ServiceWithId(request,pk): 
    try:
        serviceobject = Service.objects.get(name = pk)
        serializer = Service_Serializer(serviceobject,context = {'request':request})
        return Response(serializer.data)
    except:
        return Response("Id is invalid") 



@api_view(['GET','POST','PUT'])
def Form_without_id(request):
        if request.method == 'POST':
            try:
                
                json_input = request.body
                stream = io.BytesIO(json_input)
                parsed_data = JSONParser().parse(stream)
                serializer = Form_Serializer(data=parsed_data)
                if serializer.is_valid():
                    serializer.save()
                    return Response("successfully saved")
                else:
                    return Response(serializer.errors)
            except Exception:
                return Response("Error occurs")

        Form_set = Form.objects.all()
        serializer = Form_Serializer(Form_set, many=True)
        return Response(serializer.data)
    



    