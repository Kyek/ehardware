import re
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

CURP_REGEX = r'^[A-Z]{1}[AEIOUX]{1}[A-Z]{2}\d{2}(?:0[1-9]|1[0-2])(?:0[1-9]|[12]\d|3[01])[HM]{1}(?:AS|B[CS]|C[CLMSH]|D[FG]|G[TR]|HG|JC|M[CNS]|N[ETL]|OC|PL|Q[TR]|S[PLR]|T[CSL]|VZ|YN|ZS)[B-DF-HJ-NP-TV-Z]{3}[\dA-Z]{1}\d{1}$'

def validate_curp(value):
    """
    Validates string for CURP.
    """
    if not value:
        return
        
    curp_upper = value.upper()
    
    if not re.match(CURP_REGEX, curp_upper):
        raise ValidationError(
            _('%(value)s is not a valid CURP format.'),
            params={'value': value},
        )