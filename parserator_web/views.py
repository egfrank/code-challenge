import usaddress
from django.views.generic import TemplateView
from rest_framework.exceptions import ParseError
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView


class Home(TemplateView):
    template_name = "parserator_web/index.html"


class AddressParse(APIView):
    renderer_classes = [JSONRenderer]

    def get(self, request):
        # TODO: Flesh out this method to parse an address string using the
        # parse() method and return the parsed components to the frontend.
        input_string = request.GET.get("address", "")
        if input_string == "":
            raise ParseError(
                {
                    "error": (
                        "Please add an address to parse."
                    )
                }
            )

        try:
            address_components, address_type = self.parse(input_string)
        except usaddress.RepeatedLabelError:
            raise ParseError(
                {
                    "error": (
                        "Unable to parse this value due to repeated labels."
                    )
                }
            )
        output = {
            "input_string": input_string,
            "address_components": address_components,
            "address_type": address_type,
        }
        return Response(output)

    def parse(self, address):
        return usaddress.tag(address)
