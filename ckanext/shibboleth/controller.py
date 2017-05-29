'''
Repoze.who Shibboleth controller
'''

import logging

from pylons.i18n import _

import ckan.controllers.user as user
#import ckantoolkit.base as base
import ckan.plugins.toolkit as toolkit

log = logging.getLogger(__name__)


class ShibbolethController(user.UserController):

    def shiblogin(self):
        if toolkit.c.userobj is not None:
            log.info("Repoze.who Shibboleth controller received userobj %r " % base.c.userobj)
            return toolkit.h.redirect_to(controller='user',
                                      action='read',
                                      id=toolkit.c.userobj.name)
        else:
            log.error("No userobj received in Repoze.who Shibboleth controller %r " % toolkit.c)
            toolkit.h.flash_error(_("No user info received for login"))
            return toolkit.h.redirect_to('/')
