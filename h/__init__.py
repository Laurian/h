def includeme(config):
    config.include('h.api')
    config.include('h.app')
    config.include('h.layouts')
    config.include('h.models')
    config.include('h.panels')
    config.include('h.resources')
    config.include('h.subscribers')
    config.include('h.views')
    config.include('velruse.app')


def create_app(settings):
    from horus import groupfinder
    from pyramid.config import Configurator
    from pyramid.authentication import AuthTktAuthenticationPolicy
    from pyramid.authorization import ACLAuthorizationPolicy

    settings.setdefault('horus.activation_class', 'h.models.Activation')
    settings.setdefault('horus.user_class', 'h.models.User')

    authn_policy = AuthTktAuthenticationPolicy(
        settings['auth.secret'],
        callback=groupfinder
    )

    authz_policy = ACLAuthorizationPolicy()

    config = Configurator(
        settings=settings,
        authentication_policy=authn_policy,
        authorization_policy=authz_policy,
        root_factory='h.resources.RootFactory'
    )

    config.include(includeme)
    return config.make_wsgi_app()


def main(global_config, **settings):
    return create_app(settings)

from ._version import get_versions
__version__ = get_versions()['version']
del get_versions
