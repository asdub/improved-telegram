from django.forms.widgets import ClearableFileInput
from django.utils.translation import gettext_lazy as _


class CustomClearableFileInput(ClearableFileInput):
    """ Django Clearable File Widget """
    clear_checkbox_label = _('Remove')
    initial_text = _('Current Image')
    input_text = _('')
    name = 'products/custom_widget_templates/custom_clearable_file_input.html'
    template_name = (name)
