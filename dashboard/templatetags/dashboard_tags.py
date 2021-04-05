from django import template

register = template.Library()


@register.filter(name='filename')
def filename(file):
  # Return the name of the File only from filepath
  ff = str(file).strip("change/attachments/")
  return ff
