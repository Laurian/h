import colander
import deform

from h import api
from horus import schemas
from pyramid_deform import CSRFSchema


class ActivationCodeSchema(schemas.ResetPasswordSchema):
    code = colander.SchemaNode(
        colander.String(),
        title="Security Code"
    )


class PersonaSchema(CSRFSchema):
    id = colander.SchemaNode(
        colander.Integer(),
        widget=colander.deferred(
            lambda node, kw: deform.widget.SelectWidget(
                values=api.personas(kw['request']),
                css_class='dropdown-menu pull-right',
                template='tinyman'
            ),
        ),
        missing=-1
    )
