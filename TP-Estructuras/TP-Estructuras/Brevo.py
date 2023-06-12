# Modulo que utiliza la API de Brevo (SendInBlue) para crear campañas de email marketing y enviar los mails
from __future__ import print_function
import sib_api_v3_sdk
from sib_api_v3_sdk.rest import ApiException
from pprint import pprint

api_key = ""

class Brevo_contactos:
    def __init__(self):
        # Configure API key authorization: api-key
        self.configuration = sib_api_v3_sdk.Configuration()
        self.configuration.api_key['api-key'] = api_key

        # create an instance of the API class
        self.api_instance = sib_api_v3_sdk.ContactsApi(sib_api_v3_sdk.ApiClient(self.configuration))

#CONTACTOS
    def post_contacto(self,contact):

        create_contact = sib_api_v3_sdk.CreateContact(
          email= contact.email,
          attributes={"NOMBRE": contact.nombre, "APELLIDOS": ""},
          list_ids=[11],
          email_blacklisted=False,
          sms_blacklisted=True,
          update_enabled=False
        ) # CreateContact | Values to create a contact

        try:
            # Create a contact
            api_response = self.api_instance.create_contact(create_contact)
        except ApiException as e:
            print("Exception when calling ContactsApi->create_contact: %s\n" % e)

        return api_response
    def update_contacto(self, contact):
        id_contact = contact.email
        print(id_contact)
        update_contact = sib_api_v3_sdk.UpdateContact(attributes={'NOMBRE': contact.nombre}, sms_blacklisted=True)
        print(update_contact)

        try:
            api_response = self.api_instance.update_contact(identifier = id_contact, update_contact = update_contact)
        except ApiException as e:
            print("Exception when calling ContactsApi->update_contact: %s\n" % e)

        print(api_response)
    def get_contactos(self):
        limit = 50
        offset = 0
        modified_since = '2020-09-20T19:20:30+01:00'

        try:
            api_response = self.api_instance.get_contacts(limit=limit, offset=offset, modified_since=modified_since)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling ContactsApi->get_contacts: %s\n" % e)

#FOLDERS --> Es un objeto que no contempla nuestra app. Son carpetas de listas de contactos.
    def get_folders(self):
        limit = 10
        offset = 0

        try:
            api_response = self.api_instance.get_folders(limit, offset)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling ContactsApi->get_folders: %s\n" % e)

#LISTAS DE CONTACTOS
#
#    
    def post_lista_contactos(self,ListaContactos):
        create_list = sib_api_v3_sdk.CreateList(name=ListaContactos.nombre_lista_contacto, folder_id=1)

        try:
            api_response = self.api_instance.create_list(create_list)
        except ApiException as e:
            print("Exception when calling ContactsApi->create_list: %s\n" % e)

        return api_response

    def delete_lista_contactos(self, ListaContactos):
        list_id = ListaContactos.ID_lista_contactos

        try:
            self.api_instance.delete_list(list_id)
        except ApiException as e:
            print("Exception when calling ListsApi->delete_list: %s\n" % e)

    def post_contactos_form_lista_contactos(self, ID_lista_contactos, ListaContactos):
        contact_ids = sib_api_v3_sdk.AddContactToList()
        contact_ids.ids = ListaContactos

        try:
            api_response = self.api_instance.add_contact_to_list(ID_lista_contactos, contact_ids)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling ListsApi->add_contact_to_list: %s\n" % e)


#CAMPAÑAS
class Brevo_campañas:
    def __init__(self):
        # Configure API key authorization: api-key
        self.configuration = sib_api_v3_sdk.Configuration()
        self.configuration.api_key['api-key'] = api_key

        # create an instance of the API class
        self.api_instance = sib_api_v3_sdk.EmailCampaignsApi(sib_api_v3_sdk.ApiClient(self.configuration))

    def post_campaña(self, campaña):
        sender = {"name": 'senderName', "email": 'sender@domain.com'}
        name = campaña.nombre_campana
        template_id= campaña.id_mail
        scheduled_at = campaña.fecha
        subject = campaña.descripcion
        reply_to = 'replyto@domain.com'
        recipients = {"listIds": [campaña.ID_lista_contactos]}
        email_campaigns = sib_api_v3_sdk.CreateEmailCampaign(sender=sender, name=name, template_id=template_id, scheduled_at=scheduled_at, subject=subject, reply_to=reply_to, recipients=recipients) # CreateEmailCampaign | Values to create a campaign

        try:
            api_response = self.api_instance.create_email_campaign(email_campaigns)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling EmailCampaignsApi->create_email_campaign: %s\n" % e)
    def delete_campaña(self, campaña):
        campaign_id = campaña.id_campaña

        try:
            self.api_instance.delete_email_campaign(campaign_id)
        except ApiException as e:
            print("Exception when calling EmailCampaignsApi->delete_email_campaign: %s\n" % e)