# Modulo que utiliza la API de Brevo (SendInBlue) para crear campañas de email marketing y enviar los mails
from __future__ import print_function
from Contacto import *
import sib_api_v3_sdk
from sib_api_v3_sdk.rest import ApiException
from pprint import pprint
from Contacto import Contacto


class Brevo:
    def __init__(self):
        # Configure API key authorization: api-key
        self.configuration = sib_api_v3_sdk.Configuration()
        self.configuration.api_key['api-key'] = "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"

        # create an instance of the API class
        self.api_instance = sib_api_v3_sdk.ContactsApi(sib_api_v3_sdk.ApiClient(self.configuration))

    def post_contacto(self,contact:Contacto):

        create_contact = sib_api_v3_sdk.CreateContact(
          email= contact.email,
          attributes={"FNAME": contact.nombre, "LNAME": ""},
          list_ids=[11],
          ext_id= str(contact.id),
          email_blacklisted=False,
          sms_blacklisted=True,
          update_enabled=False
        ) # CreateContact | Values to create a contact

        try:
            # Create a contact
            api_response = self.api_instance.create_contact(create_contact)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling ContactsApi->create_contact: %s\n" % e)

        return api_response
