# from email.headerregistry import ContentTypeHeader
# from unittest import result
# from xhtml2pdf import pisa
# from django.template.loader import get_template
# from django.http import HttpResponse
# from io import BytesIO

# def render_pdf(template_src,context_dict={}):
#     template = get_template(template_src)
#     html = template.render(context_dict)
#     pdf = pisa.pisaDocument{BytesIO(html.encode("ISO-8859-1")), result}
#     if not pdf.err:    
#         return HttpResponse(result.getvalue(), ContentTypeHeader"application/pdf")
#     return None
